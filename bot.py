import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

from infrastructure.database.setup import create_engine, create_session_pool
from tgbot.config import load_config, Config
from tgbot.dialogs.group_dialogs import menu_group, group_dialog, start_group, group_settings
from tgbot.dialogs.menu_dialogs import main_menu, user_settings, user_reminders, user_support, \
    user_info_support
from tgbot.dialogs.start_dialogs import start_bot
from tgbot.handlers import routers_list
from tgbot.middlewares.check_update import CheckUpdateMiddleware
from tgbot.middlewares.config import ConfigMiddleware
from aiogram_dialog import setup_dialogs

from tgbot.middlewares.database import DatabaseMiddleware
from tgbot.middlewares.i18n.i18n import make_i18n_middleware
from tgbot.middlewares.throttling import DynamicThrottlingMiddleware
from tgbot.misc.scheduler import load_tasks_from_db, scheduler_router
from tgbot.misc.scheduler_group import scheduler_group_router, load_tasks_from_db_group
from tgbot.services import broadcaster


async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Бот запущен и готов к работе!")


def register_global_middlewares(dp: Dispatcher, config: Config, session_pool=None):
    """
    Register global middlewares for the given dispatcher.
    Global middlewares here are the ones that are applied to all the handlers (you specify the type of update)

    :param dp: The dispatcher instance.
    :type dp: Dispatcher
    :param config: The configuration object from the loaded configuration.
    :param session_pool: Optional session pool object for the database using SQLAlchemy.
    :return: None
    """
    middleware_types = [
        ConfigMiddleware(config),
        # DatabaseMiddleware(session_pool),
    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)


class SqlAlchemyFilter(logging.Filter):
    def filter(self, record):
        # Ищем в сообщениях SQLAlchemy строки, связанные с транзакциями
        if 'BEGIN' in record.getMessage() or 'COMMIT' in record.getMessage():
            return False
        return True


def setup_logging():
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )

    # Настроим логирование для SQLAlchemy
    logger = logging.getLogger("sqlalchemy.engine")
    logger.setLevel(logging.INFO)  # Уровень INFO для SQLAlchemy

    # Удаляем все обработчики из логгера, чтобы применить свои
    for handler in logger.handlers:
        logger.removeHandler(handler)

    # Создаем новый обработчик для вывода в консоль
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s"))
    handler.addFilter(SqlAlchemyFilter())  # Применяем фильтрацию
    logger.addHandler(handler)

    # Логируем начало работы бота
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


def get_storage(config):
    """
    Return storage based on the provided configuration.

    Args:
        config (Config): The configuration object.

    Returns:
        Storage: The storage object based on the configuration.

    """
    if config.tg_bot.use_redis:
        return RedisStorage.from_url(
            config.redis.dsn(),
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )
    else:
        return MemoryStorage()


async def main():
    setup_logging()
    config = load_config(".env")
    storage = get_storage(config)
    bot = Bot(token=config.tg_bot.token, session=AiohttpSession(), default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(storage=storage)

    influx_client = InfluxDBClientAsync(
        url=config.influx_db.url,
        token=config.influx_db.token,
        org=config.influx_db.org,
    )
    influx_client.bucket = config.influx_db.bucket

    i18n_middleware = make_i18n_middleware()
    engine = create_engine(config.db, echo=True)
    session = create_session_pool(engine)
    scheduler = AsyncIOScheduler()
    scheduler.start()
    dp.update.outer_middleware(CheckUpdateMiddleware())
    dp.update.outer_middleware(DynamicThrottlingMiddleware(session))
    dp.update.outer_middleware(DatabaseMiddleware(session))
    dp.include_routers(*routers_list)
    dp.include_routers(scheduler_router, scheduler_group_router, start_bot, main_menu, user_settings,
                       user_reminders, user_support, user_info_support, menu_group,
                       group_dialog, start_group, group_settings)
    dp.workflow_data.update(config=config, scheduler=scheduler, session=session, influx_client=influx_client)
    dp.message.middleware(i18n_middleware)
    dp.callback_query.middleware(i18n_middleware)
    setup_dialogs(dp)
    register_global_middlewares(dp, config)
    await load_tasks_from_db(scheduler, bot, session, influx_client)
    await load_tasks_from_db_group(scheduler, bot, session, influx_client)

    await on_startup(bot, config.tg_bot.admin_ids)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}", exc_info=True)
    finally:
        logging.info("Выключение бота, закрываем соединения...")
        await bot.session.close()
        if hasattr(influx_client, "close"):
            await influx_client.close()

        logging.info("Все соединения закрыты. Завершение работы.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот был выключен!")

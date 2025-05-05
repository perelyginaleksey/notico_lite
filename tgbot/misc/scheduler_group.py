import asyncio
import logging
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from aiogram import Bot, Router, F
from aiogram.exceptions import TelegramForbiddenError
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dateutil.relativedelta import relativedelta
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from sqlalchemy import select

from infrastructure.database.models import User, Group, Group_Reminder
from infrastructure.database.repo.reminder_group import ReminderGroupRepo
from infrastructure.database.repo.requests import RequestsRepo
from tgbot.middlewares.i18n.i18n_format import localization_format_new
from tgbot.misc.locations import get_localized_date
from tgbot.misc.metrics import stat_sent_total
from tgbot.misc.reminders import delete_message_after_delay
from tgbot.misc.scheduler import reminder_keyboard_custom, send_error_to_admin

scheduler_group_router = Router()

async def remove_keyboard_after_delay(chat_id: int, message_id: int, delay: int, bot: Bot) -> None:
    """Удаляет клавиатуру сообщения в группе через указанное время."""
    pass

def reminder_keyboard_group(user_language: str, reminder_dict: dict) -> InlineKeyboardMarkup:
    """Создает клавиатуру для управления групповым напоминанием."""
    pass

async def load_tasks_from_db_group(
    scheduler: AsyncIOScheduler,
    bot: Bot,
    session_pool,
    influx_client: InfluxDBClientAsync
) -> None:
    """Загружает активные групповые напоминания из БД в планировщик."""
    pass

async def add_task_to_scheduler_group(
    scheduler: AsyncIOScheduler,
    bot: Bot,
    reminder_dict: dict,
    group_dict: dict,
    influx_client: InfluxDBClientAsync = None,
    session_pool = None,
    repo = None
) -> None:
    """Добавляет задачу отправки группового напоминания в планировщик."""
    pass

async def add_task_del_reminder_to_scheduler_group(
    scheduler: AsyncIOScheduler,
    delete_time: datetime,
    group_dict: dict,
    reminder_id: int,
    repo = None,
    temp_repo = None
) -> None:
    """Добавляет задачу удаления группового напоминания в планировщик."""
    pass

async def del_reminder_group(reminder_id: int, repo = None, temp_repo = None) -> None:
    """Удаляет групповое напоминание из базы данных."""
    pass

async def send_reminder_group(
    bot: Bot,
    reminder_dict: dict,
    group_dict: dict,
    scheduler: AsyncIOScheduler,
    influx_client: InfluxDBClientAsync = None,
    session_pool = None,
    repo = None
) -> None:
    """Отправляет групповое напоминание и обрабатывает периодические."""
    pass

@scheduler_group_router.callback_query(F.data.startswith("greminder"))
async def process_group_callback(
    call: CallbackQuery,
    repo: RequestsRepo,
    user: User,
    scheduler: AsyncIOScheduler,
    influx_client: InfluxDBClientAsync,
    **kwargs
) -> None:
    """Обрабатывает callback-действия с групповыми напоминаниями."""
    pass
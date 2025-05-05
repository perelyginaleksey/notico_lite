import asyncio
import logging
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.widgets.kbd import Select, Button, ListGroup
from aiogram.types import LabeledPrice
from dateutil.relativedelta import relativedelta

from infrastructure.database.models import User
from infrastructure.database.repo.requests import RequestsRepo
from tgbot.config import Config
from tgbot.dialogs.states import StartBot, MainMenu, UserSettings, UserReminders, UserSupport, UserInfo
from tgbot.middlewares.i18n.i18n_format import I18N_FORMAT_KEY, localization_format, localization_format_new
from tgbot.misc.check import send_follow_channel
from tgbot.misc.metrics import stat_add_total
from tgbot.misc.reminders import delete_message_after_delay
from tgbot.misc.scheduler import add_task_to_scheduler, add_task_del_reminder_to_scheduler


async def choice_lang(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Выбор языка пользователем."""
    pass


async def back(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Возврат после выбора языка."""
    pass


async def to_switch_format(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Смена формата времени пользователем."""
    pass


async def to_main_menu(c: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход в главное меню."""
    pass


async def back_timezone(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Возврат к выбору таймзоны."""
    pass


async def check_follow(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Проверка подписки пользователя на канал."""
    pass


async def settings_confirm(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Подтверждение настроек и завершение регистрации."""
    pass


async def to_settings(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход в настройки пользователя."""
    pass


async def to_donation(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к окну поддержки проекта"""
    pass


async def add_reminder(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к добавлению напоминания"""
    pass


async def add_reminder_in_menu(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Добавить напоминание из главного меню"""
    pass


async def to_list_reminders(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к списку напоминаний"""
    pass


async def no_thanks(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Отказ после добавления напоминания"""
    pass


async def to_changes_language(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к изменению языка"""
    pass


async def to_changes_utc(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к изменению часового пояса"""
    pass


async def user_back_settings(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Назад к настройкам"""
    pass


async def user_back_changes_utc(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Назад к изменению часового пояса"""
    pass


async def to_edit_time_reminder(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к изменению времени напоминания"""
    pass


async def to_user_edit_period(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к изменению периодичности напоминания"""
    pass


async def to_select_reminder(call: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id):
    """Выбор напоминания"""
    pass


async def go_select_reminder(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Назад к выбранному напоминанию"""
    pass


async def edit_reminder(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Редактирование напоминания"""
    pass


async def back_to_add_reminder(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Возврат к добавлению напоминания"""
    pass


async def to_send_settings(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к настройкам отправки"""
    pass


async def delete_button(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Удаление пользовательской кнопки"""
    pass


async def switch_standard(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переключение параметров по умолчанию"""
    pass


async def add_custom_buttons(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Добавление пользовательской кнопки"""
    pass


async def reminder_preview(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Предпросмотр напоминания"""
    pass


async def confirm_reminder(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Подтверждение добавления напоминания"""
    pass


async def confirm_edit_reminder(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Подтверждение изменения времени напоминания"""
    pass


async def pay_stars(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Создание инвойса для доната"""
    pass


async def confirm_edit_period(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Подтверждение изменения периодичности"""
    pass


async def to_support_info(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход в раздел информации и помощи"""
    pass


async def to_info(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход в раздел информации"""
    pass


async def to_help(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход в раздел помощи"""
    pass


async def time_formats(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к форматам напоминаний"""
    pass


async def to_error_reminder(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Переход к сообщению об ошибке при добавлении напоминания"""
    pass


async def reminder_edit_name(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Редактирование названия напоминания"""
    pass


async def switch_status(call: CallbackQuery, button: Button, manager: DialogManager):
    """Переключает статус напоминания (активно/неактивно)."""
    pass

async def update_reminder(call: CallbackQuery, button: Button, manager: DialogManager):
    """Обновляет время периодического напоминания."""
    pass

async def delete_reminder(call: CallbackQuery, button: Button, manager: DialogManager):
    """Удаляет напоминание и задачу."""
    pass

async def recover_reminder(call: CallbackQuery, button: Button, manager: DialogManager):
    """Восстанавливает напоминание."""
    pass

async def choice_lang_new(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Меняет язык бота."""
    pass

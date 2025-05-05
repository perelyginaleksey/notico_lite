import logging
import re
from zoneinfo import ZoneInfo

from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, Group, Url
from aiogram_dialog.widgets.text import Format
from aiogram_i18n.types import LabeledPrice

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.dialogs.callbacks import to_main_menu, delete_button
from tgbot.dialogs.states import StartBot, UserSettings, UserReminders, UserSupport
from tgbot.middlewares.i18n.i18n_format import I18NFormat, localization_format_new
from tgbot.misc.locations import get_timezone_new, get_timezone, get_ex_reminders
from tgbot.misc.reminders import get_time_from_text, format_periodicity, get_period_from_text
from tgbot.misc.scheduler import add_task_to_scheduler


def get_common_buttons() -> list:
    """Возвращает список общих кнопок для меню."""
    pass

async def get_language(dialog_manager: DialogManager, **kwargs):
    """Получает текущий язык пользователя."""
    pass

async def utc_error(dialog_manager: DialogManager, **kwargs):
    """Возвращает сообщение об ошибке с городом."""
    pass

async def process_city(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    """Обрабатывает выбор города для часового пояса."""
    pass

async def get_time_user(dialog_manager: DialogManager, **kwargs):
    """Получает время и часовой пояс пользователя."""
    pass

async def get_user_settings(dialog_manager: DialogManager, **kwargs):
    """Получает настройки пользователя (язык, часовой пояс, формат времени)."""
    pass

async def get_nearest_reminder(dialog_manager: DialogManager, **kwargs):
    """Получает ближайшее активное напоминание."""
    pass

async def get_user_data_with_reminders(dialog_manager: DialogManager, **kwargs):
    """Получает данные пользователя и его напоминания."""
    pass

async def get_reminders_window_title(dialog_manager: DialogManager, **kwargs) -> dict:
    """Получает список напоминаний для отображения."""
    pass

async def get_send_settings_date(dialog_manager: DialogManager, **kwargs) -> dict:
    """Возвращает данные настроек для отправки."""
    pass

async def set_reminders(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    """Обрабатывает создание нового напоминания."""
    pass


async def set_period(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    """Устанавливает периодичность напоминания."""
    pass

async def get_stars_for_invite(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    """Обрабатывает ввод количества Telegram Stars для доната."""
    pass

async def edit_name_reminder(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    """Изменяет название напоминания."""
    pass

async def edit_time_reminder(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    """Изменяет время напоминания."""
    pass

async def get_reminder_date(dialog_manager: DialogManager, **kwargs):
    """Получает данные о дате и периодичности напоминания."""
    pass

async def get_reminder_preview_date(dialog_manager: DialogManager, **kwargs):
    """Получает данные для предпросмотра напоминания."""
    pass

async def on_button_input(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    """Добавляет кнопку к напоминанию."""
    pass

async def get_buttons_date(dialog_manager: DialogManager, **kwargs) -> dict:
    """Получает список кнопок для напоминания."""
    pass

async def get_reminder_info(dialog_manager: DialogManager, **kwargs):
    """Получает информацию о напоминании."""
    pass

import logging
import re
from zoneinfo import ZoneInfo

from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.dialogs.states import GroupStart, GroupSettings, GroupReminders
from tgbot.misc.locations import get_timezone, get_timezone_new
from tgbot.misc.reminders import get_time_from_text, format_periodicity, get_period_from_text
from tgbot.misc.scheduler_group import add_task_to_scheduler_group


async def get_group_window_title(dialog_manager: DialogManager, **kwargs) -> dict:
    """Получает список групп пользователя."""
    pass

async def get_group_select(dialog_manager: DialogManager, **kwargs) -> dict:
    """Получает данные выбранной группы."""
    pass

async def get_language_group(dialog_manager: DialogManager, **kwargs):
    """Получает язык группы."""
    pass

async def get_time_group(dialog_manager: DialogManager, **kwargs):
    """Получает часовой пояс и время группы."""
    pass

async def group_process_city(message: Message, message_input, dialog_manager: DialogManager):
    """Обрабатывает ввод города для часового пояса группы."""
    pass

async def get_reminders_group_window(dialog_manager: DialogManager, **kwargs) -> dict:
    """Получает список напоминаний группы."""
    pass

async def get_group_settings(dialog_manager: DialogManager, **kwargs):
    """Получает настройки группы (язык, часовой пояс)."""
    pass

async def set_reminders_group(message: Message, message_input, dialog_manager: DialogManager):
    """Создает новое напоминание для группы."""
    pass

async def get_send_settings_date_group(dialog_manager: DialogManager, **kwargs) -> dict:
    """Получает настройки отправки напоминания группы."""
    pass

async def on_button_input_group(message: Message, message_input, dialog_manager: DialogManager):
    """Добавляет пользовательскую кнопку к напоминанию группы."""
    pass

async def get_buttons_date_group(dialog_manager: DialogManager, **kwargs) -> dict:
    """Получает список пользовательских кнопок напоминания."""
    pass

async def get_reminder_preview_date_group(dialog_manager: DialogManager, **kwargs):
    """Получает данные для предпросмотра напоминания группы."""
    pass

async def edit_name_reminder_group(message: Message, message_input, dialog_manager: DialogManager):
    """Изменяет название напоминания группы."""
    pass

async def edit_time_reminder_group(message: Message, message_input, dialog_manager: DialogManager):
    """Изменяет время напоминания группы."""
    pass

async def get_add_reminder_date_group(dialog_manager: DialogManager, **kwargs):
    """Получает данные для добавления напоминания группы."""
    pass

async def get_reminder_new_period_group(dialog_manager: DialogManager, **kwargs):
    """Получает новый период напоминания группы."""
    pass

async def get_add_error_reminder_date_group(dialog_manager: DialogManager, **kwargs):
    """Получает данные об ошибке добавления напоминания."""
    pass

async def get_reminder_error_edit_period(dialog_manager: DialogManager, **kwargs):
    """Получает данные об ошибке редактирования периода."""
    pass

async def get_reminder_error_edit_time(dialog_manager: DialogManager, **kwargs):
    """Получает данные об ошибке редактирования времени."""
    pass

async def get_reminder_edit_text(dialog_manager: DialogManager, **kwargs):
    """Получает текст для редактирования названия напоминания."""
    pass

async def get_reminder_edit_time(dialog_manager: DialogManager, **kwargs):
    """Получает время для редактирования напоминания."""
    pass

async def get_reminder_period_group(dialog_manager: DialogManager, **kwargs):
    """Получает периодичность напоминания группы."""
    pass

async def get_reminder_info_group(dialog_manager: DialogManager, **kwargs):
    """Получает информацию о напоминании группы."""
    pass

async def get_new_reminder_time_group(dialog_manager: DialogManager, **kwargs):
    """Получает новое время напоминания группы."""
    pass

async def set_period_group(message: Message, message_input, dialog_manager: DialogManager):
    """Устанавливает периодичность напоминания группы."""
    pass

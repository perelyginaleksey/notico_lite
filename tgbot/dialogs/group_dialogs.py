from aiogram import F
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Button, ScrollingGroup, Select, Row, PrevPage, \
    CurrentPage, NextPage, Url, ListGroup
from aiogram_dialog.widgets.link_preview import LinkPreview
from aiogram_dialog.widgets.text import Const, Format, List

from tgbot.dialogs.callbacks import to_main_menu
from tgbot.dialogs.getters import utc_error
from tgbot.dialogs.group_callbacks import to_group, to_select_group, to_list_reminders_group, to_settings_group, \
    to_select_group_reminder, add_reminder_group, back_to_select_group, choice_lang_group, back_choice_language_group, \
    back_choice_utc_group, group_settings_confirm, to_changes_group_language, to_changes_group_utc, \
    choice_group_lang_new, confirm_group_reminder, reminder_edit_name_group, to_edit_time_group_reminder, \
    to_user_edit_period_group, time_formats_group, to_error_group_reminder, switch_status_group, update_reminder_group, \
    edit_reminder_group, to_edit_time_reminder_group, delete_reminder_group, go_select_reminder_group, \
    confirm_edit_reminder_group, confirm_edit_period_group, back_to_list_reminders_group, check_follow_group, \
    no_thanks_group, to_send_settings_group, reminder_preview_group, switch_standard_group, add_custom_buttons_group, \
    back_to_add_reminder_group, delete_button_group
from tgbot.dialogs.group_getters import get_group_window_title, group_process_city, get_time_group, get_group_select, \
    get_reminders_group_window, get_group_settings, set_reminders_group, edit_name_reminder_group, \
    edit_time_reminder_group, get_add_reminder_date_group, get_add_error_reminder_date_group, \
    get_reminder_info_group, set_period_group, get_new_reminder_time_group, get_reminder_new_period_group, \
    get_reminder_error_edit_period, get_reminder_period_group, get_reminder_error_edit_time, get_reminder_edit_text, \
    get_reminder_edit_time, get_language_group, get_send_settings_date_group, on_button_input_group, \
    get_buttons_date_group, get_reminder_preview_date_group
from tgbot.dialogs.states import GroupMenu, GroupReminders, GroupStart, GroupSettings
from tgbot.middlewares.i18n.i18n_format import I18NFormat

ID_SCROLL_NO_PAGER = "scroll_no_pager"

def start_group_dialog() -> Dialog:
    """Диалог для выбора языка и часового пояса группы."""
    return Dialog(
        Window(state="GroupStart.choice_language"),  # Выбор языка
        Window(state="GroupStart.error_utc"),  # Ошибка часового пояса
        Window(state="GroupStart.choice_utc"),  # Выбор часового пояса
        Window(state="GroupStart.confirm_settings")  # Подтверждение настроек
    )

def group_settings_dialog() -> Dialog:
    """Диалог для изменения языка и часового пояса группы."""
    return Dialog(
        Window(state="GroupSettings.window_settings"),  # Главное окно настроек
        Window(state="GroupSettings.changes_language"),  # Изменение языка
        Window(state="GroupSettings.changes_utc"),  # Изменение часового пояса
        Window(state="GroupSettings.error_utc"),  # Ошибка часового пояса
        Window(state="GroupSettings.confirm_utc")  # Подтверждение часового пояса
    )

def menu_group_dialog() -> Dialog:
    """Диалог для отображения и выбора групп."""
    return Dialog(
        Window(state="GroupMenu.main_window")  # Список групп и добавление новой
    )
def group_dialog() -> Dialog:
    """Диалог для управления группами и их напоминаниями."""
    return Dialog(
        Window(state="GroupReminders.select_group_window"),  # Выбор группы
        Window(state="GroupReminders.reminders_window"),  # Список напоминаний группы
        Window(state="GroupReminders.pre_add_reminder"),  # Подготовка к добавлению напоминания
        Window(state="GroupReminders.add_reminder"),  # Добавление напоминания
        Window(state="GroupReminders.send_settings"),  # Настройки отправки напоминания
        Window(state="GroupReminders.add_buttons"),  # Добавление пользовательских кнопок
        Window(state="GroupReminders.preview_reminders"),  # Предпросмотр напоминания
        Window(state="GroupReminders.error_add_reminder"),  # Ошибка добавления напоминания
        Window(state="GroupReminders.time_formats"),  # Форматы времени напоминаний
        Window(state="GroupReminders.selected_reminder"),  # Выбранное напоминание
        Window(state="GroupReminders.edit_reminder"),  # Редактирование напоминания
        Window(state="GroupReminders.edit_name_reminder"),  # Редактирование названия
        Window(state="GroupReminders.edit_time_reminder"),  # Редактирование времени
        Window(state="GroupReminders.error_edit_time_reminder"),  # Ошибка редактирования времени
        Window(state="GroupReminders.confirm_edit_time_reminder"),  # Подтверждение времени
        Window(state="GroupReminders.edit_period_reminder"),  # Редактирование периодичности
        Window(state="GroupReminders.error_edit_period_reminder"),  # Ошибка периодичности
        Window(state="GroupReminders.confirm_edit_period_reminder"),  # Подтверждение периодичности
        Window(state="GroupReminders.follow_channel")  # Проверка подписки на канал
    )

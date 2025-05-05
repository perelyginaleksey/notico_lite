from aiogram import F
from aiogram_dialog import Dialog, Window, ShowMode
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Group, Button, ScrollingGroup, Select, Row, PrevPage, \
    CurrentPage, NextPage, ListGroup, Url
from aiogram_dialog.widgets.link_preview import LinkPreview
from aiogram_dialog.widgets.text import Const, Format, List, Text

from tgbot.dialogs.callbacks import (add_reminder, choice_lang_new, settings_confirm,
                                     to_main_menu, to_list_reminders, to_settings, to_changes_language,
                                     to_changes_utc, confirm_reminder, time_formats,
                                     to_select_reminder, switch_status, delete_reminder, recover_reminder,
                                     go_select_reminder,
                                     edit_reminder, reminder_edit_name, confirm_edit_reminder, to_edit_time_reminder,
                                     to_user_edit_period, confirm_edit_period, update_reminder, add_reminder_in_menu,
                                     check_follow, no_thanks, to_switch_format, pay_stars, to_donation, to_info,
                                     to_help, to_support_info, to_error_reminder, back_to_add_reminder,
                                     to_send_settings, switch_standard, add_custom_buttons, reminder_preview,
                                     delete_button)

from tgbot.dialogs.getters import (get_user_settings, process_city, utc_error, get_time_user, get_common_buttons,
                                   get_reminders_window_title, get_reminder_date, set_reminders, get_reminder_info,
                                   edit_name_reminder, edit_time_reminder, set_period,
                                   get_stars_for_invite, get_nearest_reminder, get_send_settings_date, on_button_input,
                                   get_buttons_date, get_reminder_preview_date)
from tgbot.dialogs.group_callbacks import to_group

from tgbot.dialogs.states import MainMenu, UserSettings, UserReminders, UserSupport, UserInfo
from tgbot.middlewares.i18n.i18n_format import I18NFormat

def main_menu_dialog() -> Dialog:
    """Главное меню для добавления напоминаний, настроек и поддержки."""
    return Dialog(
        Window(state="MainMenu.main_menu")  # Главное окно с функциями
    )

def user_support_dialog() -> Dialog:
    """Диалог для донатов через Telegram Stars."""
    return Dialog(
        Window(state="UserSupport.user_support")  # Выбор количества Stars
    )

def user_info_support_dialog() -> Dialog:
    """Диалог для информации и поддержки пользователей."""
    return Dialog(
        Window(state="UserInfo.user_support_info"),  # Главное окно поддержки
        Window(state="UserInfo.user_select_info"),  # Информация
        Window(state="UserInfo.user_select_support")  # Помощь
    )

def user_settings_dialog() -> Dialog:
    """Диалог для управления настройками пользователя."""
    return Dialog(
        Window(state="UserSettings.user_settings"),  # Главное окно настроек
        Window(state="UserSettings.user_changes_language"),  # Изменение языка
        Window(state="UserSettings.user_changes_utc"),  # Изменение часового пояса
        Window(state="UserSettings.user_error_utc"),  # Ошибка часового пояса
        Window(state="UserSettings.user_confirm_utc")  # Подтверждение часового пояса
    )

ID_SCROLL_NO_PAGER = "scroll_no_pager"  # Идентификатор для пагинации

def user_reminders_dialog() -> Dialog:
    """Диалог для управления напоминаниями пользователя."""
    return Dialog(
        Window(state="UserReminders.user_reminders_main_window"),  # Список напоминаний
        Window(state="UserReminders.user_pre_add_reminder"),  # Подготовка к добавлению
        Window(state="UserReminders.user_add_reminder"),  # Добавление напоминания
        Window(state="UserReminders.send_settings"),  # Настройки отправки
        Window(state="UserReminders.add_buttons"),  # Добавление кнопок
        Window(state="UserReminders.preview_reminders"),  # Предпросмотр напоминания
        Window(state="UserReminders.user_error_add_reminder"),  # Ошибка добавления
        Window(state="UserReminders.user_time_formats"),  # Форматы времени
        Window(state="UserReminders.user_selected_reminder"),  # Выбранное напоминание
        Window(state="UserReminders.user_edit_reminder"),  # Редактирование напоминания
        Window(state="UserReminders.user_edit_name_reminder"),  # Редактирование названия
        Window(state="UserReminders.user_edit_time_reminder"),  # Редактирование времени
        Window(state="UserReminders.user_error_edit_time_reminder"),  # Ошибка времени
        Window(state="UserReminders.user_confirm_edit_time_reminder"),  # Подтверждение времени
        Window(state="UserReminders.user_edit_period_reminder"),  # Редактирование периода
        Window(state="UserReminders.user_error_edit_period_reminder"),  # Ошибка периода
        Window(state="UserReminders.user_confirm_edit_period_reminder"),  # Подтверждение периода
        Window(state="UserReminders.user_delete_reminder"),  # Удаление напоминания
        Window(state="UserReminders.user_follow_channel")  # Проверка подписки
    )

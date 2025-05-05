from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Button, Row
from aiogram_dialog.widgets.text import Const

from tgbot.dialogs.callbacks import choice_lang, back, back_timezone, settings_confirm, to_switch_format
from tgbot.dialogs.getters import get_language, process_city, get_time_user, utc_error
from tgbot.dialogs.states import StartBot
from tgbot.middlewares.i18n.i18n_format import I18NFormat

def start_bot_dialog() -> Dialog:
    """Диалог для выбора языка и часового пояса при старте бота."""
    return Dialog(
        Window(state="StartBot.choice_language"),  # Выбор языка
        Window(state="StartBot.error_utc"),  # Ошибка часового пояса
        Window(state="StartBot.choice_utc"),  # Выбор часового пояса
        Window(state="StartBot.confirm_settings")  # Подтверждение настроек
    )

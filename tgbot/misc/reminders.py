import asyncio
import logging
import re
from datetime import datetime, timedelta

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from dateutil.relativedelta import relativedelta

from tgbot.misc import hors
from tgbot.misc.locations import get_localized_date, format_reminder_time


FORMS_TO_DIGITS = {
    # один
    'один': '1', 'одна': '1', 'одно': '1', 'одного': '1', 'одной': '1',
    'одним': '1', 'одну': '1', 'одними': '1', 'одних': '1',
    # два
    'два': '2', 'две': '2', 'двух': '2', 'двум': '2', 'двумя': '2',
    # три
    'три': '3', 'трёх': '3', 'трем': '3', 'тремя': '3', 'трижды': '3',
    # четыре
    'четыре': '4', 'четырех': '4', 'четырём': '4', 'четырьмя': '4',
    # пять
    'пять': '5', 'пяти': '5', 'пятью': '5',
    # шесть
    'шесть': '6', 'шести': '6', 'шестью': '6',
    # семь
    'семь': '7', 'семи': '7', 'семью': '7',
    # восемь
    'восемь': '8', 'восьми': '8', 'восьмью': '8',
    # девять
    'девять': '9', 'девяти': '9', 'девятью': '9',
    # десять
    'десять': '10', 'десяти': '10', 'десятью': '10'
}

pattern = re.compile(r'\b(' + '|'.join(map(re.escape, FORMS_TO_DIGITS.keys())) + r')\b', re.IGNORECASE)


def replace_words_with_digits(text: str) -> str:
    """Заменяет числительные слова на цифры в тексте."""
    pass

async def get_period(text: str) -> tuple:
    """Определяет периодичность из текста (ежедневно, еженедельно и т.д.)."""
    pass

async def get_time_from_text(text: str, tz_user: ZoneInfo, in_bool: bool,
                           every_bool: bool, user_locale: str,
                           user_timezone: str, format_time: int) -> dict:
    """Извлекает дату/время из текста с учетом локали пользователя."""
    pass

async def get_period_from_text(text: str) -> str | int | None:
    """Возвращает периодичность в формате для хранения."""
    pass

async def format_periodicity(periodicity: int | str | None, language: str) -> str:
    """Форматирует периодичность в читаемый текст."""
    pass

async def delete_message_after_delay(chat_id: int, message_id: int,
                                   delay: int, bot: Bot) -> None:
    """Удаляет сообщение через указанное время."""
    pass

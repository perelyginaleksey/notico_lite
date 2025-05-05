import json
import logging
import re
from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_dialog import DialogManager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from redis.asyncio import Redis

from infrastructure.database.models import User, Group
from infrastructure.database.repo.requests import RequestsRepo
from tgbot.config import Config
from tgbot.middlewares.i18n.i18n_format import localization_format_new as lfn, localization_format_new
from tgbot.misc.metrics import stat_add_total
from tgbot.misc.reminders import get_time_from_text, format_periodicity
from tgbot.misc.scheduler_group import add_task_to_scheduler_group

group_router = Router()


async def get_key_reminder(key, user_locale):
    """Создает клавиатуру для подтверждения напоминания."""
    pass

async def send_reply_message(user, text: str, message: Message, redis, repo):
    """Обрабатывает и отправляет сообщение с напоминанием в группе."""
    pass

async def add_rem(message: Message, dialog_manager: DialogManager, repo, **kwargs):
    """Обрабатывает команду /rem для добавления напоминания в группе."""
    pass

async def del_mess(call, user):
    """Удаляет сообщение по callback-запросу."""
    pass

async def formats_exp(call, user):
    """Показывает форматы времени для напоминаний."""
    pass

async def confirm_reminder(callback, repo, user, scheduler, influx_client, config, **kwargs):
    """Подтверждает и сохраняет напоминание в группе."""
    pass

async def cancel_reminder(callback, user, **kwargs):
    """Отменяет создание напоминания и удаляет данные из Redis."""
    pass

async def add_check(message: Message, repo, user, **kwargs):
    """Проверяет и добавляет пользователя в список админов группы."""
    pass

def start_bot_dialog() -> Dialog:
    """Диалог для начальной настройки бота (язык, часовой пояс)."""
    return Dialog(
        Window(state="StartBot.choice_language"),  # Выбор языка
        Window(state="StartBot.error_utc"),  # Ошибка часового пояса
        Window(state="StartBot.choice_utc"),  # Выбор часового пояса
        Window(state="StartBot.confirm_settings")  # Подтверждение настроек
    )


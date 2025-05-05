import time
from random import randint

from aiogram import BaseMiddleware, types, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from infrastructure.database.repo.requests import RequestsRepo


def reminder_keyboard(user_id):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text='❌Забанить', callback_data=f'ban_{user_id}'))
    return keyboard.as_markup()


class DynamicThrottlingMiddleware(BaseMiddleware):
    def __init__(self, session_pool) :
        """Вешает ограничение на пользователя при спаме"""
        pass
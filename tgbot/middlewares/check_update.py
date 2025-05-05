import logging

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Message, CallbackQuery, ChatMemberAdministrator, ChatMemberOwner, Update
from tgbot.middlewares.i18n.i18n_format import localization_format_new as lfn


class CheckUpdateMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict) -> any:
        """Проверяет права доступа для сообщений и callback-запросов в группах."""
        pass
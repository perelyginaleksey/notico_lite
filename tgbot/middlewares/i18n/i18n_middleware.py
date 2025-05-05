from collections.abc import Awaitable, Callable
from typing import Any, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from fluent.runtime import FluentLocalization

from tgbot.middlewares.i18n.i18n_shared import I18N_FORMAT_KEY


class I18nMiddleware(BaseMiddleware):
    def __init__(
            self,
            l10ns: dict[str, FluentLocalization],
            default_lang: str,
    ):
        super().__init__()
        self.l10ns = l10ns
        self.default_lang = default_lang

    async def __call__(
            self,
            handler: Callable[
                [Union[Message, CallbackQuery], dict[str, Any]],
                Awaitable[Any],
            ],
            event: Union[Message, CallbackQuery],
            data: dict[str, Any],
    ) -> Any:
        event_from_user = data.get("event_from_user")
        user = data.get("user")
        if user and user.language:
            lang = user.language
        else:
            lang = event_from_user.language_code if event_from_user.language_code in ["en", "ru"] else self.default_lang

        if lang not in self.l10ns:
            lang = self.default_lang

        l10n = self.l10ns[lang]
        data[I18N_FORMAT_KEY] = l10n.format_value

        data["i18n"] = self

        return await handler(event, data)

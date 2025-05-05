from typing import Any, Protocol

from aiogram_dialog.api.protocols import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text
from tgbot.middlewares.i18n.i18n_shared import I18N_FORMAT_KEY
from tgbot.middlewares.i18n.i18n import make_i18n_middleware


i18n = make_i18n_middleware()


class Values(Protocol):
    def __getitem__(self, item: Any) -> Any:
        raise NotImplementedError


def default_format_text(text: str, data: Values) -> str:
    return text.format_map(data)


class I18NFormat(Text):
    def __init__(self, text: str, when: WhenCondition = None):
        super().__init__(when)
        self.text = text

    async def _render_text(self, data: dict, manager: DialogManager) -> str:
        format_text = manager.middleware_data.get(
            I18N_FORMAT_KEY, default_format_text,
        )
        return format_text(self.text, data)


def localization_format(text: str, manager: DialogManager, data: dict = None) -> str:
    format_text = manager.middleware_data.get(
        I18N_FORMAT_KEY, default_format_text,
    )
    return format_text(text, data)


def localization_format_new(text: str, locale: str, data: dict = None) -> str:
    locale = locale if locale else 'ru'
    translation = i18n.l10ns[locale].format_value(text, data)
    return translation


from fluent.runtime import FluentResourceLoader, FluentLocalization

from tgbot.middlewares.i18n.i18n_middleware import I18nMiddleware

DEFAULT_LOCALE = "en"
LOCALES = ["en", "ru"]


def make_i18n_middleware():
    loader = FluentResourceLoader(r"/usr/src/app/bot/tgbot/translations/{locale}")
    l10ns = {
        locale: FluentLocalization(
            [locale, DEFAULT_LOCALE], ["main.ftl"], loader,
        )
        for locale in LOCALES
    }
    return I18nMiddleware(l10ns, DEFAULT_LOCALE)

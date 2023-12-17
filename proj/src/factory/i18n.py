from logging import Logger, getLogger
from typing import Final

from aiogram import Dispatcher
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore


LOCALES_PATH: Final[str] = "locales"

logger: Final[Logger] = getLogger(name=__name__)


def setup_i18n(*, dispatcher: Dispatcher) -> None:
    logger.info("Setup i18n")
    core = FluentRuntimeCore(path=LOCALES_PATH)
    middleware = I18nMiddleware(core=core, default_locale="ru")
    middleware.setup(dispatcher=dispatcher)

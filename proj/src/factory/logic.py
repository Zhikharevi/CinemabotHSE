from logging import Logger, getLogger
from typing import Final

from aiogram import Dispatcher

from src.handlers import router as handlers_router


logger: Final[Logger] = getLogger(name=__name__)


def setup_logic(*, dispatcher: Dispatcher) -> None:
    logger.info("Setup logic")
    dispatcher.include_router(handlers_router)

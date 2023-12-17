from logging import Logger, getLogger
from typing import Final

from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseStorage


logger: Final[Logger] = getLogger(name=__name__)


def create_dispatcher(*, storage: BaseStorage) -> Dispatcher:
    logger.info("Create dispatcher instance")
    return Dispatcher(storage=storage, name="root")

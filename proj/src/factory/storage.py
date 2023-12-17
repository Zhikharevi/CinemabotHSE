from logging import Logger, getLogger
from typing import Final

from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage


logger: Final[Logger] = getLogger(name=__name__)


def create_storage() -> BaseStorage:
    logger.info("Create memory storage")
    return MemoryStorage()

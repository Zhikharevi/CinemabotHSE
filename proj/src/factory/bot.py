from logging import Logger, getLogger
from typing import Final

from aiogram import Bot
from aiogram.enums import ParseMode

from src.config import Config


logger: Final[Logger] = getLogger(name=__name__)


def create_bot(*, config: Config) -> Bot:
    logger.info("Create bot instance")
    return Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)

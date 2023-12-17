from logging import Logger, getLogger
from typing import Final

from src.factory import Factory


logger: Final[Logger] = getLogger(name=__name__)


def executor(*, factory: Factory) -> None:
    logger.info("Execute bot")
    factory.dispatcher.run_polling(factory.bot)

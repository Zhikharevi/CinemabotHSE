from logging import Logger, getLogger
from typing import Final

from src.config import Config
from src.utils.search_engine import AsyncSearchEngine


logger: Final[Logger] = getLogger(name=__name__)


def create_search_engine(*, config: Config) -> AsyncSearchEngine:
    logger.info("Create search engine")

    return AsyncSearchEngine(token=config.kinopoisk_token.get_secret_value())

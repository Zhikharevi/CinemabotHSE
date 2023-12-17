from logging import Logger, getLogger
from typing import Final, NamedTuple

from aiogram import Bot, Dispatcher

from src.config import Config

from .bot import create_bot
from .dispatcher import create_dispatcher
from .i18n import setup_i18n
from .logic import setup_logic
from .search import create_search_engine
from .storage import create_storage


logger: Final[Logger] = getLogger(name=__name__)


class Factory(NamedTuple):
    bot: Bot
    dispatcher: Dispatcher


def setup_factory(*, config: Config) -> Factory:
    logger.info("Setup factory")

    bot = create_bot(config=config)
    storage = create_storage()
    dispatcher = create_dispatcher(storage=storage)
    search = create_search_engine(config=config)

    setup_i18n(dispatcher=dispatcher)
    setup_logic(dispatcher=dispatcher)

    dispatcher.workflow_data.update(
        search=search,
    )

    return Factory(bot=bot, dispatcher=dispatcher)

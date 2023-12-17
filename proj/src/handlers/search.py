from typing import TYPE_CHECKING, Any, Final

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.methods import TelegramMethod
from aiogram.types import Message
from aiogram_i18n import I18nContext

from src.utils.search_engine import AsyncSearchEngine


if TYPE_CHECKING:
    from locales.stubs import I18nContext  # noqa: F811,TCH004


router: Final[Router] = Router(name=__name__)


@router.message(Command("s", "search"))
async def command_search(
    message: Message,
    command: CommandObject,
    i18n: I18nContext,
    search: AsyncSearchEngine,
) -> TelegramMethod[Any]:
    if not command.args:
        return message.answer(text=i18n.search.command_wrong_use(), parse_mode=None)

    if result := await search.search(query=command.args):
        return message.answer(
            text=i18n.search.info(
                name=result["name"],
                en_name=result["alternativeName"],
                rating=result["rating"],
                genres=", ".join(result["genres"]),
                year=result["year"],
                country=result["countries"][0],
                short_escription=result["shortDescription"] or "Нет.",
                link=f"https://www.kinopoisk.ru/film/{result['id']}/",
            ),
            disable_web_page_preview=False,
        )

    return message.answer(text=i18n.search.not_found())

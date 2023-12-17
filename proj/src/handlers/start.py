from typing import TYPE_CHECKING, Any, Final

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.methods import TelegramMethod
from aiogram.types import Message
from aiogram_i18n import I18nContext


if TYPE_CHECKING:
    from locales.stubs import I18nContext  # noqa: F811,TCH004


router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
async def command_start(
    message: Message,
    i18n: I18nContext,
) -> TelegramMethod[Any]:
    return message.answer(text=i18n.start.message(), parse_mode=None)

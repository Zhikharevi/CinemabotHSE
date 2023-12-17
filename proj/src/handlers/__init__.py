from typing import Final

from aiogram import Router

from .search import router as search_router
from .start import router as start_router


router: Final[Router] = Router(name=__name__)

router.include_routers(
    start_router,
    search_router,
)

from contextlib import contextmanager
from typing import Any, Generator, Union

from aiogram_i18n import LazyProxy


class Search:
   def command_wrong_use(self) -> Union[str, LazyProxy]: ...
   def not_found(self) -> Union[str, LazyProxy]: ...
   def info(self, *, name: Any, en_name: Any, rating: Any, genres: Any, year: Any, country: Any, short_escription: Any, link: Any) -> Union[str, LazyProxy]: ...

class Start:
   def message(self) -> Union[str, LazyProxy]: ...

class I18nStubs:
    start = Start()
    search = Search()

class I18nContext(I18nStubs):
    def get(self, key: str, /, **kwargs: Any) -> str: ...
    async def set_locale(self, locale: str, **kwargs: Any) -> None: ...
    @contextmanager
    def use_locale(self, locale: str) -> Generator[I18nContext, None, None]: ...

class LazyFactory(I18nStubs):
    key_separator: str
    def set_separator(self, key_separator: str) -> None: ...
    def __call__(self, key: str, /, **kwargs: dict[str, Any]) -> LazyProxy: ...

L: LazyFactory

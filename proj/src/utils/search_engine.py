from typing import Any, Optional

from aiohttp import ClientSession


class AsyncSearchEngine:
    BASE_URL = "https://api.kinopoisk.dev/v1.2/movie/search"

    def __init__(self, token: str) -> None:
        self._headers = {"X-API-KEY": token}
        self._params: dict[str, str | int] = {
            "limit": 1,
            "page": 1,
        }

    async def search(self, query: str) -> Optional[dict]:
        params = self._params.copy()
        params["query"] = query

        async with ClientSession() as session:
            async with session.get(
                url=self.BASE_URL,
                headers=self._headers,
                params=params,
            ) as response:
                result = await response.json()

        if not result.get("docs"):
            return None

        return result["docs"][0]

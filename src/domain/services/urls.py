from hashlib import md5
from typing import Any
from src.domain.repository import UrlRepo
from src.domain.services import BaseService


class UrlLookup(BaseService):

    def __init__(self, url_repo: UrlRepo) -> None:
        self.repo = url_repo
        super().__init__()

    async def __call__(self, url_hash: str) -> Any:
        result = await self.repo.get(url_hash=url_hash)
        return result.url if result else None


class UrlStore(BaseService):

    def __init__(self, url_repo: UrlRepo) -> None:
        self.repo = url_repo
        super().__init__()

    async def __call__(self, url: str) -> Any:
        url_hash = md5(url.encode("utf-8")).hexdigest()
        await self.repo.insert(url_hash=url_hash, url=url)
        return url_hash

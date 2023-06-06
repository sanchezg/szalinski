import secrets
from typing import Any

from src.domain.repository import UrlCacheRepo, UrlRepo
from src.domain.services import BaseService


class UrlLookup(BaseService):
    def __init__(self, url_repo: UrlRepo, cache_repo: UrlCacheRepo) -> None:
        self.repo = url_repo
        self.cache = cache_repo
        super().__init__()

    async def __call__(self, url_hash: str) -> Any:
        in_cache = await self.cache.get(url_hash)
        if in_cache:
            return in_cache.decode("utf-8")
        result = await self.repo.get(url_hash=url_hash)
        if result:
            await self.cache.set(key=url_hash, value=result.url)
            return result.url
        return None


class UrlStore(BaseService):
    def __init__(self, url_repo: UrlRepo, cache_repo: UrlCacheRepo) -> None:
        self.repo = url_repo
        self.cache = cache_repo
        super().__init__()

    async def __call__(self, url: str) -> Any:
        url_hash = secrets.token_urlsafe(8)
        in_cache = await self.cache.get(url_hash)
        if not in_cache:
            await self.repo.insert(url_hash=url_hash, url=url)
            await self.cache.set(key=url_hash, value=url)
        return url_hash

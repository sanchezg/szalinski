from typing import Any, Optional

import redis.asyncio as aioredis

from src.domain import interfaces


class RedisRepo(interfaces.AbstractRepo):
    def __init__(self, client: aioredis.Redis):
        self.client = client

    async def get(self, key: str) -> Optional[Any]:
        return await self.client.get(key)

    async def set(self, key: str, value: str) -> None:
        await self.client.set(key, value)

    async def insert(self, **kwargs) -> None:
        await self.set(key=kwargs.get("key"), value=kwargs.get("value"))

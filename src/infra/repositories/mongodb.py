from typing import Any, Optional

from src import settings
from src.domain.interfaces import AbstractRepo


class MongoDBRepo(AbstractRepo):
    def __init__(self, client) -> None:
        self.db = client[settings.MONGODB_NAME]
        super().__init__()

    async def get(self, **kwargs) -> Optional[Any]:
        filters = {}
        for k, v in kwargs.items():
            filters[k] = {"$eq": v}  # TODO: Improve filter mapping
        document = await self.db[settings.MONGODB_COLLECTION].find_one(filters)
        return document

    async def insert(self, **kwargs) -> None:
        document = await self.db[settings.MONGODB_COLLECTION].insert_one(kwargs)
        return document

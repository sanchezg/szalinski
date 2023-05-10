from typing import Any, Optional

from src.domain.interfaces import AbstractRepo
from src.settings import MONGODB_NAME


class MongoDBRepo(AbstractRepo):
    def __init__(self, client) -> None:
        self.db = client[MONGODB_NAME]
        super().__init__()

    async def get(self, **kwargs) -> Optional[Any]:
        filters = {}
        for k, v in kwargs.items():
            filters[k] = {"$eq": v}  # TODO: Improve filter mapping
        document = await self.db.collection.find_one(filters)
        return document

    async def insert(self, **kwargs) -> None:
        document = await self.db.collection.insert_one(kwargs)
        return document

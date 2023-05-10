import dataclasses
from typing import Optional

from src.domain.model import URL
from src.domain.repository import UrlRepo
from src.infra.repositories.mongodb import MongoDBRepo


class MongoDBUrlRepo(MongoDBRepo, UrlRepo):

    entity = URL

    async def get(self, **kwargs) -> Optional[URL]:
        # TODO: use some object-mapper lib for this
        doc = await super().get(**kwargs)
        if doc:
            return URL(
                **{field.name: doc[field.name] for field in dataclasses.fields(URL)}
            )
        return None

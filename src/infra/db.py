from abc import ABC, abstractmethod
from typing import Any, Optional

import motor.motor_asyncio as mongodb
import redis.asyncio as redis


class AbstractGateway(ABC):
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        pass

    @abstractmethod
    def set(self, key: str, value: str) -> None:
        pass


class MongoDBGateway(AbstractGateway):
    def __init__(self, host, port) -> None:
        self.client = mongodb.AsyncIOMotorClient(
            host, port, username="root", password="toor2023"
        )
        super().__init__()

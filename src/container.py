import redis.asyncio as aioredis
from dependency_injector import containers, providers
from motor.motor_asyncio import AsyncIOMotorClient

from src import settings
from src.domain.services.urls import UrlLookup, UrlStore
from src.infra.repositories.redis import RedisRepo
from src.infra.repositories.urls import MongoDBUrlRepo


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".application.controllers"])

    # DB clients
    mongodb_client = providers.Factory(
        AsyncIOMotorClient,
        settings.MONGODB_HOST,
        settings.MONGODB_PORT,
        username=settings.MONGODB_USER,
        password=settings.MONGODB_PASS,
        authSource="admin",
    )

    redis_client = providers.Factory(
        aioredis.Redis,
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
    )

    # Repositories
    url_repo = providers.Factory(MongoDBUrlRepo, mongodb_client)
    cache_repo = providers.Factory(RedisRepo, redis_client)

    # Services
    url_lookup = providers.Factory(UrlLookup, url_repo=url_repo, cache_repo=cache_repo)
    url_store = providers.Factory(UrlStore, url_repo=url_repo, cache_repo=cache_repo)

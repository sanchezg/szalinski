from motor.motor_asyncio import AsyncIOMotorClient

from dependency_injector import containers, providers
from src.domain.services.urls import UrlLookup, UrlStore

from src import settings
from src.infra.repositories.urls import MongoDBUrlRepo


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".application.controllers"])

    mongodb_client = providers.Factory(
        AsyncIOMotorClient, settings.MONGODB_HOST, settings.MONGODB_PORT, username="root", password="toor2023", authSource="admin"
    )

    # Repositories
    url_repo = providers.Factory(MongoDBUrlRepo, mongodb_client)

    # Services
    url_lookup = providers.Factory(UrlLookup, url_repo=url_repo)
    url_store = providers.Factory(UrlStore, url_repo=url_repo)

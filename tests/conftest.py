import pytest
from dependency_injector import containers, providers
from fastapi.testclient import TestClient

from src.domain.services.urls import UrlLookup, UrlStore
from src.main import create_app
from tests.fakes import FakeCache, FakeRepo


class TestContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["src.application.controllers"])

    # Repositories
    url_repo = providers.Factory(FakeRepo)
    cache_repo = providers.Factory(FakeCache)

    # Services
    url_lookup = providers.Factory(UrlLookup, url_repo=url_repo, cache_repo=cache_repo)
    url_store = providers.Factory(UrlStore, url_repo=url_repo, cache_repo=cache_repo)


@pytest.fixture
def app():
    app = create_app()
    app.container = TestContainer()
    return app


@pytest.fixture
def client(app):
    client = TestClient(app=app)
    return client

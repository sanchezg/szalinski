import pytest

from src.domain.services.urls import UrlLookup, UrlStore
from tests.fakes import FakeCache, FakeRepo


@pytest.mark.asyncio
async def test_urllookup_return_url_if_exists():
    FAKE_URL_HASH = "1234testhash"
    FAKE_URL = "http://some.long.url/"
    fake_repo = FakeRepo()
    await fake_repo.insert(url=FAKE_URL, url_hash=FAKE_URL_HASH)

    service = UrlLookup(url_repo=fake_repo, cache_repo=FakeCache())
    result = await service(FAKE_URL_HASH)
    assert result == FAKE_URL


@pytest.mark.asyncio
async def test_urllookup_return_None_if_not_exists():
    fake_repo = FakeRepo()  # empty data
    fake_cache = FakeCache()
    service = UrlLookup(url_repo=fake_repo, cache_repo=fake_cache)
    result = await service("some1234hash")
    assert result is None


@pytest.mark.asyncio
async def test_urlstore_returns_hash():
    service = UrlStore(url_repo=FakeRepo(), cache_repo=FakeCache())
    result = await service(url="http://some.long.url/")
    assert result
    assert isinstance(result, str)

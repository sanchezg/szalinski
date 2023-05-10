from src.domain.interfaces import AbstractRepo
from src.domain.model import URL


class FakeRepo(AbstractRepo):
    def __init__(self) -> None:
        self._data = {}
        super().__init__()

    async def get(self, url_hash):
        return self._data.get(url_hash)

    async def insert(self, url_hash, url):
        self._data[url_hash] = URL(url_hash=url_hash, url=url)
        return url_hash

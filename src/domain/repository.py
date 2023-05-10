import abc

from src.domain.interfaces import AbstractRepo
from src.domain.model import URL


class UrlRepo(AbstractRepo[URL], metaclass=abc.ABCMeta):
    pass


class UrlCacheRepo(AbstractRepo):
    pass

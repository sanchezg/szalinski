import abc

from src.domain.model import URL
from src.domain.interfaces import AbstractRepo


class UrlRepo(AbstractRepo[URL], metaclass=abc.ABCMeta):
    pass

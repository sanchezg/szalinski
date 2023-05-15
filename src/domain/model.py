from dataclasses import dataclass
from typing import Union


@dataclass()
class URL:
    url: str
    url_hash: Union[str, None] = None

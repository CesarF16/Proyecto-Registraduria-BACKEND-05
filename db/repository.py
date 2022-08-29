from typing import TypeVar, Generic, get_args
from db.db import Db

T = TypeVar('T')

class Repository(Generic[T]):
    def __init__(self) -> None:
        self.name = get_args(self.__orig_bases__[0].__name__.lower().replace('model',''))
        self.db = Db()
        self.collection = self.db.collection(self.name)
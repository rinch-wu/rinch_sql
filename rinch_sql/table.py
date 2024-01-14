from functools import cache

from .mysql import Mysql
from .db_config import DbConfig


class Table:
    db_config: DbConfig = None
    field_list_unique: list[str]

    @classmethod
    @cache
    def db(cls, db_config: DbConfig = None):
        db_config = db_config or cls.db_config
        db = Mysql(cls, db_config)
        return db

    def __hash__(self):
        return hash(self.__tuple__())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__tuple__() == other.__tuple__()
        else:
            return False

    def __iter__(self) -> iter:
        for i in self.field_list_unique:
            value = self.__dict__[i]
            yield value

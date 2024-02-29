from functools import cache

from .db_config import DbConfig
from .mysql import Mysql


class Table:
    db_config: DbConfig = None
    field_list_unique: list[str]

    @classmethod
    @cache
    def db(cls, db_config: DbConfig = None) -> Mysql:
        db_config = db_config or cls.db_config
        db = Mysql(cls, db_config)
        return db

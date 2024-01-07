from dataclasses import dataclass, field, replace
from mysql.connector.pooling import MySQLConnectionPool
from functools import cache


@dataclass(frozen=True)
class DbConfig:
    host: str
    port: int
    user: str
    password: str
    pool_size: int = 1
    database: str = None
    autocommit: bool = field(init=False, default=True)
    # autocommit: bool = True  # 强制行为

    @cache
    def pool(self) -> MySQLConnectionPool:
        return MySQLConnectionPool(**self.__dict__)

    def replace(self, /, **changes):
        return replace(self, changes)

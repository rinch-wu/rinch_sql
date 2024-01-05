from .mysql import Mysql


class Table:
    @classmethod
    @staticmethod
    def db(cls, db_config=None):
        if not db_config:
            db_config = cls.db_config

        db = Mysql(db_config, cls)
        return db

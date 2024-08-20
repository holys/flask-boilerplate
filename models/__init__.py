from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(
    engine_options={"pool_pre_ping": True, "pool_size": 20, "max_overflow": 5},
    session_options={"autoflush": False},
)


@contextmanager
def db_transaction():
    """
    用法： 大多数情况下，应该使用装饰器的用法

    e.g.
    @db_transaction()
    def some_data_operation():
        do_sth()


    如果是在函数内部使用（比如 handler 内简单的数据操作，用不上装饰器时），可以用 with 语法
    e.g.
    def some_data_operation():
        with db_transaction() as session:
            do_sth()
    无需 commit 和 rollback，会自动处理
    """
    session = db.session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def insert_records(records):
    session = db.session()
    for record in records:
        session.add(record)
    session.flush()
    return [record.id for record in records]


def insert_record(record):
    return insert_records([record])[0]

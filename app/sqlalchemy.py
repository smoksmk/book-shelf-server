from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import URL


engine = create_engine(URL)

Base = declarative_base()
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def db_connect(func):
    def inner(*args, **kwargs):
        session = Session()  # with all the requirements
        try:
            func(*args, session=session, **kwargs)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    return inner

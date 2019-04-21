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


def db_session(func):
    def inner(*args, **kwargs):
        session = Session()  # (this is now a scoped session)
        try:
            func(*args, **kwargs) # No need to pass session explicitly
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.remove()  # NOTE: *remove* rather than *close* here
    return inner

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from config import Config


def start() -> scoped_session:
    engine = create_engine(Config.postgres://zqpdoezkhnmmou:46dc728a66122a24cefa29bcaebd629bd8eefbe7bf88438633b5901cdcaf7bea@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d4tbnimsjio5kf)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

import logging

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, registry

from config import DB_URL

# Create database
mapper_registry = registry()
engine = create_engine(DB_URL)  # echo=True
logger = logging.getLogger(__name__)


@mapper_registry.mapped
class User:
    __tablename__ = 'users'

    chat_id = Column(Integer, primary_key=True)
    login = Column(String(255))
    pswd = Column(String(255))

    def __init__(self, chat_id, login, pswd):
        self.chat_id = chat_id
        self.login = login
        self.pswd = pswd

    def __repr__(self):
        return f'<id={self.chat_id}, login={self.login}, pswd={self.pswd}>'


async def create_database():
    # mapper_registry.generate_base().metadata.drop_all(bind=engine)
    mapper_registry.generate_base().metadata.create_all(bind=engine)
    logger.info('database created')


async def get_session():
    session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False,
                                          bind=engine))
    return session()


# asyncio.get_event_loop().run_until_complete(create_database())

# TODO make base abstract repository
import abc

from models import db


class AbstractRepository(abc.ABC):

    def __init__(self):
        """
        Initialise the adaptor with a session
        """
        self.session = db.get_session()

    @abc.abstractmethod
    def get_by_id(self, entity_id):
        """
        Get the entity by id
        :param entity_id: int|str
        :return: entity
        """
        raise NotImplementedError


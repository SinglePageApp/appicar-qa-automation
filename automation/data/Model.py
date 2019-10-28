from abc import ABC, abstractmethod
from automation.data import db


class Model(ABC):
    """
    Responsible for managing the data of the application.
    """
    def __init__(self, name, *fields, **args):
        """
        Constructor.

        :param name: The model's name. It has to be the same for the table or collection
                     defined in the DB.
        :type name: str
        :param fields: The fields to be mapped with the DB.
        :type fields: automation.data.Field
        """
        self.query = db
        self.model = db.define_table(name, *fields, **args)
        self.native = db._adapter.connection[name]

    @staticmethod
    @abstractmethod
    def find_all():
        """
        Finds all the elements in the collection.

        :returns: A set of elements.
        :rtype: pydal.objects.Set
        """
        pass

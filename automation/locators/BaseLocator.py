from abc import ABC, abstractmethod


class BaseLocator(ABC):
    @abstractmethod
    def get_id(self):
        """
        Gets the locator's ID.

        :returns: The locator's ID.
        :rtype: int
        """
        pass

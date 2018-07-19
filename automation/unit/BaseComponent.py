from abc import ABC, abstractmethod


class BaseComponent(ABC):
    """
    Base class for all page components.
    """
    def __init__(self, browser):
        self.browser = browser

    @abstractmethod
    def get_id(self):
        """
        Gets component's ID.

        :returns: The component's ID.
        :rtype: int
        """
        pass

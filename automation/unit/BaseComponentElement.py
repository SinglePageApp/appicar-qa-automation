from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait


class BaseComponentElement(ABC):
    """
    Base class for all component's elements.
    """
    def __get__(self, obj, owner):
        """
        Gets the value of the specified object.

        :param obj: The object from where to get the value.
        :param owner: The object's owner.
        :returns: The object's current value.
        """
        browser = obj.browser
        WebDriverWait(browser, 100).until(
            lambda browser: browser.find_element_by_name(self.locator)
        )
        element = browser.find_element_by_name(self.locator)

        return element.get_attribute("value")

    def __set__(self, obj, value):
        """
        Sets the value of the specified object.
        
        :param obj: The object to be assigned.
        :param value: The value to be set.
        """
        browser = obj.browser
        WebDriverWait(browser, 100).until(
            lambda browser: browser.find_element_by_name(self.locator)
        )
        browser.find_element_by_name(self.locator).clear()
        browser.find_element_by_name(self.locator).send_keys(value)
    
    @abstractmethod
    def get_id(self):
        """
        Gets the element's ID.

        :returns: The elements's ID.
        :rtype: int
        """
        pass
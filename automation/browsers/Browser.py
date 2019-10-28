from abc import ABC, abstractmethod
from configparser import ConfigParser
from selenium import webdriver
from automation import browsers


class Browser(ABC):
    NAME = None
    """
    Represents the current browser to run the tests on.
    """
    @staticmethod
    def get_session(name):
        """
        Initialize a session in the given browser.

        :param name: The name of the browser.
        :type name: str
        :returns: The initialized session on the browser.
        :rtype: selenium.webdriver.firefox.webdriver.WebDriver
        """
        return eval('browsers.' + name + '()')

    def get_options(self):
        """
        Gets the browsers's options.

        :returns: Google Chrome browsers's options.
        :rtype: selenium.webdriver.ChromeOptions
        """
        # Read browser options from the config file.
        config = ConfigParser()
        config.read('automation/browsers/config.ini')
        browser_options = eval('webdriver.' + self.NAME + 'Options()')
        # Add only activated options.
        for option, activated in config.items(self.NAME):
            if activated == 'yes':
                browser_options.add_argument('--' + option)

        return browser_options

    @abstractmethod
    def get_name(self):
        pass

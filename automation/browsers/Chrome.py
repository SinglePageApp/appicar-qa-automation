from selenium import webdriver
from automation.browsers import Browser


class Chrome(webdriver.Chrome, Browser):
    """
    Represents a Google Chrome browser.
    """
    NAME = 'Chrome'
    PATH = '/usr/local/bin/chromedriver'
    LOG_PATH = 'results/logs/chrome.log'

    def __init__(self):
        """
        Initialize a session in Google Chrome browser.

        :returns: The initialized session on the browser.
        :rtype: selenium.webdriver.chrome.webdriver.WebDriver
        """
        super(Chrome, self).__init__(
            executable_path=self.PATH,
            service_log_path=self.LOG_PATH,
            options=self.get_options()
        )

    def get_name(self):
        return self.NAME

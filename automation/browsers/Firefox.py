from selenium import webdriver
from automation.browsers import Browser


class Firefox(webdriver.Firefox, Browser):
    """
    Represents a Mozilla Firefox browser.
    """
    NAME = 'Firefox'
    LOG_PATH = 'results/logs/firefox.log'

    def __init__(self):
        """
        Initialize a session in Google Firefox browser.

        :returns: The initialized session on the browser.
        :rtype: selenium.webdriver.chrome.webdriver.WebDriver
        """
        super(Firefox, self).__init__(
            log_path=self.LOG_PATH,
            firefox_options=self.get_options()
        )

    def get_name(self):
        return self.NAME

import sys
import unittest
import allure
import json
from abc import ABC, abstractmethod
from automation.browsers import Browser


class BaseTestSuite(ABC, unittest.TestCase):
    """
    Base test suite. All test suites must inherite from this class.
    """
    def __init__(self, methodName='runTest', browser_name='Firefox'):
        """
        Constructor.

        :param methodName: The name of the method which will be run.
        :param param: The name of the target browser.
        """
        super(BaseTestSuite, self).__init__(methodName)
        self.browser_name = browser_name

    @allure.step('Launch app.')
    def setUp(self):
        """
        Initial configuration for the test.
        """
        # Load configurations.
        config = json.loads(open('config.json').read())
        self.browser_name = sys.argv[-1].replace('--browser=', '')
        # Create a new Browser session.
        self.browser = Browser.get_session(self.browser_name)
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()
        # Navigate to the application home page.
        self.browser.get(config['RUN']['target'])
        print('Running test on ' + self.browser_name + ' browser.')

    @allure.step('Close app.')
    def tearDown(self):
        """
        Execute this code when the test is finished.
        """
        # Save the screenshot.
        self.browser.save_screenshot(
            'results/screenshots/' + self.browser_name.lower() + '.png'
        )
        # Close the browsers window.
        self.browser.quit()

    @abstractmethod
    def get_id(self):
        """
        Gets the test suite's ID.

        :returns: The test suite's ID.
        :rtype: int
        """
        pass

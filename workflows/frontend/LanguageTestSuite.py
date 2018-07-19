import allure
from automation.unit import BaseTestSuite


@allure.story("Language Test Suite")
class LanguageTestSuite(BaseTestSuite):
    """
    SearchBox test suite.
    """
    ID = 'searchbox_tests'

    @allure.testcase("Search by food")
    def test_english(self):
        """
        This tests changes the app's language to english.
        """
        print("English test")

    def get_id(self):
        """
        Gets component's ID.

        :returns: The component's ID.
        :rtype: int
        """
        return self.ID

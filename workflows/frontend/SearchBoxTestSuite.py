import allure
from automation.unit import BaseTestSuite
from workflows.frontend.components import SearchBoxComponent


@allure.story('SearchBox Test Suite')
@allure.issue('APQA-10')
@allure.severity(allure.severity_level.CRITICAL)
class SearchBoxTestSuite(BaseTestSuite):
    """
    SearchBox test suite.
    """
    ID = 'searchbox_tests'

    @allure.testcase("Search by food")
    def test_search_by_food(self):
        """
        This test makes a search base on food criteria.
        """
        self.searchbox = SearchBoxComponent(self.browser)
        self.searchbox.fill_search_input()
        self.searchbox.click_search_button()
        self.searchbox.check_displayed_stores()

    def get_id(self):
        """
        Gets component's ID.

        :returns: The component's ID.
        :rtype: int
        """
        return self.ID

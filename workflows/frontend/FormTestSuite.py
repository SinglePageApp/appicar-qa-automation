import allure
from automation.unit import BaseTestSuite
from workflows.frontend.components import FormComponent


@allure.story("Form Test Suite")
class FormTestSuite(BaseTestSuite):
    """
    SearchBox test suite.
    """
    ID = 'form_tests'

    @allure.testcase("Tests the form")
    def test_form_tree(self):
        """
        This test makes a search based on food criteria.
        """
        self.form = FormComponent(self.browser)
        self.form.find_xpaths()

    def get_id(self):
        """
        Gets component's ID.

        :returns: The component's ID.
        :rtype: int
        """
        return self.ID

    def runTest(self):
        self.test_search_by_food()
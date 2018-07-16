from automation.unit import BaseTestSuite


class SearchBoxTestSuite(BaseTestSuite):
    """
    SearchBox test suite.
    """
    ID = 'searchbox_tests'

    def test_search_by_food(self):
        """
        This test makes a search base on food criteria.
        """
        # Get the search textbox.
        search_field = self.browser.find_element_by_id('menuItemCategory')
        search_field.clear()
        # Enter search keyword and submit.
        search_field.send_keys('pizza')
        # Locate the search button and click it.
        search_button = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-home-page/app-home-header/div/div/div/div[2]/app-searchbox/div/div/span[2]/button[2]'
        )
        search_button.click()
        # get all the anchor elements which have store names displayed
        # currently on result page using find_elements_by_xpath method
        stores = self.browser.find_elements_by_class_name('w3l-home-stores-grid')
        # get the number of anchor elements found
        print('\n\nFound ' + str(len(stores)) + ' stores:')
        # iterate through each anchor element and print the text that is # name of the store
        for store in stores:
            print('---------------------------------------------------------')
            print(store.text)
        print('---------------------------------------------------------')

    def get_id(self):
        return self.ID

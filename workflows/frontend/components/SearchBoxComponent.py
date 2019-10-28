import allure
from automation.unit import BaseComponent


class SearchBoxComponent(BaseComponent):
    """
    Represents the SearchBox component.
    """
    ID = 'searchbox'

    @allure.step('Fill the search input.')
    def fill_search_input(self):
        # Get the search textbox.
        search_field = self.browser.find_element_by_id('menuItemCategory')
        search_field.clear()
        # Enter search keyword and submit.
        search_field.send_keys('pizza')

    @allure.step('Click "Go!" button.')
    def click_search_button(self):
        # Locate the search button and click it.
        search_button = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-home-page/app-home-header/div/div/div/div[2]/app-searchbox/div/div/span[2]/button[2]'
        )
        search_button.click()

    @allure.step('Check displayed stores.')
    def check_displayed_stores(self):
        # Get all the store boxes displayed in the search results.
        stores = self.browser.find_elements_by_class_name('w3l-home-stores-grid')
        # Show the number of found stores.
        print('\n\nFound ' + str(len(stores)) + ' stores:')
        # Iterate through each store box and print the content inside it.
        for store in stores:
            print('---------------------------------------------------------')
            print(store.text)
        print('---------------------------------------------------------')

    def get_id(self):
        """
        Gets component's ID.

        :returns: The component's ID.
        :rtype: int
        """
        return self.ID

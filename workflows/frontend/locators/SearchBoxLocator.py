from automation.locators import BaseLocator, By


class SearchBoxLocator(BaseLocator):
    """
    SearchBox's elements locator.
    """
    GO_BUTTON = (By.ID, 'search-go')
    RESET_BUTTON = (By.ID, 'search-reset')

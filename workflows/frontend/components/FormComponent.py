import allure
import urllib
from lxml import etree
from pprint import pprint
from bs4 import BeautifulSoup
from automation.unit import BaseComponent


class FormComponent(BaseComponent):
    """
    Represents the SearchBox component.
    """
    ID = 'searchbox'

    @allure.step('Fill the search input.')
    def find_xpaths(self):
        with urllib.request.urlopen(self.browser.current_url) as response:
            parser = etree.HTMLParser()
            tree = etree.fromstring(response.read().decode('utf-8'), parser)

            for element in tree.iter():
                pprint(self.__guess_xpath(element))

    def get_id(self):
        """
        Gets component's ID.

        :returns: The component's ID.
        :rtype: int
        """
        return self.ID

    def __guess_xpath(self, element):
        """
        Guess the xpath
        """
        xpaths = []
        # Class attribute returned as a unicodeded list, so removing 'u from the list and joining
        for key, value in element.attrib.iteritems():
            # attr[key] = [i.encode('utf-8') for i in attr[key]]
            xpaths.append("//{}[@{}='{}']".format(element.tag, key, value))

        return xpaths



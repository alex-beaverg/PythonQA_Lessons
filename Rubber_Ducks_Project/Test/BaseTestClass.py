import unittest
from Rubber_Ducks_Project.Helpers.Webdriver import Webdriver


class BaseTestClass(unittest.TestCase):
    """Base test class"""

    def setUp(self) -> None:
        """Setup method before every test"""
        self.driver = Webdriver().webdriver_setup()
        self.pageSetUp()

    def pageSetUp(self) -> None:
        """Page set up method"""
        self.page_url = 'http://litecart.stqa.ru/en/'
        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        """Teardown method after every test"""
        self.driver.quit()

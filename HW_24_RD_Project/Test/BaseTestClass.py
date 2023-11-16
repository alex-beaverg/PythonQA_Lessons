import allure
import unittest
from HW_24_RD_Project.Helpers.Webdriver import Webdriver


class BaseTestClass(unittest.TestCase):
    """Base test class"""

    @allure.step('Set up method')
    def setUp(self) -> None:
        """Setup method before every test"""
        self.driver = Webdriver().webdriver_setup()
        self.pageSetUp()

    @allure.step('Page set up method')
    def pageSetUp(self) -> None:
        """Page set up method"""
        self.page_url = 'http://litecart.stqa.ru/en/'
        self.driver.get(self.page_url)

    @allure.step('Tear down method')
    def tearDown(self) -> None:
        """Teardown method after every test"""
        self.driver.quit()

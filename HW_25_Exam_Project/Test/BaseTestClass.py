import unittest

from HW_25_Exam_Project.Helpers.Webdriver import Webdriver
from HW_25_Exam_Project.Page_Objects.MainPage import MainPage


class BaseTestClass(unittest.TestCase):
    """Base test class"""

    def setUp(self) -> None:
        """Setup method before every test"""
        self.driver = Webdriver().webdriver_setup()
        self.pageSetUp()

    def pageSetUp(self) -> None:
        """Page set up method"""
        self.page_url = 'http://gymn7.minsk.edu.by/'
        self.driver.get(self.page_url)
        self.main_page = MainPage(self.driver)

    def tearDown(self) -> None:
        """Teardown method after every test"""
        self.driver.quit()

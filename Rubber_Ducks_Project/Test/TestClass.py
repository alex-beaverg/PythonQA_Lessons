from Rubber_Ducks_Project.Test.BaseTestClass import BaseTestClass
from Rubber_Ducks_Project.Helpers.LogDecorator import log_decorator
from Rubber_Ducks_Project.Page_Objects.LoginPage import LoginPage
from Rubber_Ducks_Project.Page_Objects.RubberDucksPage import RubberDucksPage
from Rubber_Ducks_Project.Page_Objects.SubcategoryPage import SubcategoryPage


class TestClass(BaseTestClass):
    """Test class"""

    @log_decorator
    def test_01_open_login_page(self) -> None:
        """Test method to open login page"""
        self.login_page = LoginPage(self.driver)
        self.login_page.assert_title()

    @log_decorator
    def test_02_login_as_a_customer(self) -> None:
        """Test method to login as a customer"""
        self.login_page = LoginPage(self.driver)
        self.login_page.login_action()
        self.login_page.assert_login()

    @log_decorator
    def test_03_open_rubber_ducks_page(self) -> None:
        """Test method to open Rubber Ducks page"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.assert_title()

    @log_decorator
    def test_04_open_subcategory_page(self) -> None:
        """Test method to open Subcategory page"""
        self.subcategory_page = SubcategoryPage(self.driver)
        self.subcategory_page.main_menu.click_to_subcategory_item()
        self.subcategory_page.assert_title()

    @log_decorator
    def test_05_sort_rubber_ducks_by_name(self) -> None:
        """Test method to sort rubber ducks by name"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.sort_ducks_by_name()
        self.rubber_ducks_page.assert_sorting_by_name()

    @log_decorator
    def test_06_check_sticker_sale(self) -> None:
        """Test method to check sticker 'SALE'"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.assert_getting_sale()

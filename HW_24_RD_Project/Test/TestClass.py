# Running tests with generating allure reports:
#   python -m pytest HW_24_RD_Project/Test/TestClass.py --alluredir HW_24_RD_Project/test-allure-reports -s
# Showing allure reports:
#   allure serve HW_24_RD_Project/test-allure-reports

import allure

from HW_24_RD_Project.Test.BaseTestClass import BaseTestClass
from HW_24_RD_Project.Helpers.LogDecorator import log_decorator
from HW_24_RD_Project.Page_Objects.LoginPage import LoginPage
from HW_24_RD_Project.Page_Objects.RubberDucksPage import RubberDucksPage
from HW_24_RD_Project.Page_Objects.SubcategoryPage import SubcategoryPage


@allure.story('Rubber ducks website tests')
@allure.feature('All tests')
@allure.testcase('My educational testcase')
class TestClass(BaseTestClass):
    """Test class"""

    @allure.step('Test 01. Test method to open login page')
    @log_decorator
    def test_01_open_login_page(self) -> None:
        """Test method to open login page"""
        self.login_page = LoginPage(self.driver)
        self.login_page.assert_title()

    @allure.step("Test 02. Test method to login as a customer")
    @log_decorator
    def test_02_login_as_a_customer(self) -> None:
        """Test method to login as a customer"""
        self.login_page = LoginPage(self.driver)
        self.login_page.login_action()
        self.login_page.assert_login()

    @allure.step('Test 03. Test method to open Rubber Ducks page')
    @log_decorator
    def test_03_open_rubber_ducks_page(self) -> None:
        """Test method to open Rubber Ducks page"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.assert_title()

    @allure.step('Test 04. Test method to open Subcategory page')
    @log_decorator
    def test_04_open_subcategory_page(self) -> None:
        """Test method to open Subcategory page"""
        self.subcategory_page = SubcategoryPage(self.driver)
        self.subcategory_page.main_menu.click_to_subcategory_item()
        self.subcategory_page.assert_title()

    @allure.step('Test 05. Test method to sort rubber ducks by name')
    @log_decorator
    def test_05_sort_rubber_ducks_by_name(self) -> None:
        """Test method to sort rubber ducks by name"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.sort_ducks_by_name()
        self.rubber_ducks_page.assert_sorting_by_name()

    @allure.step('Test 06. Test method to check sticker "SALE"')
    @log_decorator
    def test_06_check_sticker_sale(self) -> None:
        """Test method to check sticker 'SALE'"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.assert_getting_sale()

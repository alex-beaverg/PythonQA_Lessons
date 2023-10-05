# Homework 20 - (2023.10.05)
# Homework -> Page Object and Page Element

import unittest
from typing import Self

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePageLocators:
    """Docstring: Class BasePageLocators"""
    PAGE_TITLE = (By.CSS_SELECTOR, 'h1.title')


class LoginPageLocators:
    """Docstring: Class LoginPageLocators"""
    TITLE_OF_LOGIN_BOX = (By.CSS_SELECTOR, '#box-account-login .title')
    INPUT_LOGIN = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    BUTTON_LOGIN = (By.NAME, 'login')
    TEXT_AFTER_LOGIN = (By.CSS_SELECTOR, '.notice.success')


class MainMenuElementLocators:
    """Docstring: Class MainMenuLocators"""
    MAIN_MENU_ITEM_ELEMENT = (By.CSS_SELECTOR, '#site-menu .category-1 > a')


class RubberDucksPageLocators:
    """Docstring: Class RubberDucksPageLocators"""
    DUCK = (By.CLASS_NAME, 'name')
    BUTTON_SORT_BY_NAME = (By.CSS_SELECTOR, 'nav.filter>a:first-child')
    STICKER_SALE = (By.CSS_SELECTOR, 'div.sticker.sale')


class SystemVariables:
    """Docstring: Class SystemVariables"""
    TIMEOUT = 5


class BasePage:
    """Docstring: Parent class BasePage (Design pattern Page Object)"""
    def __init__(self, driver) -> None:
        """Docstring: Constructor for class BasePage"""
        self.driver = driver
        self.main_menu = MainMenuElement(self.driver)

    def __get_title(self) -> str:
        """Docstring: Method to get title of page"""
        return self.driver.find_element(*BasePageLocators.PAGE_TITLE).text


class LoginPage(BasePage):
    """Docstring: Class LoginPage extends BasePage (Design pattern Page Object)"""
    def __init__(self, driver):
        """Docstring: Constructor for class LoginPage"""
        super().__init__(driver)
        self.__expected_title_of_login_box = 'Login'
        self.__login = 'a.beaverg@gmail.com'
        self.__password = 'Test1234!'
        self.__expected_part_of_text_after_login = 'Alexey Bobrikov'

    def __get_title_of_login_box(self) -> str:
        """Docstring: Method to get title of login page"""
        return self.driver.find_element(*LoginPageLocators.TITLE_OF_LOGIN_BOX).text

    def assert_title(self) -> None:
        """Docstring: Method to assert title"""
        assert self.__expected_title_of_login_box, self.__get_title_of_login_box()

    def login_action(self) -> None:
        """Docstring: Method to login"""
        self.driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(self.__login)
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(self.__password)
        self.driver.find_element(*LoginPageLocators.BUTTON_LOGIN).click()

    def __get_message(self) -> str:
        """Docstring: Method to get message after login"""
        return self.driver.find_element(*LoginPageLocators.TEXT_AFTER_LOGIN).text

    def assert_login(self) -> None:
        """Docstring: Method to assert login"""
        assert self.__expected_part_of_text_after_login in self.__get_message()


class MainMenuElement:
    """Docstring: Class MainMenuElement (Design pattern Page Element)"""

    def __init__(self, driver) -> None:
        """Docstring: Constructor for class MainMenuElement"""
        self.driver = driver

    def click_to_rubber_ducks_item(self) -> None:
        """Docstring: Method to click rubber ducks main menu item"""
        self.driver.find_element(*MainMenuElementLocators.MAIN_MENU_ITEM_ELEMENT).click()

    def click_to_subcategory_item(self) -> None:
        """Docstring: Method to click subcategory main menu item"""
        ActionChains(self.driver)\
            .move_to_element(self.driver.find_element(*MainMenuElementLocators.MAIN_MENU_ITEM_ELEMENT))\
            .move_by_offset(0, 45)\
            .click()\
            .perform()


class RubberDucksPage(BasePage):
    """Docstring: Class RubberDucksPage extends BasePage (Design pattern Page Object)"""
    def __init__(self, driver):
        """Docstring: Constructor for class RubberDucksPage"""
        super().__init__(driver)
        self.__rubber_ducks_title = 'Rubber Ducks'
        self.__all_ducks_before_sort = []
        self.__ducks_names_before_sort = []
        self.__all_ducks_after_sort = []
        self.__ducks_names_after_sort = []
        self.__expected_text_sale = 'SALE'

    def assert_title(self) -> None:
        """Docstring: Method to assert title"""
        assert self.__rubber_ducks_title, self.__get_title()

    def sort_ducks_by_name(self) -> None:
        """Docstring: Method to sort ducks by name"""
        self.driver.find_element(*RubberDucksPageLocators.BUTTON_SORT_BY_NAME).click()

    def assert_sorting_by_name(self) -> None:
        """Docstring: Method to assert sorting ducks by name"""
        self.__all_ducks_before_sort = self.driver.find_elements(*RubberDucksPageLocators.DUCK)
        for duck in self.__all_ducks_before_sort:
            self.__ducks_names_before_sort.append(duck.text)
        self.__ducks_names_before_sort.sort()
        self.__all_ducks_after_sort = self.driver.find_elements(*RubberDucksPageLocators.DUCK)
        for duck in self.__all_ducks_after_sort:
            self.__ducks_names_after_sort.append(duck.text)
        assert self.__ducks_names_after_sort, self.__ducks_names_before_sort

    def __get_sale(self) -> str:
        """Docstring: Method to get sticker 'SALE'"""
        return self.driver.find_element(*RubberDucksPageLocators.STICKER_SALE).text

    def assert_getting_sale(self) -> None:
        """Docstring: Method to assert getting sticker 'SALE'"""
        assert self.__expected_text_sale, self.__get_sale()


class SubcategoryPage(BasePage):
    """Docstring: Class SubcategoryPage (Design pattern Page Object)"""
    def __init__(self, driver):
        """Docstring: Constructor for class RubberDucksPage"""
        super().__init__(driver)
        self.__subcategory_title = 'Subcategory'

    def assert_title(self) -> None:
        assert self.__subcategory_title, self.__get_title()


class ChromeDriverSingleton(webdriver.Chrome):
    """Docstring: Class singleton ChromeWebDriver"""
    def __new__(cls):
        """Docstring: Special constructor for singleton class ChromeWebDriver"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChromeDriverSingleton, cls).__new__(cls)
        return cls.instance

    def webdriver_setup(self) -> Self:
        """Docstring: Method to set up webdriver"""
        self.maximize_window()
        self.implicitly_wait(SystemVariables.TIMEOUT)
        return self


class TestClass(unittest.TestCase):
    """Docstring: Test class"""
    def setUp(self) -> None:
        """Docstring: Setup method before every test"""
        self.driver = ChromeDriverSingleton().webdriver_setup()
        self.pageSetUp()

    def pageSetUp(self) -> None:
        """Docstring: Page set up method"""
        self.page_url = 'http://litecart.stqa.ru/en/'
        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        """Docstring: Teardown method after every test"""
        self.driver.quit()

    def test_01_open_login_page(self) -> None:
        """Docstring: Test method to open login page"""
        self.login_page = LoginPage(self.driver)
        self.login_page.assert_title()

    def test_02_login_as_a_customer(self) -> None:
        """Docstring: Test method to login as a customer"""
        self.login_page = LoginPage(self.driver)
        self.login_page.login_action()
        self.login_page.assert_login()

    def test_03_open_rubber_ducks_page(self) -> None:
        """Docstring: Test method to open Rubber Ducks page"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.assert_title()

    def test_04_open_subcategory_page(self) -> None:
        """Docstring: Test method to open Subcategory page"""
        self.subcategory_page = SubcategoryPage(self.driver)
        self.subcategory_page.main_menu.click_to_subcategory_item()
        self.subcategory_page.assert_title()

    def test_05_sort_rubber_ducks_by_name(self) -> None:
        """Docstring: Test method to sort rubber ducks by name"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.sort_ducks_by_name()
        self.rubber_ducks_page.assert_sorting_by_name()

    def test_06_check_sticker_sale(self) -> None:
        """Docstring: Test method to check sticker 'SALE'"""
        self.rubber_ducks_page = RubberDucksPage(self.driver)
        self.rubber_ducks_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_ducks_page.assert_getting_sale()

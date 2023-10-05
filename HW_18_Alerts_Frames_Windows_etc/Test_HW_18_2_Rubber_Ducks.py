# Homework 18, file 2 - (2023.09.26)
# Homework -> Rubber ducks website tests
# Run configuration -> Current File
# Run: Shift + F10

import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class ChromeDriverSingleton(webdriver.Chrome):
    """Docstring: Class singleton ChromeWebDriver"""

    def __new__(cls):
        """Docstring: Special constructor for singleton class ChromeWebDriver"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChromeDriverSingleton, cls).__new__(cls)
        return cls.instance


class TestClassForRubberDucksSite(unittest.TestCase):
    """Docstring: Test class"""

    def setUp(self) -> None:
        """Docstring: Setup method before every test"""
        self.setWebdriver()
        self.webdriverSetUp()
        self.pageSetUp()
        self.setTestsParameters()

    def setWebdriver(self) -> None:
        """Docstring: Set webdriver setup method"""
        self.driver = ChromeDriverSingleton()

    def webdriverSetUp(self) -> None:
        """Docstring: Webdriver setup method"""
        self.timeout = 5
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)

    def pageSetUp(self) -> None:
        """Docstring: Page URLs method"""
        self.page_url = 'https://litecart.stqa.ru/en/'
        self.driver.get(self.page_url)

    def setTestsParameters(self) -> None:
        """Docstring: Method to set parameters to all tests"""
        self.setLocators()
        self.setVariables()

    def setLocators(self) -> None:
        """Docstring: Set locators method"""
        self.title_of_login_box_css_selector = '#box-account-login .title'
        self.input_login_element_name = 'email'
        self.input_password_element_name = 'password'
        self.button_login_element_name = 'login'
        self.text_after_login_css_selector = '.notice.success'

        self.rubber_ducks_menu_item_element_css_selector = '#site-menu .category-1 > a'

        self.text_after_click_to_menu_item_element_css_selector = 'h1.title'
        self.duck_class = 'name'
        self.button_sort_by_name_element_css_selector = 'nav.filter>a:first-child'
        self.sticker_sale_element_css_selector = 'div.sticker.sale'

    def setVariables(self) -> None:
        """Docstring: Set variables method"""
        self.expected_title_of_login_box = 'Login'
        self.login = 'a.beaverg@gmail.com'
        self.password = 'Test1234!'
        self.expected_part_of_text_after_login = 'Alexey Bobrikov'
        self.expected_text_after_click_to_rubber_ducks_menu_item = 'Rubber Ducks'
        self.expected_text_after_click_to_subcategory_menu_item = 'Subcategory'
        self.expected_text_sale = 'SALE'

    def tearDown(self) -> None:
        """Docstring: Teardown method after every test"""
        self.driver.quit()

    def test_01_open_login_page(self) -> None:
        """Docstring: Test method to open login page"""
        self.title_of_login_box = self.driver.find_element(By.CSS_SELECTOR, self.title_of_login_box_css_selector).text
        self.assertEqual(self.expected_title_of_login_box, self.title_of_login_box)

    def test_02_login_as_a_customer(self) -> None:
        """Docstring: Test method to login as a customer"""
        self.input_login_element = self.driver.find_element(By.NAME, self.input_login_element_name)
        self.input_login_element.send_keys(self.login)
        self.input_password_element = self.driver.find_element(By.NAME, self.input_password_element_name)
        self.input_password_element.send_keys(self.password)
        self.button_login_element = self.driver.find_element(By.NAME, self.button_login_element_name)
        self.button_login_element.click()
        self.text_after_login_element = self.driver.find_element(By.CSS_SELECTOR, self.text_after_login_css_selector)
        self.assertTrue(self.text_after_login_element.text.__contains__(self.expected_part_of_text_after_login))

    def test_03_open_rubber_ducks_page(self) -> None:
        """Docstring: Test method to open Rubber Ducks page"""
        self.rubber_ducks_menu_item_element = self.driver\
            .find_element(By.CSS_SELECTOR, self.rubber_ducks_menu_item_element_css_selector)
        self.rubber_ducks_menu_item_element.click()
        self.text_after_click_to_rubber_ducks_menu_item = self.driver\
            .find_element(By.CSS_SELECTOR, self.text_after_click_to_menu_item_element_css_selector).text
        self.assertEqual(self.expected_text_after_click_to_rubber_ducks_menu_item,
                         self.text_after_click_to_rubber_ducks_menu_item)

    def test_04_open_subcategory_page(self) -> None:
        """Docstring: Test method to opem Subcategory page"""
        self.rubber_ducks_menu_item_element = self.driver \
            .find_element(By.CSS_SELECTOR, self.rubber_ducks_menu_item_element_css_selector)
        ActionChains(self.driver)\
            .move_to_element(self.rubber_ducks_menu_item_element)\
            .move_by_offset(0, 45)\
            .click()\
            .perform()
        self.text_after_click_to_subcategory_menu_item = self.driver \
            .find_element(By.CSS_SELECTOR, self.text_after_click_to_menu_item_element_css_selector).text
        self.assertEqual(self.expected_text_after_click_to_subcategory_menu_item,
                         self.text_after_click_to_subcategory_menu_item)

    def test_05_sort_rubber_ducks_by_name(self) -> None:
        """Docstring: Test method to sort rubber ducks by name"""
        self.rubber_ducks_menu_item_element = self.driver \
            .find_element(By.CSS_SELECTOR, self.rubber_ducks_menu_item_element_css_selector)
        self.rubber_ducks_menu_item_element.click()
        self.all_ducks_before_sort = self.driver.find_elements(By.CLASS_NAME, self.duck_class)
        self.ducks_names_before_sort = []
        for duck in self.all_ducks_before_sort:
            self.ducks_names_before_sort.append(duck.text)
        self.ducks_names_before_sort.sort()
        self.button_sort_by_name = self.driver\
            .find_element(By.CSS_SELECTOR, self.button_sort_by_name_element_css_selector)
        self.button_sort_by_name.click()
        self.all_ducks_after_sort = self.driver.find_elements(By.CLASS_NAME, self.duck_class)
        self.ducks_names_after_sort = []
        for duck in self.all_ducks_after_sort:
            self.ducks_names_after_sort.append(duck.text)
        self.assertEqual(self.ducks_names_after_sort, self.ducks_names_before_sort)

    def test_06_check_sticker_sale(self) -> None:
        """Docstring: Test method to check sticker 'Sale'"""
        self.rubber_ducks_menu_item_element = self.driver \
            .find_element(By.CSS_SELECTOR, self.rubber_ducks_menu_item_element_css_selector)
        self.rubber_ducks_menu_item_element.click()
        self.text_sale = self.driver.find_element(By.CSS_SELECTOR, self.sticker_sale_element_css_selector).text
        self.assertEqual(self.expected_text_sale, self.text_sale)

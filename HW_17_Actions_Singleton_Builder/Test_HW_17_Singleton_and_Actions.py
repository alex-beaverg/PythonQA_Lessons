# Homework 17, file 2 - (2023.09.19)
# Homework -> ActionChains and Singleton
# Run configuration -> Current File
# Run: Shift + F10

import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class WebDriverSingleton(webdriver.Chrome):
    """Docstring: Class singleton ChromeWebDriver"""

    def __new__(cls):
        """Docstring: Special constructor for singleton class ChromeWebDriver"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(WebDriverSingleton, cls).__new__(cls)
        return cls.instance


class TestClass(unittest.TestCase):
    """Docstring: Test class"""

    def setUp(self) -> None:
        """Docstring: Setup method before every test"""
        self.setWebdriver()
        self.webdriverSetUp()
        self.pageSetUp()
        self.setTestsParameters()

    def setWebdriver(self) -> None:
        """Docstring: Set webdriver setup method"""
        self.driver = WebDriverSingleton()

    def webdriverSetUp(self) -> None:
        """Docstring: Webdriver setup method"""
        self.timeout = 5
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)

    def pageSetUp(self) -> None:
        """Docstring: Page setup method"""
        self.page_url = 'https://the-internet.herokuapp.com/'
        self.driver.get(self.page_url)

    def setTestsParameters(self) -> None:
        """Docstring: Method to set parameters to all tests"""
        self.setLocators()
        self.setVariables()

    def setLocators(self) -> None:
        """Docstring: Set locators method"""
        self.drag_and_drop_link_text = 'Drag and Drop'
        self.area_a_id = 'column-a'
        self.area_b_id = 'column-b'
        self.hovers_link_text = 'Hovers'
        self.user_1_css_selector = '#content>div>div:nth-child(3)>img'
        self.user_1_page_tag_name = 'h1'
        self.expected_user_1_page_text = 'Not Found'

    def setVariables(self) -> None:
        """Docstring: Set variables method"""
        self.expected_letter = 'A'

    def tearDown(self) -> None:
        """Docstring: Teardown method after every test"""
        self.driver.quit()

    def following_the_link(self, link_text: str) -> None:
        """Docstring: Method to follow the link"""
        self.driver.find_element(By.LINK_TEXT, link_text).click()

    def test_01_drag_and_drop(self) -> None:
        """Docstring: Test 01 (Drag and Drop elements)"""
        self.following_the_link(self.drag_and_drop_link_text)
        self.drag_and_drop_from_element = self.driver.find_element(By.ID, self.area_a_id)
        self.drag_and_drop_to_element = self.driver.find_element(By.ID, self.area_b_id)
        ActionChains(self.driver)\
            .drag_and_drop(self.drag_and_drop_from_element, self.drag_and_drop_to_element).perform()
        self.assertEqual(self.expected_letter, self.drag_and_drop_to_element.text)

    def test_02_hovers(self) -> None:
        """Docstring: Test 02 (Hovers)"""
        self.following_the_link(self.hovers_link_text)
        self.user_1_element = self.driver.find_element(By.CSS_SELECTOR, self.user_1_css_selector)
        ActionChains(self.driver).move_to_element(self.user_1_element).move_by_offset(0, 130).click().perform()
        self.user_1_page_text = self.driver.find_element(By.TAG_NAME, self.user_1_page_tag_name).text
        self.assertEqual(self.expected_user_1_page_text, self.user_1_page_text)

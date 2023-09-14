# Homework 15, file 1 - (2023.09.12)
# Classwork -> Refactoring and decomposition of HW_14
# Run configuration -> Current File
# Run: Shift + F10

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestHomeWork15File1(unittest.TestCase):
    """Docstring: Test class"""

    def setUp(self) -> None:
        """Docstring: Setup method before every test"""
        self.setWebdriver()
        self.webdriverSetUp()
        self.setVariables()
        self.preSteps()

    def setWebdriver(self) -> None:
        """Docstring: Set webdriver setup method"""
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Edge()
        # self.driver = webdriver.Firefox()

    def webdriverSetUp(self) -> None:
        """Docstring: Webdriver setup method"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def setVariables(self) -> None:
        """Docstring: Set variables setup method"""
        self.page_url = "https://www.google.com/"
        self.search_field_id = "APjFqb"
        self.search_text = "IT STEP"
        self.link_partial_text = "Академия ШАГ: Компьютерные курсы IT"
        self.expected_url = "https://itstep.by/"

    def preSteps(self) -> None:
        """Docstring: Pre-steps setup method"""
        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        """Docstring: Teardown method after every test"""
        self.driver.quit()

    def test_01_open_itstep_page_with_google_search(self) -> None:
        """Docstring: Test 01 (open IT STEP page with Google search)"""
        self.search_field_element = self.driver.find_element(By.ID, self.search_field_id)
        self.search_field_element.send_keys(self.search_text + Keys.ENTER)
        self.link_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.link_partial_text)
        self.link_element.click()
        self.assertEqual(self.expected_url, self.driver.current_url)

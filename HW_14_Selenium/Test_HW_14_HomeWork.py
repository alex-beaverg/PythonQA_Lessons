# Homework 14 - (2023.09.07)
# Run configuration -> Current File
# Run: Shift + F10

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestHomeWork14(unittest.TestCase):
    """Docstring: Test class"""
    def setUp(self) -> None:
        """Docstring: Method before every test"""
        self.page_url = "https://www.google.com/"
        self.search_field_id = "APjFqb"
        self.search_text = "IT STEP"
        self.link_partial_text = "Академия ШАГ: Компьютерные курсы IT"
        self.expected_url = "https://itstep.by/"

    def tearDown(self) -> None:
        """Docstring: Method after every test"""
        self.driver.quit()

    def test_01_open_itstep_page_with_google_search_in_chrome(self) -> None:
        """Docstring: Test 01 (open IT STEP page with Google search in Chrome browser)"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Waiter for load pages:
        self.driver.implicitly_wait(10)

        self.driver.get(self.page_url)
        self.search_field_element = self.driver.find_element(By.ID, self.search_field_id)
        self.search_field_element.send_keys(self.search_text + Keys.ENTER)
        self.link_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.link_partial_text)
        self.link_element.click()
        self.assertEqual(self.expected_url, self.driver.current_url)

    def test_02_open_itstep_page_with_google_search_in_edge(self) -> None:
        """Docstring: Test 02 (open IT STEP page with Google search in Edge browser)"""
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

        # Waiter for load pages:
        self.driver.implicitly_wait(10)

        self.driver.get(self.page_url)
        self.search_field_element = self.driver.find_element(By.ID, self.search_field_id)
        self.search_field_element.send_keys(self.search_text + Keys.ENTER)
        self.link_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.link_partial_text)
        self.link_element.click()

        self.assertEqual(self.expected_url, self.driver.current_url)

    def test_03_open_itstep_page_with_google_search_in_firefox(self) -> None:
        """Docstring: Test 03 (open IT STEP page with Google search in Firefox browser)"""
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        # Waiter for load pages:
        self.driver.implicitly_wait(10)

        self.driver.get(self.page_url)
        self.search_field_element = self.driver.find_element(By.ID, self.search_field_id)
        self.search_field_element.send_keys(self.search_text + Keys.ENTER)
        self.link_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.link_partial_text)
        self.link_element.click()

        self.assertEqual(self.expected_url, self.driver.current_url)

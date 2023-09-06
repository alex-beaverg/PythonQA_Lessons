# Homework 13 - (2023.09.05)
# Run configuration -> Current File
# Run: Shift + F10

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestHomeWork(unittest.TestCase):
    """Docstring: Test class"""

    def setUp(self) -> None:
        """Docstring: Method before every test"""
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def tearDown(self) -> None:
        """Docstring: Method after every test"""
        self.driver.quit()

    def test_01_open_and_search_and_assert(self):
        """Docstring: Test 01 (my own test)"""
        self.page_url = "https://www.selenium.dev/"
        self.driver.get(self.page_url)
        self.search_field = self.driver.find_element(By.CLASS_NAME, "DocSearch-Button-Placeholder")
        self.search_field.click()
        self.real_search_field = self.driver.find_element(By.ID, "docsearch-input")
        self.real_search_field.send_keys("IDE")
        time.sleep(1)
        self.real_search_field.send_keys(Keys.ENTER)
        self.find_text = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Selenium", self.find_text)

    def test_02_from_presentation(self):
        """Docstring: Test 02 (from presentation)"""
        self.page_url = "https://the-internet.herokuapp.com/"
        self.driver.get(self.page_url)
        self.links = self.driver.find_elements(By.TAG_NAME, "a")
        self.links[10].click()
        self.find_text = self.driver.find_element(By.TAG_NAME, "h3").text
        self.assertEqual(self.find_text, "Drag and Drop")
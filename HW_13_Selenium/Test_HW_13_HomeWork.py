# Homework 13 - (2023.09.05)
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestHomeWork(unittest.TestCase):

    def test_open_page_and_search(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.page_url = "https://www.google.com/"
        self.driver.get(self.page_url)
        self.search_field = self.driver.find_element(By.ID, "APjFqb")
        self.search_field.send_keys("Intel" + Keys.ENTER)
        time.sleep(5)
        self.title = self.driver.title
        self.assertIn("Google", self.title)
        self.driver.close()

# Homework 15, file 2 - (2023.09.14)
# Homework -> Using selene library
# Run configuration -> Current File
# Run: Shift + F10

import unittest

from selene.api import *
from selenium import webdriver


class TestClass(unittest.TestCase):
    """Docstring: Test class"""

    def setUp(self) -> None:
        """Docstring: Setup method before every test"""
        self.webdriverSetUp()
        self.setTestsParameters()
        self.pageSetUp()

    def tearDown(self) -> None:
        """Docstring: Teardown method after every test"""
        self.driver.quit()

    def webdriverSetUp(self) -> None:
        """Docstring: Webdriver setup method"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        browser.set_driver(self.driver)

    def pageSetUp(self) -> None:
        """Docstring: Page setup method"""
        browser.open_url(self.expected_url)

    def setTestsParameters(self) -> None:
        """Docstring: Method to set parameters to all tests"""
        self.setLocators()
        self.setVariables()

    def setLocators(self) -> None:
        """Docstring: Set locators method"""
        self.login_field_id = 'passp-field-login'
        self.wrong_message_id = 'field:input-login:hint'

    def setVariables(self) -> None:
        """Docstring: Set variables method"""
        self.expected_url = 'https://passport.yandex.by/auth'
        self.invalid_login = 'invalid-account-123-123'
        self.expected_invalid_login_text = 'Нет такого аккаунта'

    def test_01_yandex_account_invalid_login(self) -> None:
        """Docstring: Test 01 (Yandex account invalid log in)"""
        s(by.id(self.login_field_id)).set_value(self.invalid_login).press_enter()
        s(by.id(self.wrong_message_id)).should(have.text(self.expected_invalid_login_text))

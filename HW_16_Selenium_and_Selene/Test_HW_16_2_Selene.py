# Homework 15, file 2 - (2023.09.14)
# Homework -> Using selene library
# Run configuration -> Current File
# Run: Shift + F10

import unittest

from parameterized import parameterized
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
        self.empty_login = ''
        self.correct_symbol = 'q'
        self.long_login = 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
        self.expected_invalid_login_text = 'Нет такого аккаунта'
        self.expected_empty_login_text = 'Логин не указан'
        self.expected_not_suitable_login_text = 'Такой логин не подойдет'

    @staticmethod
    def get_wrong_symbols() -> list:
        """Docstring: Static method to get list of wrong symbols for parametrize test methods"""
        return [';', ':', '!', '(', ')']

    def test_01_yandex_account_invalid_login(self) -> None:
        """Docstring: Test 01 (Yandex account invalid log in)"""
        s(by.id(self.login_field_id)).set_value(self.invalid_login).press_enter()
        s(by.id(self.wrong_message_id)).should(have.text(self.expected_invalid_login_text))

    def test_02_yandex_account_empty_login(self) -> None:
        """Docstring: Test 02 (Yandex account empty log in)"""
        s(by.id(self.login_field_id)).set_value(self.empty_login).press_enter()
        s(by.id(self.wrong_message_id)).should(have.text(self.expected_empty_login_text))

    @parameterized.expand(get_wrong_symbols())
    def test_03_yandex_account_wrong_symbol_login(self, wrong_symbol: str) -> None:
        """Docstring: Test 03 (Yandex account wrong symbol log in)"""
        s(by.id(self.login_field_id)).set_value(wrong_symbol).press_enter()
        s(by.id(self.wrong_message_id)).should(have.text(self.expected_not_suitable_login_text))

    @parameterized.expand(get_wrong_symbols())
    def test_04_yandex_account_login_with_wrong_symbol(self, wrong_symbol: str) -> None:
        """Docstring: Test 04 (Yandex account log in with wrong symbol)"""
        s(by.id(self.login_field_id)).set_value(self.correct_symbol + wrong_symbol).press_enter()
        s(by.id(self.wrong_message_id)).should(have.text(self.expected_not_suitable_login_text))

    def test_05_yandex_account_long_login(self) -> None:
        """Docstring: Test 05 (Yandex account long log in)"""
        s(by.id(self.login_field_id)).set_value(self.long_login).press_enter()
        s(by.id(self.wrong_message_id)).should(have.text(self.expected_not_suitable_login_text))

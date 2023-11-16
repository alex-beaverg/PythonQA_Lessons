from selenium import webdriver
from typing import Self
from HW_24_RD_Project.Helpers.SystemVariables import SystemVariables


class Webdriver(webdriver.Chrome):
    """Docstring: Class singleton ChromeWebDriver"""
    def __new__(cls):
        """Docstring: Special constructor for singleton class ChromeWebDriver"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Webdriver, cls).__new__(cls)
        return cls.instance

    def webdriver_setup(self) -> Self:
        """Docstring: Method to set up webdriver"""
        self.maximize_window()
        self.implicitly_wait(SystemVariables.TIMEOUT)
        return self
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from HW_25_Exam_Project.Helpers.Locators import MainMenuElementLocators
from HW_25_Exam_Project.Helpers.Locators import OneWindowSubMenuElementLocators


class OneWindowSubMenuElement:
    """Class OneWindowMenuElement"""

    def __init__(self, driver) -> None:
        """Constructor for class OneWindowMenuElement"""
        self.driver = driver

    def click_to_schedule_item(self) -> None:
        """Method to click "Schedule" menu item"""
        schedule_item = self.driver.find_element(*OneWindowSubMenuElementLocators.SCHEDULE)
        ActionChains(self.driver)\
            .move_to_element(self.one_window_hover())\
            .move_to_element(schedule_item).click()\
            .perform()

    def click_to_procedures_item(self) -> None:
        """Method to click "Procedures" menu item"""
        procedures_item = self.driver.find_element(*OneWindowSubMenuElementLocators.PROCEDURES)
        ActionChains(self.driver)\
            .move_to_element(self.one_window_hover())\
            .move_to_element(procedures_item)\
            .click()\
            .perform()

    def one_window_hover(self) -> WebElement:
        return self.driver.find_element(*MainMenuElementLocators.ONE_WINDOW)
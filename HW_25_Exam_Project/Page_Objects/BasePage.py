from HW_25_Exam_Project.Page_Elements.MainMenuElement import MainMenuElement
from HW_25_Exam_Project.Helpers.Locators import BasePageLocators


class BasePage:
    """Parent class BasePage"""

    def __init__(self, driver) -> None:
        """Constructor for class BasePage"""
        self.driver = driver
        self.main_menu = MainMenuElement(self.driver)

    def __get_title(self) -> str:
        """Method to get title of "Base" page"""
        return self.driver.find_element(*BasePageLocators.PAGE_TITLE).text
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from HW_25_Exam_Project.Helpers.Locators import MainMenuElementLocators
from HW_25_Exam_Project.Helpers.Locators import AboutSubMenuElementLocators


class AboutSubMenuElement:
    """Class AboutSubMenuElement"""

    def __init__(self, driver) -> None:
        """Constructor for class AboutSubMenuElement"""
        self.driver = driver

    def click_to_goals_and_tasks_item(self) -> None:
        """Method to click "Goals and tasks" menu item"""
        goals_and_tasks_item = self.driver.find_element(*AboutSubMenuElementLocators.GOALS_AND_TASKS)
        ActionChains(self.driver)\
            .move_to_element(self.about_hover())\
            .move_to_element(goals_and_tasks_item)\
            .click()\
            .perform()

    def click_to_history_and_traditions_item(self) -> None:
        """Method to click "History and traditions" menu item"""
        history_and_traditions_item = self.driver.find_element(*AboutSubMenuElementLocators.HISTORY_AND_TRADITIONS)
        ActionChains(self.driver)\
            .move_to_element(self.about_hover())\
            .move_to_element(history_and_traditions_item)\
            .click()\
            .perform()

    def about_hover(self) -> WebElement:
        return self.driver.find_element(*MainMenuElementLocators.ABOUT)
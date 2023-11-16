from selenium.webdriver import ActionChains
from HW_24_RD_Project.Helpers.Locators import MainMenuElementLocators


class MainMenuElement:
    """Class MainMenuElement"""

    def __init__(self, driver) -> None:
        """Constructor for class MainMenuElement"""
        self.driver = driver

    def click_to_rubber_ducks_item(self) -> None:
        """Method to click rubber ducks main menu item"""
        self.driver.find_element(*MainMenuElementLocators.MAIN_MENU_ITEM_ELEMENT).click()

    def click_to_subcategory_item(self) -> None:
        """Method to click subcategory main menu item"""
        ActionChains(self.driver) \
            .move_to_element(self.driver.find_element(*MainMenuElementLocators.MAIN_MENU_ITEM_ELEMENT)) \
            .move_by_offset(0, 45) \
            .click() \
            .perform()

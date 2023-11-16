from HW_25_Exam_Project.Helpers.Locators import MainMenuElementLocators
from HW_25_Exam_Project.Page_Elements.AboutSubMenuElement import AboutSubMenuElement
from HW_25_Exam_Project.Page_Elements.OneWindowSubMenuElement import OneWindowSubMenuElement


class MainMenuElement:
    """Class MainMenuElement"""

    def __init__(self, driver) -> None:
        """Constructor for class MainMenuElement"""
        self.driver = driver
        self.one_window_sub_menu = OneWindowSubMenuElement(self.driver)
        self.about_sub_menu = AboutSubMenuElement(self.driver)

    def click_to_one_window_item(self) -> None:
        """Method to click 'One window' main menu item"""
        self.driver.find_element(*MainMenuElementLocators.ONE_WINDOW).click()

    def click_to_about_item(self) -> None:
        """Method to click 'About' main menu item"""
        self.driver.find_element(*MainMenuElementLocators.ABOUT).click()

    def click_to_teachers_room_item(self) -> None:
        """Method to click 'Teachers room' main menu item"""
        self.driver.find_element(*MainMenuElementLocators.TEACHERS_ROOM).click()

    def click_to_pupils_item(self) -> None:
        """Method to click 'Pupils' main menu item"""
        self.driver.find_element(*MainMenuElementLocators.PUPILS).click()

    def click_to_graduates_item(self) -> None:
        """Method to click 'Graduates' main menu item"""
        self.driver.find_element(*MainMenuElementLocators.GRADUATES).click()

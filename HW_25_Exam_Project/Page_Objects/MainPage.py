from HW_25_Exam_Project.Page_Objects.BasePage import BasePage
from HW_25_Exam_Project.Helpers.Locators import MainPageLocators


class MainPage(BasePage):
    """Class MainPage"""

    def __init__(self, driver) -> None:
        """Constructor for class MainPage"""
        super().__init__(driver)
        self.__main_page_title = 'Новости учреждения'

    def __get_main_page_title(self) -> str:
        """Method to get title of "Main" page"""
        return self.driver.find_element(*MainPageLocators.MAIN_PAGE_TITLE).text

    def assert_main_page_title(self) -> None:
        """Method to assert "Main" page title"""
        assert self.__main_page_title, self.__get_main_page_title()
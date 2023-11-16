from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class AboutPage(BasePage):
    """Class AboutPage"""

    def __init__(self, driver) -> None:
        """Constructor for class AboutPage"""
        super().__init__(driver)
        self.__about_page_title = 'О гимназии'

    def assert_about_page_title(self) -> None:
        """Method to assert "About" page title"""
        assert self.__about_page_title, self.__get_title()

from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class OneWindowPage(BasePage):
    """Class OneWindowPage"""

    def __init__(self, driver) -> None:
        """Constructor for class OneWindowPage"""
        super().__init__(driver)
        self.__one_window_page_title = 'Одно окно'

    def assert_one_window_page_title(self) -> None:
        """Method to assert "One window" page title"""
        assert self.__one_window_page_title, self.__get_title()
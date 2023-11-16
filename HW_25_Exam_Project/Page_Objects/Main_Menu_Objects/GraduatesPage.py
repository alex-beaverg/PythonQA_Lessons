from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class GraduatesPage(BasePage):
    """Class GraduatesPage"""

    def __init__(self, driver) -> None:
        """Constructor for class GraduatesPage"""
        super().__init__(driver)
        self.__graduates_page_title = 'Выпускнику'

    def assert_graduates_page_title(self) -> None:
        """Method to assert "Graduates" page title"""
        assert self.__graduates_page_title, self.__get_title()
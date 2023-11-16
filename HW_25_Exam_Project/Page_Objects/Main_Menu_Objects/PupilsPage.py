from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class PupilsPage(BasePage):
    """Class PupilsPage"""

    def __init__(self, driver) -> None:
        """Constructor for class PupilsPage"""
        super().__init__(driver)
        self.__pupils_page_title = 'Учащимся'

    def assert_pupils_page_title(self) -> None:
        """Method to assert "Pupils" page title"""
        assert self.__pupils_page_title, self.__get_title()

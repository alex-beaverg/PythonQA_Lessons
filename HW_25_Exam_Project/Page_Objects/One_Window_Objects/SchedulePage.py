from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class SchedulePage(BasePage):
    """Class SchedulePage"""

    def __init__(self, driver) -> None:
        """Constructor for class SchedulePage"""
        super().__init__(driver)
        self.__schedule_page_title = 'График работы руководства'

    def assert_schedule_page_title(self) -> None:
        """Method to assert "Schedule" page title"""
        assert self.__schedule_page_title, self.__get_title()
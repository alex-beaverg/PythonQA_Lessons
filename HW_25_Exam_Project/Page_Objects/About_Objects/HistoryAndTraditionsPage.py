from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class HistoryAndTraditionsPage(BasePage):
    """Class HistoryAndTraditionsPage"""

    def __init__(self, driver) -> None:
        """Constructor for class HistoryAndTraditionsPage"""
        super().__init__(driver)
        self.__history_and_traditions_page_title = 'История и традиции'

    def assert_history_and_traditions_page_title(self) -> None:
        """Method to assert "History and traditions" page title"""
        assert self.__history_and_traditions_page_title, self.__get_title()
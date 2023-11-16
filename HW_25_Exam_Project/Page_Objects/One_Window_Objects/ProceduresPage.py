from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class ProceduresPage(BasePage):
    """Class ProceduresPage"""

    def __init__(self, driver) -> None:
        """Constructor for class ProceduresPage"""
        super().__init__(driver)
        self.__procedures_page_title = 'Административные процедуры'

    def assert_procedures_page_title(self) -> None:
        """Method to assert "Procedures" page title"""
        assert self.__procedures_page_title, self.__get_title()
from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class GoalsAndTasksPage(BasePage):
    """Class GoalsAndTasksPage"""

    def __init__(self, driver) -> None:
        """Constructor for class GoalsAndTasksPage"""
        super().__init__(driver)
        self.__goals_and_tasks_page_title = 'Цели и задачи'

    def assert_goals_and_tasks_page_title(self) -> None:
        """Method to assert "Goals and tasks" page title"""
        assert self.__goals_and_tasks_page_title, self.__get_title()
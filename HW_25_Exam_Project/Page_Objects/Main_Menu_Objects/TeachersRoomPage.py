from HW_25_Exam_Project.Page_Objects.BasePage import BasePage


class TeachersRoomPage(BasePage):
    """Class TeachersRoomPage"""

    def __init__(self, driver) -> None:
        """Constructor for class TeachersRoomPage"""
        super().__init__(driver)
        self.__teachers_room_page_title = 'Учительская'

    def assert_teachers_room_page_title(self) -> None:
        """Method to assert "Teachers room" page title"""
        assert self.__teachers_room_page_title, self.__get_title()
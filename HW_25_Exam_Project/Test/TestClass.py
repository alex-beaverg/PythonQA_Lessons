# Running tests with generating allure reports:
#   python -m pytest HW_25_Exam_Project/Test/TestClass.py --alluredir HW_25_Exam_Project/test-allure-reports -s
# Showing allure reports:
#   allure serve HW_25_Exam_Project/test-allure-reports

import glamor as allure

from HW_25_Exam_Project.Page_Objects.About_Objects.GoalsAndTasksPage import GoalsAndTasksPage
from HW_25_Exam_Project.Page_Objects.About_Objects.HistoryAndTraditionsPage import HistoryAndTraditionsPage
from HW_25_Exam_Project.Page_Objects.Main_Menu_Objects.AboutPage import AboutPage
from HW_25_Exam_Project.Page_Objects.Main_Menu_Objects.GraduatesPage import GraduatesPage
from HW_25_Exam_Project.Page_Objects.Main_Menu_Objects.PupilsPage import PupilsPage
from HW_25_Exam_Project.Page_Objects.Main_Menu_Objects.TeachersRoomPage import TeachersRoomPage
from HW_25_Exam_Project.Page_Objects.One_Window_Objects.ProceduresPage import ProceduresPage
from HW_25_Exam_Project.Page_Objects.One_Window_Objects.SchedulePage import SchedulePage
from HW_25_Exam_Project.Test.BaseTestClass import BaseTestClass
from HW_25_Exam_Project.Page_Objects.Main_Menu_Objects.OneWindowPage import OneWindowPage


@allure.feature('Gymnasium N7 website tests')
@allure.story('"Main" page testing')
class TestClass01MainPage(BaseTestClass):
    """Test class for "Main" page testing"""

    @allure.title('Opening "Main" page')
    @allure.step('Checking opening of "Main" page')
    def test_01_open_main_page(self) -> None:
        """Test method to open "Main" page"""
        self.main_page.assert_main_page_title()


@allure.feature('Gymnasium N7 website tests')
@allure.story('"Main" menu testing')
class TestClass02MainMenu(BaseTestClass):
    """Test class for "Main" menu testing"""

    @allure.title('Opening "One window" page')
    @allure.step('Checking opening of "One window" page by clicking to main menu item from main page')
    def test_01_click_to_one_window_main_menu_item(self) -> None:
        """Test method to click to "One window" main menu item from main page"""
        self.main_page.main_menu.click_to_one_window_item()
        self.one_window_page = OneWindowPage(self.driver)
        self.one_window_page.assert_one_window_page_title()

    @allure.title('Opening "About" page')
    @allure.step('Checking opening of "About" page by clicking to main menu item from main page')
    def test_02_click_to_about_main_menu_item(self) -> None:
        """Test method to click to "About" main menu item from main page"""
        self.main_page.main_menu.click_to_about_item()
        self.about_page = AboutPage(self.driver)
        self.about_page.assert_about_page_title()

    @allure.title('Opening "Teachers room" page')
    @allure.step('Checking opening of "Teachers room" page by clicking to main menu item from main page')
    def test_03_click_to_teachers_room_main_menu_item(self) -> None:
        """Test method to click to "Teachers room" main menu item from main page"""
        self.main_page.main_menu.click_to_teachers_room_item()
        self.teachers_room_page = TeachersRoomPage(self.driver)
        self.teachers_room_page.assert_teachers_room_page_title()

    @allure.title('Opening "Pupils" page')
    @allure.step('Checking opening of "Pupils" page by clicking to main menu item from main page')
    def test_04_click_to_pupils_main_menu_item(self) -> None:
        """Test method to click to "Pupils" main menu item from main page"""
        self.main_page.main_menu.click_to_pupils_item()
        self.pupils_page = PupilsPage(self.driver)
        self.pupils_page.assert_pupils_page_title()

    @allure.title('Opening "Graduates" page')
    @allure.step('Checking opening of "Graduates" page by clicking to main menu item from main page')
    def test_05_click_to_graduates_main_menu_item(self) -> None:
        """Test method to click to "Graduates" main menu item from main page"""
        self.main_page.main_menu.click_to_graduates_item()
        self.graduates_page = GraduatesPage(self.driver)
        self.graduates_page.assert_graduates_page_title()


@allure.feature('Gymnasium N7 website tests')
@allure.story('"Main" menu "One window" sub-menu items testing')
class TestClass03MainMenuOneWindowSubItems(BaseTestClass):
    """Test class for "Main" menu "One window" sub-menu items testing"""

    @allure.title('Opening "Schedule" page')
    @allure.step('Checking opening of "Schedule" page by clicking to "Main" menu "One window" sub-menu '
                 'item "Schedule" from main page')
    def test_01_click_to_one_window_sub_menu_item_schedule(self) -> None:
        """Test method to click to "Main" menu "One window" sub-menu item "Schedule" from main page"""
        self.main_page.main_menu.one_window_sub_menu.click_to_schedule_item()
        self.schedule_page = SchedulePage(self.driver)
        self.schedule_page.assert_schedule_page_title()

    @allure.title('Opening "Procedures" page')
    @allure.step('Checking opening of "Procedures" page by clicking to "Main" menu "One window" sub-menu '
                 'item "Procedures" from main page')
    def test_02_click_to_one_window_sub_menu_item_procedures(self) -> None:
        """Test method to click to "Main" menu "One window" sub-menu item "Procedures" from main page"""
        self.main_page.main_menu.one_window_sub_menu.click_to_procedures_item()
        self.procedures_page = ProceduresPage(self.driver)
        self.procedures_page.assert_procedures_page_title()


@allure.feature('Gymnasium N7 website tests')
@allure.story('"Main" menu "About" sub-menu items testing')
class TestClass04MainMenuAboutSubItems(BaseTestClass):
    """Test class for "Main" menu "About" sub-menu items testing"""

    @allure.title('Opening "Goals and tasks" page')
    @allure.step('Checking opening of "Goals and tasks" page by clicking to "Main" menu "About" sub-menu '
                 'item "Goals and tasks" from main page')
    def test_01_click_to_about_sub_menu_item_goals_and_tasks(self) -> None:
        """Test method to click to "Main" menu "About" sub-menu item "Goals and tasks" from main page"""
        self.main_page.main_menu.about_sub_menu.click_to_goals_and_tasks_item()
        self.goals_and_tasks_page = GoalsAndTasksPage(self.driver)
        self.goals_and_tasks_page.assert_goals_and_tasks_page_title()

    @allure.title('Opening "History and traditions" page')
    @allure.step('Checking opening of "History and traditions" page by clicking to "Main" menu "About" sub-menu '
                 'item "History and traditions" from main page')
    def test_02_click_to_about_sub_menu_item_history_and_traditions(self) -> None:
        """Test method to click to "Main" menu "About" sub-menu item "History and traditions" from main page"""
        self.main_page.main_menu.about_sub_menu.click_to_history_and_traditions_item()
        self.history_and_traditions_page = HistoryAndTraditionsPage(self.driver)
        self.history_and_traditions_page.assert_history_and_traditions_page_title()

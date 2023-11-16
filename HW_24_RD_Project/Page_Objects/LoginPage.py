from HW_24_RD_Project.Page_Objects.BasePage import BasePage
from HW_24_RD_Project.Helpers.Locators import LoginPageLocators


class LoginPage(BasePage):
    """Class LoginPage extends BasePage (Design pattern Page Object)"""

    def __init__(self, driver) -> None:
        """Constructor for class LoginPage"""
        super().__init__(driver)
        self.__expected_title_of_login_box = 'Login'
        self.__login = 'a.beaverg@gmail.com'
        self.__password = 'Test1234!'
        self.__expected_part_of_text_after_login = 'Alexey Bobrikov'

    def __get_title_of_login_box(self) -> str:
        """Method to get title of login page"""
        return self.driver.find_element(*LoginPageLocators.TITLE_OF_LOGIN_BOX).text

    def assert_title(self) -> None:
        """Method to assert title"""
        assert self.__expected_title_of_login_box, self.__get_title_of_login_box()

    def login_action(self) -> None:
        """Method to login"""
        self.driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(self.__login)
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(self.__password)
        self.driver.find_element(*LoginPageLocators.BUTTON_LOGIN).click()

    def __get_message(self) -> str:
        """Method to get message after login"""
        return self.driver.find_element(*LoginPageLocators.TEXT_AFTER_LOGIN).text

    def assert_login(self) -> None:
        """Method to assert login"""
        assert self.__expected_part_of_text_after_login in self.__get_message()

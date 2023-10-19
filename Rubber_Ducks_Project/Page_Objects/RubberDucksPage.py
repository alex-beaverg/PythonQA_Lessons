from Rubber_Ducks_Project.Page_Objects.BasePage import BasePage
from Rubber_Ducks_Project.Helpers.Locators import RubberDucksPageLocators


class RubberDucksPage(BasePage):
    """Class RubberDucksPage extends BasePage (Design pattern Page Object)"""

    def __init__(self, driver) -> None:
        """Constructor for class RubberDucksPage"""
        super().__init__(driver)
        self.__rubber_ducks_title = 'Rubber Ducks'
        self.__all_ducks_before_sort = []
        self.__ducks_names_before_sort = []
        self.__all_ducks_after_sort = []
        self.__ducks_names_after_sort = []
        self.__expected_text_sale = 'SALE'

    def assert_title(self) -> None:
        """Method to assert title"""
        assert self.__rubber_ducks_title, self.__get_title()

    def sort_ducks_by_name(self) -> None:
        """Method to sort ducks by name"""
        self.driver.find_element(*RubberDucksPageLocators.BUTTON_SORT_BY_NAME).click()

    def assert_sorting_by_name(self) -> None:
        """Method to assert sorting ducks by name"""
        self.__all_ducks_before_sort = self.driver.find_elements(*RubberDucksPageLocators.DUCK)
        for duck in self.__all_ducks_before_sort:
            self.__ducks_names_before_sort.append(duck.text)
        self.__ducks_names_before_sort.sort()
        self.__all_ducks_after_sort = self.driver.find_elements(*RubberDucksPageLocators.DUCK)
        for duck in self.__all_ducks_after_sort:
            self.__ducks_names_after_sort.append(duck.text)
        assert self.__ducks_names_after_sort, self.__ducks_names_before_sort

    def __get_sale(self) -> str:
        """Method to get sticker 'SALE'"""
        return self.driver.find_element(*RubberDucksPageLocators.STICKER_SALE).text

    def assert_getting_sale(self) -> None:
        """Method to assert getting sticker 'SALE'"""
        assert self.__expected_text_sale, self.__get_sale()

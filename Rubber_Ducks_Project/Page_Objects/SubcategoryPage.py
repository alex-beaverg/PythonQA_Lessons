from Rubber_Ducks_Project.Page_Objects.BasePage import BasePage


class SubcategoryPage(BasePage):
    """Class SubcategoryPage"""

    def __init__(self, driver) -> None:
        """Constructor for class RubberDucksPage"""
        super().__init__(driver)
        self.__subcategory_title = 'Subcategory'

    def assert_title(self) -> None:
        assert self.__subcategory_title, self.__get_title()

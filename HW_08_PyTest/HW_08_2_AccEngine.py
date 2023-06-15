# Homework 08, file 2 (2023.06.08)
# Accounting Engine

from HW_08_1_CalcEngine import CalcEngine


class AccountingEngine:
    """Docstring: Class AccountingEngine"""

    def __init__(self) -> None:
        """Docstring: Constructor for class AccountingEngine"""
        self.calc_engine = CalcEngine()

    def calc_se_taxes(self, income: (int, float)) -> (int, float):
        """Docstring: Method for calculation SE taxes"""
        se_taxes_percent = self.get_se_taxes_percent_from_gov()
        return self.calc_engine.percent(income, se_taxes_percent)

    def calc_devil_taxes_for_nonresident(self, income: (int, float)) -> (int, float):
        """Docstring: Method for calculation devil taxes"""
        devil_taxes_percent = self.get_se_taxes_percent_from_gov() * self.get_devil_coefficient_from_gov()
        return self.calc_engine.percent(income, devil_taxes_percent)

    def calc_light_taxes_for_gov_structures(self, income: (int, float)) -> (int, float):
        """Docstring: Method for calculation light taxes"""
        light_taxes_percent = self.get_se_taxes_percent_from_gov() * self.get_light_coefficient_from_gov()
        return self.calc_engine.percent(income, light_taxes_percent)

    def calc_special_taxes_for_under_gov_structures(self, income: (int, float)) -> (int, float):
        """Docstring: Method for calculation special taxes"""
        special_taxes_percent = self.calc_engine.sqrt(self.get_se_taxes_percent_from_gov())
        return self.calc_engine.percent(income, special_taxes_percent)

    def calc_free_taxes_for_elected_people(self, income: (int, float)) -> (int, float):
        """Docstring: Method for calculation free taxes"""
        free_taxes_percent = self.get_free_taxes_percent_from_gov()
        return self.calc_engine.percent(income, free_taxes_percent)

    def calc_killable_taxes_for_unique_people(self, income: (int, float)) -> (int, float):
        """Docstring: Method for calculation killable taxes"""
        killable_taxes_percent = 100 - self.get_free_taxes_percent_from_gov()
        return self.calc_engine.percent(income, killable_taxes_percent)

    @staticmethod
    def get_se_taxes_percent_from_gov() -> int:
        """Docstring: Static method for get SE taxes percent"""
        return 16

    @staticmethod
    def get_devil_coefficient_from_gov() -> int:
        """Docstring: Static method for get devil coefficient"""
        return 5

    @staticmethod
    def get_light_coefficient_from_gov() -> float:
        """Docstring: Static method for get light coefficient"""
        return 0.2

    @staticmethod
    def get_free_taxes_percent_from_gov() -> float:
        """Docstring: Static method for get free taxes percent"""
        return 0.001

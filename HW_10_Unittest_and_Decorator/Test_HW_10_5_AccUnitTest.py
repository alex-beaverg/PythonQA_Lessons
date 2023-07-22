# Homework 10, file 5 (2023.06.15)
# Accounting Engine Tests (Unittest)

# Run with cmd-line from current files_for_classwork' folder:
#   All tests:
#       python -m unittest -v
# (Flag "-v" -> using for more information in console)

import unittest
from parameterized import parameterized

from HW_10_2_AccEngine import AccountingEngine


class TestAccountingEngine(unittest.TestCase):
    """Docstring: Test class (suite) TestAccountingEngine"""

    def setUp(self) -> None:
        """Docstring: SetUp method for test class TestAccountingEngine"""
        self.accounting_engine = AccountingEngine()

    def tearDown(self) -> None:
        """Docstring: TearDown method for test class TestAccountingEngine"""
        del self.accounting_engine

    @parameterized.expand([[800, 128], [0, 0], [1_000_000, 160_000]])
    def test_01_calc_se_taxes(self, income, expected_result) -> None:
        """Docstring: Parametrized test method for calculation SE taxes"""
        result = self.accounting_engine.calc_se_taxes(income)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: SE tax is incorrect!")

    @parameterized.expand([[800, 640], [0, 0], [1_000_000, 800_000]])
    def test_02_calc_devil_taxes(self, income, expected_result) -> None:
        """Docstring: Parametrized test method for calculation devil taxes"""
        result = self.accounting_engine.calc_devil_taxes_for_nonresident(income)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Devil tax is incorrect!")

    @parameterized.expand([[800, 25.6], [0, 0], [1_000_000, 32_000]])
    def test_03_calc_light_taxes(self, income, expected_result) -> None:
        """Docstring: Parametrized test method for calculation light taxes"""
        result = self.accounting_engine.calc_light_taxes_for_gov_structures(income)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Light tax is incorrect!")

    @parameterized.expand([[800, 32], [0, 0], [1_000_000, 40_000]])
    def test_04_calc_special_taxes(self, income, expected_result) -> None:
        """Docstring: Parametrized test method for calculation special taxes"""
        result = self.accounting_engine.calc_special_taxes_for_under_gov_structures(income)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Special tax is incorrect!")

    @parameterized.expand([[800, 0.008], [0, 0], [1_000_000, 10]])
    def test_05_calc_free_taxes(self, income, expected_result) -> None:
        """Docstring: Parametrized test method for calculation free taxes"""
        result = self.accounting_engine.calc_free_taxes_for_elected_people(income)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Free tax is incorrect!")

    @parameterized.expand([[800, 799.992], [0, 0], [1_000_000, 999_990]])
    def test_06_calc_killable_taxes(self, income, expected_result) -> None:
        """Docstring: Parametrized test method for calculation killable taxes"""
        result = self.accounting_engine.calc_killable_taxes_for_unique_people(income)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Killable tax is incorrect!")

    @parameterized.expand([16])
    def test_07_get_se_taxes_percent_from_gov(self, expected_result) -> None:
        """Docstring: Parametrized test method for get SE taxes percent from government"""
        se_taxes_percent = AccountingEngine.get_se_taxes_percent_from_gov()
        self.assertEqual(se_taxes_percent, expected_result, "[ASSERT MESSAGE]: Tax percent is incorrect!")

    @parameterized.expand([5])
    def test_08_get_devil_coefficient_from_gov(self, expected_result) -> None:
        """Docstring: Parametrized test method for get devil coefficient from government"""
        devil_coefficient = AccountingEngine.get_devil_coefficient_from_gov()
        self.assertEqual(devil_coefficient, expected_result, "[ASSERT MESSAGE]: Devil coefficient is incorrect!")

    @parameterized.expand([0.2])
    def test_09_get_light_coefficient_from_gov(self, expected_result) -> None:
        """Docstring: Parametrized test method for get light coefficient from government"""
        light_coefficient = AccountingEngine.get_light_coefficient_from_gov()
        self.assertEqual(light_coefficient, expected_result, "[ASSERT MESSAGE]: Light coefficient is incorrect!")

    @parameterized.expand([0.001])
    def test_10_get_free_taxes_percent_from_gov(self, expected_result) -> None:
        """Docstring: Parametrized test method for get free taxes percent from government"""
        free_taxes_percent = AccountingEngine.get_free_taxes_percent_from_gov()
        self.assertEqual(free_taxes_percent, expected_result, "[ASSERT MESSAGE]: Free coefficient is incorrect!")

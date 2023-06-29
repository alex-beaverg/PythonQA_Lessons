# Homework 10, file 4 (2023.06.15)
# Calculating Engine Tests (Unittest)

# Run with cmd-line from current files' folder:
#   All tests:
#       python -m unittest -v
# (Flag "-v" -> using for more information in console)

import unittest
from parameterized import parameterized

from HW_10_1_CalcEngine import CalcEngine


class TestCalcEngine(unittest.TestCase):
    """Docstring: Test class (suite) TestCalcEngine"""

    def setUp(self) -> None:
        """Docstring: SetUp method for test class TestCalcEngine"""
        self.calc_engine = CalcEngine()

    def tearDown(self) -> None:
        """Docstring: TearDown method for test class TestCalcEngine"""
        del self.calc_engine

    @parameterized.expand([[5, 9, 14], [15.3, 25.2, 40.5], [-5, -13, -18]])
    def test_01_add_method(self, a, b, expected_result) -> None:
        """Docstring: Parametrized test method for basic realization of method for addiction"""
        result = self.calc_engine.add(a, b)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Sum of two numbers is incorrect!")

    @parameterized.expand([[10, 12, 15, 37], [15.3, 25.2, 1.5, 42], [-5, -13, -12, -30]])
    def test_02_add_method_with_one_argument(self, a, b, c, expected_result) -> None:
        """Docstring: Parametrized test method for method overload for addiction"""
        self.calc_engine.add(a, b)
        result = self.calc_engine.add(c)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Sum of itself and number is incorrect!")

    @parameterized.expand([[10, 12, -2], [25.4, 12.2, 13.2], [-12, -15, 3]])
    def test_03_sub_method(self, a, b, expected_result) -> None:
        """Docstring: Parametrized test method for basic realization of method for subtraction"""
        result = self.calc_engine.sub(a, b)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Difference of numbers is incorrect!")

    @parameterized.expand([[10, 12, -2, 0], [25.4, 12.2, 13.2, 0], [-12, -15, 3, 0]])
    def test_04_sub_method_with_one_argument(self, a, b, c, expected_result) -> None:
        """Docstring: Parametrized test method for method overload for subtraction"""
        self.calc_engine.sub(a, b)
        result = self.calc_engine.sub(c)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Difference of itself and number is incorrect!")

    @parameterized.expand([[10, 12, 120], [5.5, 7.5, 41.25], [-10, 12, -120]])
    def test_05_mul_method(self, a, b, expected_result) -> None:
        """Docstring: Parametrized test method for basic realization of method for multiply"""
        result = self.calc_engine.mul(a, b)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Product of numbers is incorrect!")

    @parameterized.expand([[10, 12, 2, 240], [5.5, 7.5, 2, 82.5], [-10, 12, 2, -240]])
    def test_06_mul_method_with_one_argument(self, a, b, c, expected_result) -> None:
        """Docstring: Parametrized test method for method overload for multiply"""
        self.calc_engine.mul(a, b)
        result = self.calc_engine.mul(c)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Product of itself and number is incorrect!")

    @parameterized.expand([[100, 10, 10], [6.6, 3.3, 2], [-10, 5, -2]])
    def test_07_div_method(self, a, b, expected_result) -> None:
        """Docstring: Parametrized test method for basic realization of method for division"""
        result = self.calc_engine.div(a, b)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Quotient of numbers is incorrect!")

    @parameterized.expand([[100, 10, 10, 1], [6.6, 3.3, 2, 1], [-10, 5, -2, 1]])
    def test_08_div_method_with_one_argument(self, a, b, c, expected_result) -> None:
        """Docstring: Parametrized test method for method overload for division"""
        self.calc_engine.div(a, b)
        result = self.calc_engine.div(c)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Quotient of itself and number is incorrect!")

    @parameterized.expand([[100, 0], [15.5, 0], [-25, 0]])
    def test_09_div_method_by_zero(self, a, b) -> None:
        """Docstring: Parametrized test method for basic realization of method for division by zero"""
        with self.assertRaises(ZeroDivisionError):
            self.calc_engine.div(a, b)

    @parameterized.expand([[100, 10, 0], [15.5, 10, 0], [-25, 5, 0]])
    def test_10_div_method_by_zero_with_one_argument(self, a, b, c) -> None:
        """Docstring: Parametrized test method for method overload for division by zero"""
        self.calc_engine.div(a, b)
        with self.assertRaises(ZeroDivisionError):
            self.calc_engine.div(c)

    @parameterized.expand([[2, 2, 4], [6.0, 2.0, 36], [-10, 3, -1000]])
    def test_11_exp_method(self, a, b, expected_result) -> None:
        """Docstring: Parametrized test method for basic realization of method for exponentiation"""
        result = self.calc_engine.exp(a, b)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Result of exponentiation of numbers is incorrect!")

    @parameterized.expand([[2, 2, 2, 16], [6.0, 2.0, 2, 1296], [-10, 3, 2, 1_000_000]])
    def test_12_exp_method_with_one_argument(self, a, b, c, expected_result) -> None:
        """Docstring: Parametrized test method for method overload for exponentiation"""
        self.calc_engine.exp(a, b)
        result = self.calc_engine.exp(c)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Result of exponentiation of itself and number "
                                                  "is incorrect!")

    @parameterized.expand([[200, 20, 40], [500.5, 10.5, 52.5525], [-200, 20, -40]])
    def test_13_percent_method(self, a, b, expected_result) -> None:
        """Docstring: Parametrized test method for calculate percent method"""
        result = self.calc_engine.percent(a, b)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Percent is incorrect!")

    @parameterized.expand([[100, 10], [6.25, 2.5]])
    def test_14_sqrt_method(self, a, expected_result) -> None:
        """Docstring: Parametrized test method for calculate square root method"""
        result = self.calc_engine.sqrt(a)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Square root is incorrect!")

    @parameterized.expand([-10, -2.5])
    def test_15_sqrt_method_for_negative(self, a) -> None:
        """Docstring: Parametrized test method for calculate square root method for negative number"""
        with self.assertRaises(ValueError):
            self.calc_engine.sqrt(a)

# Homework 11, file 1 - (2023.06.29)
# Classwork
# CalcEngine and AccEngine Unittest are in HW_10_Unittest folder

import unittest
from parameterized import parameterized

# Data for BAD parametrize
data = [[10, 20, 30], [100, 200, 300], [1, 2, 3]]


class TestString(unittest.TestCase):
    """Docstring: Test class (suite) TestString"""

    def test_upper(self) -> None:
        """Docstring: Test Method test_upper()"""
        # 1A:
        input_string = 'foo'
        expected_result = 'FOO'
        # 2A:
        result = input_string.upper()
        # 3A:
        self.assertEqual(result, expected_result)

    def test_isupper_true(self) -> None:
        """Docstring: Test Method test_isupper_true()"""
        # 1A:
        input_string = 'FOO'
        # 2A:
        result = input_string.isupper()
        # 3A:
        self.assertTrue(result)

    # Example with decorator for skipping tests
    @unittest.skip('Skip reason written here')
    def test_isupper_false(self) -> None:
        """Docstring: Test Method test_isupper_false()"""
        # 1A:
        input_string = 'Foo'
        # 2A:
        result = input_string.isupper()
        # 3A:
        self.assertFalse(result)

    def test_split(self) -> None:
        """Docstring: Test Method test_split()"""
        # 1A:
        s = 'hello world'
        expected_result = ['hello', 'world']
        # 2A:
        result = s.split()
        # 3A:
        self.assertEqual(result, expected_result)

    def test_split_false(self) -> None:
        """Docstring: Test Method test_split_false()"""
        # 1A:
        s = 'hello world'
        # 3A (2A):
        with self.assertRaises(TypeError):
            s.split(2)

    # 1A -> before this class
    def test_parametrized_custom_bad(self) -> None:
        """Docstring: Test Method test_parametrized_custom_bad()"""
        for expected_result, a, b in data:
            # 2A:
            result = b - a
            # 3A:
            self.assertEqual(result, expected_result)

    # 1A -> in decorator:
    @parameterized.expand([[10, 20, 30], [100, 200, 301], [1, 2, 3]])
    def test_parametrized_custom_good(self, expected_result, a, b) -> None:
        """Docstring: Test Method test_parametrized_custom_good()"""
        # 2A:
        result = b - a
        # 3A:
        self.assertEqual(result, expected_result)

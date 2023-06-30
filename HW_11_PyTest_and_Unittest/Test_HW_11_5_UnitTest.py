# Homework 11, file 5 - (2023.06.29)
# Tests (Unittest)

import unittest
from parameterized import parameterized

from HW_11_PyTest_and_Unittest.HW_11_2_Functions import *


class TestFunctions(unittest.TestCase):
    """Docstring: Test class (suite) TestFunctions"""

    @parameterized.expand([[2, (8, 4, 2.83)], [3, (12, 9, 4.24)], [4, (16, 16, 5.66)]])
    def test_01_square_parameters_var1(self, side, expected_result) -> None:
        """Docstring: Parametrized test method for function for square parameters. Variant 1"""
        result = square_parameters_var1(side)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[2, (8, 4, 2.83)], [3, (12, 9, 4.24)], [4, (16, 16, 5.66)]])
    def test_02_square_parameters_var2(self, side, expected_result) -> None:
        """Docstring: Parametrized test method for function for square parameters. Variant 2"""
        result = square_parameters_var2(side)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5, [1, 1, 2, 3]],
                           [[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 15, [1, 1, 2, 3, 5, 8, 13]],
                           [[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 56, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]]])
    def test_03_list_from_list_with_elements_less_than_number_var1(self, lst, number, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new list with elements
           less than number. Variant 1"""
        result = list_from_list_with_elements_less_than_number_var1(lst, number)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5, [1, 1, 2, 3]],
                           [[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 15, [1, 1, 2, 3, 5, 8, 13]],
                           [[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 56, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]]])
    def test_04_list_from_list_with_elements_less_than_number_var2(self, lst, number, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new list with elements
           less than number. Variant 2"""
        result = list_from_list_with_elements_less_than_number_var2(lst, number)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], True, [1, 1, 2, 3, 5, 8, 13]],
                           [[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], False, [1, 2, 3, 5, 8, 13]]])
    def test_05_intersection_of_lists_var1(self, lst1, lst2, not_unique, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new list with intersection
           of two lists. Variant 1"""
        result = intersection_of_lists_var1(lst1, lst2, not_unique)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], True, [1, 1, 2, 3, 5, 8, 13]],
                           [[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], False, [1, 2, 3, 5, 8, 13]]])
    def test_06_intersection_of_lists_var2(self, lst1, lst2, not_unique, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new list with intersection
           of two lists. Variant 2"""
        result = intersection_of_lists_var2(lst1, lst2, not_unique)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
                            {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}, True,
                            {'four': 4, 'five': 5, 'six': 60, 'seven': 70, 'eight': 80,
                             'one': 1, 'two': 2, 'three': 3}],
                           [{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
                            {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}, False,
                            {'one': 1, 'two': 2, 'three': 3, 'four': 40, 'five': 50, 'six': 60,
                             'seven': 70, 'eight': 80}]])
    def test_07_union_of_dicts_var1(self, dict1, dict2, first_into_second, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new dict with union of two dicts. Variant 1"""
        result = union_of_dicts_var1(dict1, dict2, first_into_second)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
                            {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}, True,
                            {'four': 4, 'five': 5, 'six': 60, 'seven': 70, 'eight': 80,
                             'one': 1, 'two': 2, 'three': 3}],
                           [{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
                            {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}, False,
                            {'one': 1, 'two': 2, 'three': 3, 'four': 40, 'five': 50, 'six': 60,
                             'seven': 70, 'eight': 80}]])
    def test_08_union_of_dicts_var2(self, dict1, dict2, first_into_second, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new dict with union of two dicts. Variant 2"""
        result = union_of_dicts_var2(dict1, dict2, first_into_second)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
                            {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}, True,
                            {'four': 4, 'five': 5, 'six': 60, 'seven': 70, 'eight': 80,
                             'one': 1, 'two': 2, 'three': 3}],
                           [{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
                            {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}, False,
                            {'one': 1, 'two': 2, 'three': 3, 'four': 40, 'five': 50, 'six': 60,
                             'seven': 70, 'eight': 80}]])
    def test_09_union_of_dicts_var3(self, dict1, dict2, first_into_second, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new dict with union of two dicts. Variant 3"""
        result = union_of_dicts_var3(dict1, dict2, first_into_second)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
                            {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}, True,
                            {'four': 4, 'five': 5, 'six': 60, 'seven': 70, 'eight': 80,
                             'one': 1, 'two': 2, 'three': 3}],
                           [{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
                            {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}, False,
                            {'one': 1, 'two': 2, 'three': 3, 'four': 40, 'five': 50, 'six': 60,
                             'seven': 70, 'eight': 80}]])
    def test_10_union_of_dicts_var4(self, dict1, dict2, first_into_second, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new dict with union of two dicts. Variant 4"""
        result = union_of_dicts_var4(dict1, dict2, first_into_second)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['gig', True], ['git', False]])
    def test_11_is_palindrome_var1(self, string, expected_result) -> None:
        """Docstring: Parametrized test method for function to check string for palindrome. Variant 1"""
        result = is_palindrome_var1(string)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['gig', True], ['git', False]])
    def test_12_is_palindrome_var2(self, string, expected_result) -> None:
        """Docstring: Parametrized test method for function to check string for palindrome. Variant 2"""
        result = is_palindrome_var2(string)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['gig', True], ['git', False]])
    def test_13_is_palindrome_var3(self, string, expected_result) -> None:
        """Docstring: Parametrized test method for function to check string for palindrome. Variant 3"""
        result = is_palindrome_var3(string)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['gig', True], ['git', False]])
    def test_14_is_palindrome_var4(self, string, expected_result) -> None:
        """Docstring: Parametrized test method for function to check string for palindrome. Variant 4"""
        result = is_palindrome_var4(string)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['1,2,3,4,5,6,7', 'list', [1, 2, 3, 4, 5, 6, 7]], ['1,2,3,4,5', 'tuple', (1, 2, 3, 4, 5)]])
    def test_15_numbers_to_iterable_var1(self, numbers, result_as, expected_result) -> None:
        """Docstring: Parametrized test method for function to return list or tuple from string
           with numbers. Variant 1"""
        result = numbers_to_iterable_var1(numbers, result_as)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['1,2,3,4,5,6,7', 'list', [1, 2, 3, 4, 5, 6, 7]], ['1,2,3,4,5', 'tuple', (1, 2, 3, 4, 5)]])
    def test_16_numbers_to_iterable_var2(self, numbers, result_as, expected_result) -> None:
        """Docstring: Parametrized test method for function to return list or tuple from string
           with numbers. Variant 2"""
        result = numbers_to_iterable_var2(numbers, result_as)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 2, 3, 4, 5], [1, 5]], [[10], [10, 10]], [[], []]])
    def test_17_first_and_last_numbers_from_list_var1(self, income_list, expected_result) -> None:
        """Docstring: Parametrized test method for function to return list with first and last elements of
           income list. Variant 1"""
        result = first_and_last_numbers_from_list_var1(income_list)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 2, 3, 4, 5], [1, 5]], [[10], [10, 10]], [[], []]])
    def test_18_first_and_last_numbers_from_list_var2(self, income_list, expected_result) -> None:
        """Docstring: Parametrized test method for function to return list with first and last elements of
           income list. Variant 2"""
        result = first_and_last_numbers_from_list_var2(income_list)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['project.py', 'py'], ['python.lib.org', 'org'],
                           ['this_is_folder', "Filename doesn't contain extension"]])
    def test_19_extension_from_filename_var1(self, filename, expected_result) -> None:
        """Docstring: Parametrized test method for function to return extension from filename. Variant 1"""
        result = extension_from_filename_var1(filename)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['project.py', 'py'], ['python.lib.org', 'org'],
                           ['this_is_folder', "Filename doesn't contain extension"]])
    def test_20_extension_from_filename_var2(self, filename, expected_result) -> None:
        """Docstring: Parametrized test method for function to return extension from filename. Variant 2"""
        result = extension_from_filename_var2(filename)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 8, 21, 12, 5, 2, 3, 4, 88, 45, 100, 237, 101, 102, 103, 104],
                            [8, 12, 2, 4, 88, 100]], [[1, 8, 21, 12, 237, 5, 2, 3], [8, 12]]])
    def test_21_even_numbers_from_list_var1(self, income_list, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new list with even numbers from
           income list. Variant 1"""
        result = even_numbers_from_list_var1(income_list)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 8, 21, 12, 5, 2, 3, 4, 88, 45, 100, 237, 101, 102, 103, 104],
                            [8, 12, 2, 4, 88, 100]], [[1, 8, 21, 12, 237, 5, 2, 3], [8, 12]]])
    def test_22_even_numbers_from_list_var2(self, income_list, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new list with even numbers from
           income list. Variant 2"""
        result = even_numbers_from_list_var2(income_list)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [21, 34, 55, 89]],
                           [[1, 8, 21, 12, 237, 5, 2, 3], [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [12, 237]]])
    def test_23_difference_of_lists_var1(self, income_lst1, income_lst2, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new list with difference
           of two lists. Variant 1"""
        result = difference_of_lists_var1(income_lst1, income_lst2)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([[[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [21, 34, 55, 89]],
                           [[1, 8, 21, 12, 237, 5, 2, 3], [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [12, 237]]])
    def test_24_difference_of_lists_var2(self, income_lst1, income_lst2, expected_result) -> None:
        """Docstring: Parametrized test method for function to return new list with difference
           of two lists. Variant 2"""
        result = difference_of_lists_var2(income_lst1, income_lst2)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['.', ['HW_11_1_Classwork.py', 'HW_11_2_Functions.py', 'HW_11_3_Actions.py',
                                  'Test_HW_11_4_PyTest.py', 'Test_HW_11_5_UnitTest.py']]])
    def test_25_files_from_dir_var1(self, path, expected_result) -> None:
        """Docstring: Parametrized test method for function to return list with files in directory. Variant 1"""
        result = files_from_dir_var1(path)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

    @parameterized.expand([['.', ['HW_11_1_Classwork.py', 'HW_11_2_Functions.py', 'HW_11_3_Actions.py',
                                  'Test_HW_11_4_PyTest.py', 'Test_HW_11_5_UnitTest.py']]])
    def test_26_files_from_dir_var2(self, path, expected_result) -> None:
        """Docstring: Parametrized test method for function to return list with files in directory. Variant 2"""
        result = files_from_dir_var2(path)
        self.assertEqual(result, expected_result, "[ASSERT MESSAGE]: Function does not work correctly!")

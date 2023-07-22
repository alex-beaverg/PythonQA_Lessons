# Homework 11, file 2 - (2023.06.29)
# Functions

import math
import os


# Task 1 --------------------------------------------------------------------------------------------------------------
def square_parameters_var1(income_side: (int, float)) -> tuple:
    """Docstring: Function for square parameters. Variant 1"""
    square_perimeter = income_side * 4
    square_square = income_side ** 2
    square_diagonal = round(math.sqrt(2) * income_side, 2)
    result = (square_perimeter, square_square, square_diagonal)
    return result


def square_parameters_var2(income_side: (int, float)) -> tuple:
    """Docstring: Function for square parameters. Variant 2"""
    return income_side * 4, income_side ** 2, round(math.sqrt(2) * income_side, 2)


# Task 2 --------------------------------------------------------------------------------------------------------------
def list_from_list_with_elements_less_than_number_var1(income_list: list, income_number: int) -> list:
    """Docstring: Function to return new list with elements less than number. Variant 1"""
    result = []
    for element in income_list:
        if element < income_number:
            result.append(element)
    return result


def list_from_list_with_elements_less_than_number_var2(income_list: list, income_number: int) -> list:
    """Docstring: Function to return new list with elements less than number. Variant 2"""
    return [element for element in income_list if element < income_number]


# Task 3 --------------------------------------------------------------------------------------------------------------
def intersection_of_lists_var1(income_list1: list, income_list2: list, not_unique=True) -> list:
    """Docstring: Function to return new list with intersection of two lists. Variant 1"""
    result = []
    if not_unique:
        for element in income_list1:
            if element in income_list2:
                result.append(element)
    else:
        result = list(set(income_list1) & set(income_list2))
    return result


def intersection_of_lists_var2(income_lst1: list, income_lst2: list, not_unique=True) -> list:
    """Docstring: Function to return new list with intersection of two lists. Variant 2"""
    return [i for i in income_lst1 if i in income_lst2] if not_unique else list(set(income_lst1) & set(income_lst2))


# Task 4 --------------------------------------------------------------------------------------------------------------
def union_of_dicts_var1(income_dict1: dict, income_dict2: dict, first_into_second=True) -> dict:
    """Docstring: Function to return new dict with union of two dicts. Variant 1"""
    if first_into_second:
        result = income_dict2 | income_dict1
    else:
        result = income_dict1 | income_dict2
    return result


def union_of_dicts_var2(income_dict1: dict, income_dict2: dict, first_into_second=True) -> dict:
    """Docstring: Function to return new dict with union of two dicts. Variant 2"""
    if first_into_second:
        result = {**income_dict2, **income_dict1}
    else:
        result = {**income_dict1, **income_dict2}
    return result


def union_of_dicts_var3(income_dict1: dict, income_dict2: dict, first_into_second=True) -> dict:
    """Docstring: Function to return new dict with union of two dicts. Variant 3"""
    return income_dict2 | income_dict1 if first_into_second else income_dict1 | income_dict2


def union_of_dicts_var4(income_dict1: dict, income_dict2: dict, first_into_second=True) -> dict:
    """Docstring: Function to return new dict with union of two dicts. Variant 4"""
    return {**income_dict2, **income_dict1} if first_into_second else {**income_dict1, **income_dict2}


# Task 5 --------------------------------------------------------------------------------------------------------------
def is_palindrome_var1(string: str) -> bool:
    """Docstring: Function to check string for palindrome. Variant 1"""
    reversed_string = string[::-1]
    return string == reversed_string


def is_palindrome_var2(string: str) -> bool:
    """Docstring: Function to check string for palindrome. Variant 2"""
    reversed_string = ''.join(reversed(string))
    return string == reversed_string


def is_palindrome_var3(string: str) -> bool:
    """Docstring: Function to check string for palindrome. Variant 3"""
    return string == string[::-1]


def is_palindrome_var4(string: str) -> bool:
    """Docstring: Function to check string for palindrome. Variant 4"""
    return string == ''.join(reversed(string))


# Task 6 --------------------------------------------------------------------------------------------------------------
def numbers_to_iterable_var1(numbers: str, result_as='list') -> (list, tuple):
    """Docstring: Function to return list or tuple from string with numbers. Variant 1"""
    if result_as == 'tuple':
        result = tuple(map(int, numbers.split(',')))
    else:
        result = list(map(int, numbers.split(',')))
    return result


def numbers_to_iterable_var2(numbers: str, result_as='list') -> (list, tuple):
    """Docstring: Function to return list or tuple from string with numbers. Variant 2"""
    return tuple(map(int, numbers.split(','))) if result_as == 'tuple' else list(map(int, numbers.split(',')))


# Task 7 --------------------------------------------------------------------------------------------------------------
def first_and_last_numbers_from_list_var1(income_list: list) -> list:
    """Docstring: Function to return list with first and last elements of income list. Variant 1"""
    if len(income_list) > 0:
        first_element = income_list[0]
        last_element = income_list[len(income_list) - 1]
        result = [first_element, last_element]
    else:
        result = []
    return result


def first_and_last_numbers_from_list_var2(income_list: list) -> list:
    """Docstring: Function to return list with first and last elements of income list. Variant 2"""
    if len(income_list) > 0:
        return [income_list[0], income_list[len(income_list) - 1]]
    else:
        return []


# Task 8 --------------------------------------------------------------------------------------------------------------
class NotExtensionException(Exception):
    pass


def extension_from_filename_var1(filename: str) -> str:
    """Docstring: Function to return extension from filename. Variant 1"""
    if '.' in filename:
        result = filename[::-1][0:filename[::-1].find('.'):][::-1]
    else:
        try:
            raise NotExtensionException
        except NotExtensionException:
            result = "Filename doesn't contain extension"
    return result


def extension_from_filename_var2(filename: str) -> str:
    """Docstring: Function to return extension from filename. Variant 2"""
    if filename.find('.') != -1:
        return filename[::-1][0:filename[::-1].find('.'):][::-1]
    else:
        try:
            raise NotExtensionException
        except NotExtensionException:
            return "Filename doesn't contain extension"


# Task 9 --------------------------------------------------------------------------------------------------------------
def even_numbers_from_list_var1(income_list: list) -> list:
    """Docstring: Function to return new list with even numbers from income list. Variant 1"""
    result = []
    for element in income_list:
        if element == 237:
            break
        elif element % 2 == 0:
            result.append(element)
    return result


def even_numbers_from_list_var2(income_list: list) -> list:
    """Docstring: Function to return new list with even numbers from income list. Variant 2"""
    result = []
    for i in range(len(income_list)):
        if income_list[i] == 237:
            break
        elif income_list[i] % 2 == 0:
            result.append(income_list[i])
    return result


# Task 10 -------------------------------------------------------------------------------------------------------------
def difference_of_lists_var1(income_lst1: list, income_lst2: list) -> list:
    """Docstring: Function to return new list with difference of two lists. Variant 1"""
    result = []
    for element in income_lst1:
        if element not in income_lst2:
            result.append(element)
    return result


def difference_of_lists_var2(income_lst1: list, income_lst2: list) -> list:
    """Docstring: Function to return new list with difference of two lists. Variant 2"""
    return [elem for elem in income_lst1 if elem not in income_lst2]


# Task 11 -------------------------------------------------------------------------------------------------------------
def files_from_dir_var1(path: str) -> list:
    """Docstring: Function to return list with files_for_classwork in directory. Variant 1"""
    result = []
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                result.append(entry.name)
    return result


def files_from_dir_var2(path: str) -> list:
    """Docstring: Function to return list with files_for_classwork in directory. Variant 2"""
    result = []

    def files(file_path):
        for one_file in os.listdir(file_path):
            if os.path.isfile(os.path.join(file_path, one_file)):
                yield one_file

    for file in files(path):
        result.append(file)
    return result

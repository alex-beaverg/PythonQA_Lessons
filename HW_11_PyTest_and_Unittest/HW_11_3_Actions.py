# Homework 11, file 3 - (2023.06.29)
# Actions

from HW_11_PyTest_and_Unittest.HW_11_2_Functions import *

# Task 1 --------------------------------------------------------------------------------------------------------------
print("Task 1:")
square_side = 4
# Variant 1:
square_params1 = square_parameters_var1(square_side)
print(f'Variant 1: {square_params1}')
# Variant 2:
square_params2 = square_parameters_var2(square_side)
print(f'Variant 2: {square_params2}')
print()

# Task 2 --------------------------------------------------------------------------------------------------------------
print("Task 2:")
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = 5
# Variant 1:
list_from_lst1 = list_from_list_with_elements_less_than_number_var1(lst, number)
print(f'Variant 1: {list_from_lst1}')
# Variant 2:
list_from_lst2 = list_from_list_with_elements_less_than_number_var2(lst, number)
print(f'Variant 2: {list_from_lst2}')
print()

# Task 3 --------------------------------------------------------------------------------------------------------------
print("Task 3:")
lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Variant 1:
intersection_list1 = intersection_of_lists_var1(lst1, lst2)
print(f'Variant 1.1: {intersection_list1}')
intersection_list_unique_elements1 = intersection_of_lists_var1(lst1, lst2, False)
print(f'Variant 1.2: {intersection_list_unique_elements1}')
# Variant 2:
intersection_list2 = intersection_of_lists_var2(lst1, lst2)
print(f'Variant 2.1: {intersection_list2}')
intersection_list_unique_elements2 = intersection_of_lists_var2(lst1, lst2, False)
print(f'Variant 2.2: {intersection_list_unique_elements2}')
print()

# Task 4 --------------------------------------------------------------------------------------------------------------
print("Task 4:")
dct1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
dct2 = {'four': 40, 'five': 50, 'six': 60, 'seven': 70, 'eight': 80}
# Variant 1:
union_dict1 = union_of_dicts_var1(dct1, dct2)
print(f'Variant 1.1: {union_dict1}')
union_dict_second_into_first1 = union_of_dicts_var1(dct1, dct2, False)
print(f'Variant 1.2: {union_dict_second_into_first1}')
# Variant 2:
union_dict2 = union_of_dicts_var2(dct1, dct2)
print(f'Variant 2.1: {union_dict2}')
union_dict_second_into_first2 = union_of_dicts_var2(dct1, dct2, False)
print(f'Variant 2.2: {union_dict_second_into_first2}')
# Variant 3:
union_dict3 = union_of_dicts_var3(dct1, dct2)
print(f'Variant 3.1: {union_dict3}')
union_dict_second_into_first3 = union_of_dicts_var3(dct1, dct2, False)
print(f'Variant 3.2: {union_dict_second_into_first3}')
# Variant 4:
union_dict4 = union_of_dicts_var4(dct1, dct2)
print(f'Variant 4.1: {union_dict4}')
union_dict_second_into_first4 = union_of_dicts_var4(dct1, dct2, False)
print(f'Variant 4.2: {union_dict_second_into_first4}')
print()

# Task 5 --------------------------------------------------------------------------------------------------------------
print("Task 5:")
txt_true = 'gig'
txt_false = 'git'
# Variant 1:
is_palindrome_true1 = is_palindrome_var1(txt_true)
print(f'Variant 1.1: {is_palindrome_true1}')
is_palindrome_false1 = is_palindrome_var1(txt_false)
print(f'Variant 1.2: {is_palindrome_false1}')
# Variant 2:
is_palindrome_true2 = is_palindrome_var2(txt_true)
print(f'Variant 2.1: {is_palindrome_true2}')
is_palindrome_false2 = is_palindrome_var2(txt_false)
print(f'Variant 2.2: {is_palindrome_false2}')
# Variant 3:
is_palindrome_true3 = is_palindrome_var3(txt_true)
print(f'Variant 3.1: {is_palindrome_true3}')
is_palindrome_false3 = is_palindrome_var3(txt_false)
print(f'Variant 3.2: {is_palindrome_false3}')
# Variant 4:
is_palindrome_true4 = is_palindrome_var4(txt_true)
print(f'Variant 4.1: {is_palindrome_true4}')
is_palindrome_false4 = is_palindrome_var4(txt_false)
print(f'Variant 4.2: {is_palindrome_false4}')
print()

# Task 6 --------------------------------------------------------------------------------------------------------------
print("Task 6:")
string_of_numbers = '1,2,3,4,5,6,7,8,9'
# Variant 1:
list_from_string1 = numbers_to_iterable_var1(string_of_numbers)
print(f'Variant 1.1: {list_from_string1}')
tuple_from_string1 = numbers_to_iterable_var1(string_of_numbers, 'tuple')
print(f'Variant 1.2: {tuple_from_string1}')
# Variant 2:
list_from_string2 = numbers_to_iterable_var2(string_of_numbers)
print(f'Variant 2.1: {list_from_string2}')
tuple_from_string2 = numbers_to_iterable_var2(string_of_numbers, 'tuple')
print(f'Variant 2.2: {tuple_from_string2}')
print()

# Task 7 --------------------------------------------------------------------------------------------------------------
print("Task 7:")
first_list = [1, 2, 3, 4, 5]
second_list = [10]
third_list = []
# Variant 1:
list_from_first_list1 = first_and_last_numbers_from_list_var1(first_list)
print(f'Variant 1.1: {list_from_first_list1}')
list_from_second_list1 = first_and_last_numbers_from_list_var1(second_list)
print(f'Variant 1.2: {list_from_second_list1}')
list_from_third_list1 = first_and_last_numbers_from_list_var1(third_list)
print(f'Variant 1.3: {list_from_third_list1}')
# Variant 2:
list_from_first_list2 = first_and_last_numbers_from_list_var2(first_list)
print(f'Variant 2.1: {list_from_first_list2}')
list_from_second_list2 = first_and_last_numbers_from_list_var2(second_list)
print(f'Variant 2.2: {list_from_second_list2}')
list_from_third_list2 = first_and_last_numbers_from_list_var2(third_list)
print(f'Variant 2.3: {list_from_third_list2}')
print()

# Task 8 --------------------------------------------------------------------------------------------------------------
print("Task 8:")
first_filename = 'project.py'
second_filename = 'python.lib.org'
third_filename = 'this_is_folder'
# Variant 1:
extension_from_first_filename1 = extension_from_filename_var1(first_filename)
print(f'Variant 1.1: {extension_from_first_filename1}')
extension_from_second_filename1 = extension_from_filename_var1(second_filename)
print(f'Variant 1.2: {extension_from_second_filename1}')
extension_from_third_filename1 = extension_from_filename_var1(third_filename)
print(f'Variant 1.3: {extension_from_third_filename1}')
# Variant 2:
extension_from_first_filename2 = extension_from_filename_var2(first_filename)
print(f'Variant 2.1: {extension_from_first_filename2}')
extension_from_second_filename2 = extension_from_filename_var2(second_filename)
print(f'Variant 2.2: {extension_from_second_filename2}')
extension_from_third_filename2 = extension_from_filename_var2(third_filename)
print(f'Variant 2.3: {extension_from_third_filename2}')
print()

# Task 9 --------------------------------------------------------------------------------------------------------------
print("Task 9:")
some_list = [1, 8, 21, 12, 5, 2, 3, 4, 88, 45, 100, 237, 101, 102, 103, 104]
# Variant 1:
list_with_even_numbers1 = even_numbers_from_list_var1(some_list)
print(f'Variant 1: {list_with_even_numbers1}')
# Variant 2:
list_with_even_numbers2 = even_numbers_from_list_var2(some_list)
print(f'Variant 2: {list_with_even_numbers2}')
print()

# Task 10 -------------------------------------------------------------------------------------------------------------
print("Task 10:")
some_lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
some_lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Variant 1:
diff_list1 = difference_of_lists_var1(some_lst1, some_lst2)
print(f'Variant 1: {diff_list1}')
# Variant 2:
diff_list2 = difference_of_lists_var2(some_lst1, some_lst2)
print(f'Variant 2: {diff_list2}')
print()

# Task 11 -------------------------------------------------------------------------------------------------------------
print("Task 11:")
folder_path = '.'
# Variant 1:
list_of_files1 = files_from_dir_var1(folder_path)
print(f'Variant 1: {list_of_files1}')
# Variant 2:
list_of_files2 = files_from_dir_var2(folder_path)
print(f'Variant 2: {list_of_files2}')
print()

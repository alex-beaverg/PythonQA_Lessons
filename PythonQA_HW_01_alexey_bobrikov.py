# Homework 01 (2023.03.23)
# Task 1
def information() -> None:
    """Function for print information about me"""
    name = 'Alexey'
    surname = 'Bobrikov'
    patronymic = 'Valerievich'
    print('\nTASK 1')
    print('-' * 6)
    print(f'Hello! My full name is {surname} {name} {patronymic} ({surname} {name[0:1]}.{patronymic[0:1]}.)\n')


# Task 2
def variables() -> None:
    """Function for print all types variables"""
    vars_types = {'Number, int': 1,
                  'Number, float': 1.1,
                  'Boolean': "True",
                  'String': '"Text"',
                  'NoneType': "None",
                  'Sequence, List': "[1, 2, 3]",
                  'Sequence, Tuple': "(1, 2, 3)",
                  'Sequence, Range': "range(5)",
                  'Dictionary': "{'one': 1, 'two': 2, 'three': 3}",
                  'Set, Set': "{1, 2, 3}",
                  'Set, Frozenset': "{1, 2, 3}"}
    print('\nTASK 2')
    print('-' * 6)
    print('Variables what i know:')
    print(f'{"Type":20s} {"Example":35s}')
    for key, value in vars_types.items():
        print(f'{key:<20} {value:<35}')
    print()


# Task 3
def string_methods() -> None:
    """Function for print results of string methods"""
    print('\nTASK 3')
    print('-' * 6)
    print('Write your text, for example "hello my dear friends!!!":', end=' ')
    text = input()[:25]
    lng = len("-".join(text)) + 5
    lst = [('text.upper():', text.upper(), '- all letters in UPPERCASE'),
           ('text.lower()', text.lower(), '- all letters in lowercase'),
           ('text.title()', text.title(), '- all first letters in Uppercase'),
           ('text.capitalize()', text.capitalize(), '- one first letter in Uppercase'),
           ('text.swapcase()', text.swapcase(), '- invert register of all letters'),
           ('text.split()', str(text.split()), '- split by space'),
           ('text.find("a")', str(text.find("a")), '- return index of first "a" (-1 if not find)'),
           ('text.replace("e", "E")', text.replace("e", "E"), '- replace all "e" to "E"'),
           ('"-".join(text)', "-".join(text), '- symbol "-" between all letters in text'),
           ('text.islower()', str(text.islower()), '- True, if all letters in lowercase'),
           ('text.isupper()', str(text.isupper()), '- True, if all letters in UPPERCASE'),
           ('text.count("s")', str(text.count("s")), '- count "s" in text')]
    print('String methods (for the first 25 letters of your text):')
    for item in lst:
        print(f'{item[0]:30s} {item[1]:<{lng}s} {item[2]:55s}')
    print('...and many other methods\n')


# Task 4
def simple_calculations() -> None:
    """Function for print results of simple calculations"""
    print('\nTASK 4')
    print('-' * 6)
    print('Results of simple calculations:')
    print(f'10 + 10 = {10 + 10} | 10 - 10 = {10 - 10} | 10 * 10 = {10 * 10} | 10 / 10 = {10 / 10}')
    print(f'12 // 10 = {12 // 10} | 12 % 10 = {12 % 10} | 2 ** 4 = {2 ** 4}')
    a = 10
    a += 5
    print(f'a = 10, a += 5 => a = {a}')
    b = 10
    b -= 5
    print(f'b = 10, b -= 5 => b = {b}')
    print('a = 10, b = 0 => ', end='')
    a = 10
    b = 0
    if b == 0:
        print('a / b = "ZeroDivisionError: division by zero"')
    else:
        print(a / b)
    print(f'"Hel" + "lo" = "{"hel" + "lo"}" - Concatenation')
    print(f'"100" + "500" = "{"100" + "500"}" - Concatenation too')
    print(f'int("100") + int("500") = {int("100") + int("500")} - addition')


# Main program entry point
if __name__ == '__main__':
    print('\nHomework 01 (2023.03.23)')
    information()
    variables()
    string_methods()
    simple_calculations()

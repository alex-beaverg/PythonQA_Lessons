# Homework 02 (2023.03.30)
# Task 1 (extends Task 3 from Homework 01)

def string_methods() -> int:
    """Function for print results of string methods"""
    print('\nTASK 1 (extends Task 3 from Homework 01)')
    print('-' * 6)
    print('LOG_INFO: Print results of string methods')
    text = "Hello my dear Friends!!!"
    print('Text for examples: "Hello my dear Friends!!!":')
    print('-' * 46)
    lng = len("-".join(text)) + 5
    lst = [('text.upper():', text.upper(), '- all letters in UPPERCASE'),
           ('text.lower():', text.lower(), '- all letters in lowercase'),
           ('text.title():', text.title(), '- all first letters in Uppercase'),
           ('text.capitalize():', text.capitalize(), '- one first letter in Uppercase'),
           ('text.swapcase():', text.swapcase(), '- invert register of all letters'),
           ('text.split():', str(text.split()), '- split by space'),
           ('text.split(" ", 1):', str(text.split(" ", 1)), '- split by space 1 time'),
           ('text.find("a"):', str(text.find("a")), '- return index of first "a" (-1 if not find)'),
           ('text.rfind("F"):', str(text.rfind("F")), '- return index of first "F" from end (-1)'),
           ('text.replace("e", "E"):', text.replace("e", "E"), '- replace all "e" to "E"'),
           ('"-".join(text):', "-".join(text), '- symbol "-" between all letters in text'),
           ('text.islower():', str(text.islower()), '- True, if all letters in lowercase'),
           ('text.isupper():', str(text.isupper()), '- True, if all letters in UPPERCASE'),
           ('text.count("s"):', str(text.count("s")), '- count "s" in text'),
           ('text.index("F"):', str(text.index("F")), '- position of first letter "F"'),
           ('text.removeprefix("Hello"):', text.removeprefix("Hello"), '- remove "Hello" from start'),
           ('text.removesuffix("!!!"):', text.removesuffix("!!!"), '- remove "!!!" in the end'),
           ('text.startswidth("Hello"):', str(text.startswith("Hello")), '- True, if "Hello" is in start of text'),
           ('text.endswidth("Hi"):', str(text.endswith("Hi")), '- True, if "Hi" is in the end of text'),
           ('text.isdigit():', str(text.isdigit()), '- True, if all symbols are numbers'),
           ('text.isalpha():', str(text.isalpha()), '- True, if all symbols are letters'),
           ('text.isalnum():', str(text.isalnum()), '- True, if all symbols are numbers and letters'),
           ('text.istitle():', str(text.istitle()), '- True, if all first letters in Uppercase'),
           ('text.ljust(40, "-"):', text.ljust(40, "-"), '- fill with "-" in the end to 40 symbols'),
           ('text.rjust(40, "+"):', text.rjust(40, "+"), '- fill with "+" from start to 40 symbols'),
           ('text.center(40, "_"):', text.center(40, "_"), '- fill with "_" from start and end to 40 symbols'),
           ('text.strip():', text.strip(), '- remove spaces in start and end and all escape symbols'),
           ('text.strip("!"):', text.strip("!"), '- remove all "!" in start and end'),
           ('text.rstrip("!"):', text.rstrip("!"), '- remove all "!" in the end'),
           ('text.lstrip("H"):', text.lstrip("H"), '- remove all "H" in start'),
           ('text.rpartiotion("dear"):', str(text.rpartition("dear")), '- return tuple with 3 elements')]
    for item in lst:
        print(f'{item[0]:30s} {item[1]:{lng}s} {item[2]:60s}')
    print('-' * 8)
    print('Slicing:')
    print('-' * 8)
    lst_slice = [('text[1]:', text[1], '- get symbol in position 1'),
                 ('text[6:13]:', text[6:13], '- get symbols from pos.6 to pos.13'),
                 ('text[:10]:', text[:10], '- get symbols from pos.0 to pos.10'),
                 ('text[10:]:', text[10:], '- get symbols from pos.9 to end'),
                 ('text[-10:]:', text[-10:], '- get symbols from pos.-10 to end'),
                 ('text[1:-1]:', text[1:-1], '- get symbols from pos.1 to pos.-1'),
                 ('text[1:15:2]:', text[1:15:2], '- get symbols from pos.1 to pos.15 with step 2'),
                 ('text[12:5:-1]:', text[12:5:-1], '- get symbols from pos.12 to pos.5 with step -1'),
                 ('text[-4:-11:-1]:', text[-4:-11:-1], '- get symbols from pos.-5 to pos.-10 with step -1'),
                 ('text[::-1]:', text[::-1], '- get all text from end to start'),
                 ('text[::]:', text[::], '- get "copy" of text')]
    for item in lst_slice:
        print(f'{item[0]:20s} {item[1]:30s} {item[2]:55s}')
    return len(lst) + len(lst_slice)


# Task 2 (extends Task 1 from Homework 01)
class Person:
    """Class Person"""

    # Constructor
    def __init__(self) -> None:
        """Constructor for class Person"""
        print('LOG_INFO: Create person without parameters')
        self.__name = 'Unknown'
        self.__surname = 'Unknown'
        self.__patronymic = 'Unknown'

    # Setters
    def set_name(self, name: str) -> None:
        """Method to Set Name"""
        print(f'LOG_INFO: Set name with value = {name}')
        self.__name = name

    def set_surname(self, surname: str) -> None:
        """Method to Set Surname"""
        print(f'LOG_INFO: Set surname with value = {surname}')
        self.__surname = surname

    def set_patronymic(self, patronymic: str) -> None:
        """Method to Set Patronymic"""
        print(f'LOG_INFO: Set patronymic with value = {patronymic}')
        self.__patronymic = patronymic

    # Getters
    def get_name(self) -> str:
        """Method to Get Name"""
        print(f'LOG_INFO: Get name with value = {self.__name}')
        return self.__name

    def get_surname(self) -> str:
        """Method to Get Surname"""
        print(f'LOG_INFO: Get surname with value = {self.__surname}')
        return self.__surname

    def get_patronymic(self) -> str:
        """Method to Get Patronymic"""
        print(f'LOG_INFO: Get patronymic with value = {self.__patronymic}')
        return self.__patronymic

    # Other methods
    def get_surname_with_initials(self) -> str:
        """Method to Get Surname with Initials"""
        print('LOG_INFO: Get Surname with Initials')
        return f'{self.__surname} {self.__name[0:1]}.{self.__patronymic[0:1]}.'

    def get_all_information(self) -> str:
        """Method to Get all Information about Person"""
        print('LOG_INFO: Get all Information about Person')
        return f'{self.__surname} {self.__name} {self.__patronymic}'

    def print_all_information(self) -> None:
        """Method to Print all Information about Person"""
        print('LOG_INFO: Print all Information about Person')
        print(f'Surname: {self.__surname}')
        print(f'Name: {self.__name}')
        print(f'Patronymic: {self.__patronymic}')


class Student(Person):
    """Class Student extends class Person"""

    # Constructor
    def __init__(self) -> None:
        """Constructor for class Student"""
        super().__init__()
        print('LOG_INFO: Create student with default parameters')
        self.__university = 'IT STEP'
        self.__group_id = 'QA1823'

    # Setters
    def set_university(self, university: str) -> None:
        """Method to Set University"""
        print(f'LOG_INFO: Set university with value = {university}')
        self.__university = university

    def set_group_id(self, group_id: str) -> None:
        """Method to Set Group ID"""
        print(f'LOG_INFO: Set group_id with value = {group_id}')
        self.__group_id = group_id

    # Getters
    def get_university(self) -> str:
        """Method to Get University"""
        print(f'LOG_INFO: Get university with value = {self.__university}')
        return self.__university

    def get_group_id(self) -> str:
        """Method to Get Group ID"""
        print(f'LOG_INFO: Get group_id with value = {self.__group_id}')
        return self.__group_id

    # Other methods
    def get_all_information(self) -> str:
        """Method to Get all Information about Student"""
        print('LOG_INFO: Get all Information about Student')
        return f'{super().get_all_information()} is studying at the {self.__university} in the {self.__group_id} group'

    def print_all_information(self) -> None:
        """Method to Print all Information about Student"""
        print('LOG_INFO: Print all Information about Student')
        super().print_all_information()
        print(f'University: {self.__university}')
        print(f'Group: {self.__group_id}')


def task_2_launcher() -> None:
    """Function for launch Task 2"""
    print('\nTASK 2 (extends Task 1 from Homework 01)')
    print('-' * 6)
    print('LOG_INFO: Function for launch Task 2')
    me = Student()
    print(me.get_all_information())
    me.set_name('Alexey')
    print(me.get_name())
    me.set_surname('Bobrikov')
    print(me.get_surname())
    me.set_patronymic('Valerievich')
    print(me.get_patronymic())
    print(me.get_university())
    print(me.get_group_id())
    print(me.get_surname_with_initials())
    print(me.get_all_information())
    print(3 * '-')
    me.print_all_information()


# Main program entry point
if __name__ == '__main__':
    print('\nHomework 02 (2023.03.30)')
    string_methods()
    task_2_launcher()

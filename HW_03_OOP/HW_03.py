# Homework 03 (2023.04.06)
# Task 1

class Library:
    """Docstring: Class Library"""

    def __init__(self) -> None:
        """Docstring: Constructor for class Library"""
        print('LOG_INFO: Create library with empty list of books')
        self.__books = dict()

    def add_book(self, book) -> None:
        """Docstring: Method to add book to library"""
        print('LOG_INFO: Add book to library')
        self.__books[book.get_orders()["ID"]] = book.get_orders()

    def get_books(self) -> dict:
        """Docstring: Getter for book list"""
        return self.__books

    def print_summary_of_all_library(self) -> None:
        """Docstring: Function for print summary of all books in library"""
        print('LOG_INFO: Print summary of all books in library')
        print('List of books in library:')
        for book_info in self.__books.values():
            print(f'\tTitle: {book_info["Title"]:30s}Author: {book_info["Author"]:20s}ID: {book_info["ID"]}', end='\n')
        print()


class Book:
    """Docstring: Class Book"""

    def __init__(self, *args: (str, int, bool, dict)) -> None:
        """Docstring: Constructor for class Book"""
        print('LOG_INFO: Create book with parameters')
        self.__my_book = {
            'ID': self.__hash__(),
            'Title': args[0],
            'Author': args[1],
            'Pages': args[2],
            'Age rating': args[3],
            'Language': args[4],
            'Country': args[5],
            'Availability': args[6],
            'Preview': args[7]
        }

    def get_book(self) -> dict:
        """Docstring: Method to get book"""
        print('LOG_INFO: Get book')
        return self.__my_book

    def print_book_description(self) -> None:
        """Docstring: Function for print full book description"""
        print('LOG_INFO: Print full book description')
        print(f'{self.__my_book["Title"]} ({self.__my_book["Author"]}):')
        for key, value in self.__my_book.items():
            if key != 'Preview' and key != 'Title' and key != 'Author':
                print(f'\t{key + ":":15s}{value}')
        print()

    def print_first_three_pages_preview(self) -> None:
        """Docstring: Function for print preview of the first three pages"""
        print('LOG_INFO: Print preview of the first three pages')
        print(f'Preview pages of the book "{self.__my_book["Title"]}":')
        for string in self.__my_book['Preview']:
            print('\t' + string)
        print()


# Task 2 (extends Task 2 from Homework 02)
class Person:
    """Docstring: Class Person"""

    # Constructor
    def __init__(self) -> None:
        """Docstring: Constructor for class Person"""
        print('LOG_INFO: Create person without parameters')
        self.__name = 'Unknown'
        self.__surname = 'Unknown'
        self.__patronymic = 'Unknown'

    # Setters
    def set_name(self, name: str) -> None:
        """Docstring: Method to Set Name"""
        print(f'LOG_INFO: Set name with value = {name}')
        self.__name = name

    def set_surname(self, surname: str) -> None:
        """Docstring: Method to Set Surname"""
        print(f'LOG_INFO: Set surname with value = {surname}')
        self.__surname = surname

    def set_patronymic(self, patronymic: str) -> None:
        """Docstring: Method to Set Patronymic"""
        print(f'LOG_INFO: Set patronymic with value = {patronymic}')
        self.__patronymic = patronymic

    # Getters
    def get_name(self) -> str:
        """Docstring: Method to Get Name"""
        print(f'LOG_INFO: Get name with value = {self.__name}')
        return self.__name

    def get_surname(self) -> str:
        """Docstring: Method to Get Surname"""
        print(f'LOG_INFO: Get surname with value = {self.__surname}')
        return self.__surname

    def get_patronymic(self) -> str:
        """Docstring: Method to Get Patronymic"""
        print(f'LOG_INFO: Get patronymic with value = {self.__patronymic}')
        return self.__patronymic

    # Other methods
    def get_surname_with_initials(self) -> str:
        """Docstring: Method to Get Surname with Initials"""
        print('LOG_INFO: Get Surname with Initials')
        return f'{self.__surname} {self.__name[0:1]}.{self.__patronymic[0:1]}.'

    def get_all_information(self) -> str:
        """Docstring: Method to Get all Information about Person"""
        print('LOG_INFO: Get all Information about Person')
        return f'{self.__surname} {self.__name} {self.__patronymic}'

    def print_all_information(self) -> None:
        """Docstring: Method to Print all Information about Person"""
        print('LOG_INFO: Print all Information about Person')
        print(f'Surname: {self.__surname}')
        print(f'Name: {self.__name}')
        print(f'Patronymic: {self.__patronymic}')


class Student(Person):
    """Docstring: Class Student extends class Person"""

    # Constructor
    def __init__(self) -> None:
        """Docstring: Constructor for class Student"""
        super().__init__()
        print('LOG_INFO: Create student with default parameters')
        self.__university = 'IT STEP'
        self.__group_id = 'QA1823'

    # Setters
    def set_university(self, university: str) -> None:
        """Docstring: Method to Set University"""
        print(f'LOG_INFO: Set university with value = {university}')
        self.__university = university

    def set_group_id(self, group_id: str) -> None:
        """Docstring: Method to Set Group ID"""
        print(f'LOG_INFO: Set group_id with value = {group_id}')
        self.__group_id = group_id

    # Getters
    def get_university(self) -> str:
        """Docstring: Method to Get University"""
        print(f'LOG_INFO: Get university with value = {self.__university}')
        return f'"{self.__university}"'

    def get_group_id(self) -> str:
        """Docstring: Method to Get Group ID"""
        print(f'LOG_INFO: Get group_id with value = {self.__group_id}')
        return f'"{self.__group_id}"'

    # Other methods
    def get_all_information(self) -> str:
        """Docstring: Method to Get all Information about Student"""
        print('LOG_INFO: Get all Information about Student')
        if self.get_name() == 'Unknown' and self.get_surname() == 'Unknown' and self.get_patronymic() == 'Unknown':
            return '!!! Information is not set !!!'
        else:
            return f'{super().get_all_information()} is studying at the "{self.__university}" in ' \
                   f'the "{self.__group_id}" group'

    def print_all_information(self) -> None:
        """Docstring: Method to Print all Information about Student"""
        print('LOG_INFO: Print all Information about Student')
        if self.get_name() == 'Unknown' and self.get_surname() == 'Unknown' and self.get_patronymic() == 'Unknown':
            print('!!! Information is not set !!!')
        else:
            super().print_all_information()
            print(f'University: "{self.__university}"')
            print(f'Group: "{self.__group_id}"')


# Main program entry point
if __name__ == '__main__':
    print('\nHomework 03 (2023.04.06)')

    def task_1_launcher() -> None:
        """Docstring: Function for launch Task 1"""
        print('\nTASK 1')
        print('-' * 6)
        print('LOG_INFO: Function for launch Task 1')

        # Build a new library named 'my_lib':
        my_lib = Library()

        # Add books to 'my_lib':
        first_book = Book('Chook and Gek', 'Arcadii Gaidar', 150, 10, 'ru', 'Belarus', True,
                          ('Chook and Gek were brothers.',
                           'They received a telegram but quarreled.',
                           'And the story began...'))
        my_lib.add_book(first_book)
        primer_book = Book('Primer Book', 'Group of authors', 100, 3, 'en', 'US', False,
                           ('A - Apple.',
                            'B - Banana.',
                            'C - Cucumber.'))
        my_lib.add_book(primer_book)
        blue_book = Book('Blue Book', 'Blue Author', 666, 18, 'by', 'Belarus', True,
                         ('My name is Alexey and I am an alcoholic.',
                          'I really like to drink beer.',
                          'And I will be drink it every week!'))
        my_lib.add_book(blue_book)
        b_a_book = Book('Murder in the Front Row', 'Brian Lew', 272, 18, 'US', 'United States', True,
                        ('This is a story about roots of thrash metal.',
                         'It began at the Bay area in San Francisco.',
                         'It was in the early eighties...'))
        my_lib.add_book(b_a_book)
        about_mouse = Book('Pook the mouse', 'Steeve Edgard', 94, 6, 'UK', 'United Kingdom', False,
                           ('There lived a little mouse Pook.',
                            'She liked to fart very loudly.',
                            'So no one was friends with her...'))
        my_lib.add_book(about_mouse)

        # List of books in 'my_lib':
        my_lib.print_summary_of_all_library()

        # Details about every book in 'my_lib':
        first_book.print_book_description()
        primer_book.print_book_description()
        blue_book.print_book_description()
        b_a_book.print_book_description()
        about_mouse.print_book_description()

        # Preview pages of every book in 'my_lib':
        first_book.print_first_three_pages_preview()
        primer_book.print_first_three_pages_preview()
        blue_book.print_first_three_pages_preview()
        b_a_book.print_first_three_pages_preview()
        about_mouse.print_first_three_pages_preview()

    def task_2_launcher() -> None:
        """Docstring: Function for launch Task 2"""
        print('\nTASK 2')
        print('-' * 6)
        print('LOG_INFO: Function for launch Task 2')

        # About me:
        me = Student()
        print(me.get_all_information())
        me.set_surname('Bobrikov')
        print(me.get_surname())
        me.set_name('Alexey')
        print(me.get_name())
        me.set_patronymic('Valerievich')
        print(me.get_patronymic())
        print(me.get_university())
        print(me.get_group_id())
        print(me.get_surname_with_initials())
        print(me.get_all_information())
        print(3 * '-')
        me.print_all_information()
        print()

        # About Jim Carrey:
        my_friend = Student()
        print(my_friend.get_all_information())
        my_friend.set_name('Jim')
        print(my_friend.get_name())
        my_friend.set_patronymic('Eugene')
        print(my_friend.get_patronymic())
        my_friend.set_surname('Carrey')
        print(my_friend.get_surname())
        my_friend.set_university('Agincourt Collegiate Institute')
        my_friend.set_group_id('...and who knows')
        print(my_friend.get_university())
        print(my_friend.get_group_id())
        print(my_friend.get_surname_with_initials())
        print(my_friend.get_all_information())
        print(3 * '-')
        my_friend.print_all_information()
        print()

        # About somebody:
        somebody = Student()
        print(somebody.get_all_information())
        somebody.set_surname('Nedavaeva')
        print(somebody.get_surname())
        somebody.set_name('Leopolda')
        print(somebody.get_name())
        somebody.set_patronymic('Arnoldovna')
        print(somebody.get_patronymic())
        somebody.set_university('The School of Noble Maidens')
        somebody.set_group_id('Virgins')
        print(somebody.get_university())
        print(somebody.get_group_id())
        print(somebody.get_surname_with_initials())
        print(somebody.get_all_information())
        print(3 * '-')
        somebody.print_all_information()
        print()


    task_1_launcher()
    task_2_launcher()

# Homework 03 (2023.04.06)
# Task 1
class Library:
    """Class Library"""

    def __init__(self) -> None:
        """Constructor for class Library"""
        self.books = dict()

    def print_summary_of_all_library(self) -> None:
        """Function for print summary of all books in library"""
        print('List of books in library:')
        for book_info in self.books.values():
            print(f'\tTitle: {book_info["Title"]:30s}Author: {book_info["Author"]:20s}ID: {book_info["ID"]}', end='\n')
        print()


class Book:
    """Class Book"""

    def __init__(self, *args: (str, int, bool, dict)) -> None:
        """Constructor for class Book"""
        self.my_book = {
            'ID': self.__hash__(),
            'Title': args[0],
            'Author': args[1],
            'Pages': args[2],
            'Age rating': args[3],
            'Language': args[4],
            'Country': args[5],
            'Availability': args[6],
            'Preview': args[8]
        }
        args[7][f'{self.my_book["ID"]}'] = self.my_book

    def print_book_description(self) -> None:
        """Function for print full book description"""
        print(f'{self.my_book["Title"]} ({self.my_book["Author"]}):')
        for key, value in self.my_book.items():
            if key != 'Preview' and key != 'Title' and key != 'Author':
                print(f'\t{key + ":":15s}{value}')
        print()

    def print_first_three_pages_preview(self) -> None:
        """Function for print preview of the first three pages"""
        print(f'Preview pages of the book "{self.my_book["Title"]}":')
        for string in self.my_book['Preview']:
            print('\t' + string)
        print()


# Task 2 (extends Task 2 from Homework 02)
class Person:
    """Class Person"""

    # Constructor
    def __init__(self) -> None:
        """Constructor for class Person"""
        self.name = 'Unknown'
        self.surname = 'Unknown'
        self.patronymic = 'Unknown'

    # Setters
    def set_name(self, name: str) -> None:
        """Method to Set Name"""
        self.name = name

    def set_surname(self, surname: str) -> None:
        """Method to Set Surname"""
        self.surname = surname

    def set_patronymic(self, patronymic: str) -> None:
        """Method to Set Patronymic"""
        self.patronymic = patronymic

    # Getters
    def get_name(self) -> str:
        """Method to Get Name"""
        return self.name

    def get_surname(self) -> str:
        """Method to Get Surname"""
        return self.surname

    def get_patronymic(self) -> str:
        """Method to Get Patronymic"""
        return self.patronymic

    # Other methods
    def get_surname_with_initials(self) -> str:
        """Method to Get Surname with Initials"""
        return f'{self.surname} {self.name[0:1]}.{self.patronymic[0:1]}.'

    def get_all_information(self) -> str:
        """Method to Get all Information about Person"""
        return f'{self.surname} {self.name} {self.patronymic}'

    def print_all_information(self) -> None:
        """Method to Print all Information about Person"""
        print(f'Surname: {self.surname}')
        print(f'Name: {self.name}')
        print(f'Patronymic: {self.patronymic}')


class Student(Person):
    """Class Student extends class Person"""

    # Constructor
    def __init__(self) -> None:
        """Constructor for class Student"""
        super().__init__()
        self.university = 'IT STEP'
        self.group_id = 'QA1823'

    # Setters
    def set_university(self, university: str) -> None:
        """Method to Set University"""
        self.university = university

    def set_group_id(self, group_id: str) -> None:
        """Method to Set Group ID"""
        self.group_id = group_id

    # Getters
    def get_university(self) -> str:
        """Method to Get University"""
        return f'"{self.university}"'

    def get_group_id(self) -> str:
        """Method to Get Group ID"""
        return f'"{self.group_id}"'

    # Other methods
    def get_all_information(self) -> str:
        """Method to Get all Information about Student"""
        if self.name == 'Unknown' and self.surname == 'Unknown' and self.patronymic == 'Unknown':
            return '!!! Information is not set !!!'
        else:
            return f'{super().get_all_information()} is studying at the "{self.university}" in ' \
                   f'the "{self.group_id}" group'

    def print_all_information(self) -> None:
        """Method to Print all Information about Student"""
        if self.name == 'Unknown' and self.surname == 'Unknown' and self.patronymic == 'Unknown':
            print('!!! Information is not set !!!')
        else:
            super().print_all_information()
            print(f'University: "{self.university}"')
            print(f'Group: "{self.group_id}"')


# Main program entry point
if __name__ == '__main__':
    def task_1_launcher() -> None:
        """Function for launch Task 1"""
        print('\nTASK 1')
        print('-' * 6)

        # Build a new library named 'my_lib':
        my_lib = Library()

        # Add books to 'my_lib':
        first_book = Book('Chook and Gek', 'Arcadii Gaidar', 150, 10, 'ru', 'Belarus', True, my_lib.books,
                          ('Chook and Gek were brothers.',
                           'They received a telegram but quarreled.',
                           'And the story began...'))
        primer_book = Book('Primer Book', 'Group of authors', 100, 3, 'en', 'US', False, my_lib.books,
                           ('A - Apple.',
                            'B - Banana.',
                            'C - Cucumber.'))
        blue_book = Book('Blue Book', 'Blue Author', 666, 18, 'by', 'Belarus', True, my_lib.books,
                         ('My name is Alexey and I am an alcoholic.',
                          'I really like to drink beer.',
                          'And I will be drink it every week!'))
        b_a_book = Book('Murder in the Front Row', 'Brian Lew', 272, 18, 'US', 'United States', True, my_lib.books,
                        ('This is a story about roots of thrash metal.',
                         'It began at the Bay area in San Francisco.',
                         'It was in the early eighties...'))
        about_mouse = Book('Pook the mouse', 'Steeve Edgard', 94, 6, 'UK', 'United Kingdom', False, my_lib.books,
                           ('There lived a little mouse Pook.',
                            'She liked to fart very loudly.',
                            'So no one was friends with her...'))

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
        """Function for launch Task 2"""
        print('\nTASK 2')
        print('-' * 6)

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

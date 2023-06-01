# Homework 06 (2023.05.25)

class Person:
    """Docstring: Class Person"""
    def __init__(self, name, second_name, birth_year):
        """Docstring: Constructor for class Person"""
        self.__name = name
        self.__second_name = second_name
        self.__birth_year = birth_year

    def get_name(self):
        """Docstring: Getter for field 'name'"""
        return self.__name

    def get_second_name(self):
        """Docstring: Getter for field 'second_name'"""
        return self.__second_name

    def get_birth_year(self):
        """Docstring: Getter for field 'birth_year'"""
        return self.__birth_year

    def set_name(self, name):
        """Docstring: Setter for field 'name'"""
        self.__name = name

    def set_second_name(self, second_name):
        """Docstring: Setter for field 'second_name'"""
        self.__second_name = second_name

    def set_birth_year(self, birth_year):
        """Docstring: Setter for field 'birth_year'"""
        self.__birth_year = birth_year

    def print(self):
        """Docstring: Method to print information"""
        print('\nPerson:')
        print(f'\tSecond name: {self.__second_name}')
        print(f'\tName: {self.__name}')
        print(f'\tBirth year: {self.__birth_year}')


class SchoolBoy(Person):
    """Docstring: Class SchoolBoy extends class Person"""
    def __init__(self, grade, *args):
        """Docstring: Constructor for class SchoolBoy"""
        super().__init__(*args)
        self.__grade = grade

    def get_grade(self):
        """Docstring: Getter for field 'grade'"""
        return self.__grade

    def set_grade(self, grade):
        """Docstring: Setter for field 'grade'"""
        self.__grade = grade

    def print(self):
        """Docstring: Method to print information"""
        super().print()
        print('\tType: SchoolBoy')
        print(f'\tGrade: {self.__grade}')


class Parent(Person):
    """Docstring: Class Parent extends class Person"""
    def __init__(self, job_address, *args):
        """Docstring: Constructor for class Parent"""
        super().__init__(*args)
        self.__job_address = job_address
        self.children = []

    def get_job_address(self):
        """Docstring: Getter for field 'job_address'"""
        return self.__job_address

    def set_job_address(self, job_address):
        """Docstring: Setter for field 'job_address'"""
        self.__job_address = job_address

    def add_child(self, child):
        """Docstring: Method to add child"""
        self.children.append(child)

    def print(self):
        """Docstring: Method to print information"""
        super().print()
        print('\tType: Parent')
        print(f'\tJob address: {self.__job_address}')
        if len(self.children) > 0:
            print('\tChildren:')
            for child in self.children:
                print(f'\t\t{child.get_name()} {child.get_second_name()}, {child.get_grade()}')


# Main program entry point
if __name__ == '__main__':
    print('\nHomework 06 (2023.05.25)')
    print('-' * 24)

    person1 = Person('Ivanov', 'Ivan', 25)
    person2 = Person('Petrov', 'Petr', 35)

    schoolboy1 = SchoolBoy('7 "A"', 'Dimov', 'Dima', 13)
    schoolboy2 = SchoolBoy('5 "B"', 'Popov', 'Alex', 10)

    parent1 = Parent('Minsk', 'Irova', 'Ira', 27)
    parent2 = Parent('Grodno', 'Sashov', 'Sasha', 40)

    person1.print()
    person2.print()
    schoolboy1.print()
    schoolboy2.print()
    parent1.print()
    parent2.print()

    parent2.add_child(schoolboy1)
    parent2.add_child(schoolboy2)

    parent2.print()

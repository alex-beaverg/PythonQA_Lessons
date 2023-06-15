# Homework 08, file 6 (2023.06.08)
# All Homeworks Tests (PyTest)

# Run with cmd-line from current files' folder:
#   Current file:
#       pytest HW_08_6_AllHomeworksTest.py -v
# (Flag "-v" -> using for more information in console)

import pytest

from HW_01_Basics.HW_01 import information, variables, string_methods as SM1, simple_calculations
from HW_02_Basics_and_OOP.HW_02 import string_methods as SM2, Person as Pers1, Student as Stud1
from HW_03_OOP.HW_03 import Book, Library, Person as Pers2, Student as Stud2
from HW_04_OOP.HW_04 import BookStore, NewBook, Customer, Order, Package, Stamp, Envelop
from HW_05_OOP.HW_05_1 import Employee
from HW_05_OOP.HW_05_2_Circles import Circle, CircleAnother, Point
from HW_06_OOP.HW_06 import Person as Pers3, SchoolBoy, Parent as Parent1
from HW_07_Basics_and_OOP.HW_07_1_Classes import Human, Parent as Parent2, Kid


class TestCaseHomework01:
    """Docstring: Test class (case) for tests for homework 01"""

    @pytest.mark.parametrize('expected_result', ['Bobrikov A.V.'])
    def test_01_01_information_method(self, expected_result) -> None:
        """Docstring: Parametrized test method for method information"""
        result = information()
        assert result == expected_result, "[ASSERT MESSAGE]: Incorrect information!"

    @pytest.mark.parametrize('expected_result', [11])
    def test_01_02_variables_method(self, expected_result) -> None:
        """Docstring: Parametrized test method for method variables"""
        result = variables()
        assert result == expected_result, "[ASSERT MESSAGE]: Length of variables' list is incorrect!"

    @pytest.mark.parametrize('expected_result', [12])
    def test_01_03_string_methods_method(self, expected_result) -> None:
        """Docstring: Parametrized test method for method string_methods"""
        result = SM1()
        assert result == expected_result, "[ASSERT MESSAGE]: Length of methods' list is incorrect!"

    @pytest.mark.parametrize('expected_result', [10])
    def test_01_04_simple_calculations_method(self, expected_result) -> None:
        """Docstring: Parametrized test method for method simple_calculations"""
        result = simple_calculations()
        assert result == expected_result, "[ASSERT MESSAGE]: Variable 'a' is incorrect!"


class TestCaseHomework02:
    """Docstring: Test class (case) for tests for homework 02"""

    @pytest.mark.parametrize('expected_result', [42])
    def test_02_01_string_methods_method(self, expected_result) -> None:
        """Docstring: Parametrized test method for method string_methods"""
        result = SM2()
        assert result == expected_result, "[ASSERT MESSAGE]: Length of methods' list is incorrect!"

    @pytest.mark.parametrize('name, expected_result', [('Alexey', 'Alexey'), ('Ivan', 'Ivan')])
    def test_02_02_get_person_name(self, name, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person name"""
        person = Pers1()
        person.set_name(name)
        result = person.get_name()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's name is incorrect!"

    @pytest.mark.parametrize('surname, expected_result', [('Bobrikov', 'Bobrikov'), ('Ivanov', 'Ivanov')])
    def test_02_03_get_person_surname(self, surname, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person surname"""
        person = Pers1()
        person.set_surname(surname)
        result = person.get_surname()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's surname is incorrect!"

    @pytest.mark.parametrize('patronymic, expected_result', [('Valerievich', 'Valerievich'), ('Mitrich', 'Mitrich')])
    def test_02_04_get_person_patronymic(self, patronymic, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person patronymic"""
        person = Pers1()
        person.set_patronymic(patronymic)
        result = person.get_patronymic()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's patronymic is incorrect!"

    @pytest.mark.parametrize('name, surname, patronymic, expected_result',
                             [('Alexey', 'Bobrikov', 'Valerievich', 'Bobrikov A.V.')])
    def test_02_05_get_person_surname_with_initials(self, name, surname, patronymic, expected_result) -> None:
        """Docstring: Parametrized test method for method get_surname_with_initials"""
        person = Pers1()
        person.set_name(name)
        person.set_surname(surname)
        person.set_patronymic(patronymic)
        result = person.get_surname_with_initials()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect!"

    @pytest.mark.parametrize('name, surname, patronymic, expected_result',
                             [('Alexey', 'Bobrikov', 'Valerievich', 'Bobrikov Alexey Valerievich')])
    def test_02_06_get_person_all_information(self, name, surname, patronymic, expected_result) -> None:
        """Docstring: Parametrized test method for method get_all_information"""
        person = Pers1()
        person.set_name(name)
        person.set_surname(surname)
        person.set_patronymic(patronymic)
        result = person.get_all_information()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect!"

    @pytest.mark.parametrize('expected_result', ['IT STEP'])
    def test_02_07_get_student_university(self, expected_result) -> None:
        """Docstring: Parametrized test method for getter for student university"""
        student = Stud1()
        result = student.get_university()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect!"

    @pytest.mark.parametrize('expected_result', ['QA1823'])
    def test_02_08_get_student_group_id(self, expected_result) -> None:
        """Docstring: Parametrized test method for getter for student group_id"""
        student = Stud1()
        result = student.get_group_id()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect"

    @pytest.mark.parametrize('name, surname, patronymic, expected_result',
                             [('Alexey', 'Bobrikov', 'Valerievich',
                               'Bobrikov Alexey Valerievich is studying at the IT STEP in the QA1823 group')])
    def test_02_09_get_student_all_information(self, name, surname, patronymic, expected_result) -> None:
        """Docstring: Parametrized test method for method get_all_information"""
        student = Stud1()
        student.set_name(name)
        student.set_surname(surname)
        student.set_patronymic(patronymic)
        result = student.get_all_information()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect!"


class TestCaseHomework03:
    """Docstring: Test class (case) for tests for homework 03"""

    @pytest.mark.parametrize('expected_result', [1])
    def test_03_01_add_book_to_library_and_get_books(self, expected_result) -> None:
        """Docstring: Parametrized test method for add book to library"""
        book = Book('Name', 'Author', 150, 10, 'ru', 'Belarus', True,
                    ('1st string', '2nd string', '3rd string'))
        library = Library()
        library.add_book(book)
        result = len(library.get_books())
        assert result == expected_result, "[ASSERT MESSAGE]: Book didn't add to library!"

    @pytest.mark.parametrize('expected_result', ['Author'])
    def test_03_02_get_book(self, expected_result) -> None:
        """Docstring: Parametrized test method for get book"""
        book = Book('Name', 'Author', 150, 10, 'ru', 'Belarus', True,
                    ('1st string', '2nd string', '3rd string'))
        result = book.get_book()['Author']
        assert result == expected_result, "[ASSERT MESSAGE]: Book didn't create!"

    @pytest.mark.parametrize('name, expected_result', [('Alexey', 'Alexey'), ('Ivan', 'Ivan')])
    def test_03_03_get_person_name(self, name, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person name"""
        person = Pers2()
        person.set_name(name)
        result = person.get_name()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's name is incorrect!"

    @pytest.mark.parametrize('surname, expected_result', [('Bobrikov', 'Bobrikov'), ('Ivanov', 'Ivanov')])
    def test_03_04_get_person_surname(self, surname, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person surname"""
        person = Pers2()
        person.set_surname(surname)
        result = person.get_surname()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's surname is incorrect!"

    @pytest.mark.parametrize('patronymic, expected_result', [('Valerievich', 'Valerievich'), ('Mitrich', 'Mitrich')])
    def test_03_05_get_person_patronymic(self, patronymic, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person patronymic"""
        person = Pers2()
        person.set_patronymic(patronymic)
        result = person.get_patronymic()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's patronymic is incorrect!"

    @pytest.mark.parametrize('name, surname, patronymic, expected_result',
                             [('Alexey', 'Bobrikov', 'Valerievich', 'Bobrikov A.V.')])
    def test_03_06_get_person_surname_with_initials(self, name, surname, patronymic, expected_result) -> None:
        """Docstring: Parametrized test method for method get_surname_with_initials"""
        person = Pers2()
        person.set_name(name)
        person.set_surname(surname)
        person.set_patronymic(patronymic)
        result = person.get_surname_with_initials()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect!"

    @pytest.mark.parametrize('name, surname, patronymic, expected_result',
                             [('Alexey', 'Bobrikov', 'Valerievich', 'Bobrikov Alexey Valerievich')])
    def test_03_07_get_person_all_information(self, name, surname, patronymic, expected_result) -> None:
        """Docstring: Parametrized test method for method get_all_information"""
        person = Pers2()
        person.set_name(name)
        person.set_surname(surname)
        person.set_patronymic(patronymic)
        result = person.get_all_information()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect!"

    @pytest.mark.parametrize('expected_result', ['"IT STEP"'])
    def test_03_08_get_student_university(self, expected_result) -> None:
        """Docstring: Parametrized test method for getter for student university"""
        student = Stud2()
        result = student.get_university()
        assert result == expected_result, "[ASSERT MESSAGE]: University is incorrect!"

    @pytest.mark.parametrize('expected_result', ['"QA1823"'])
    def test_03_09_get_student_group_id(self, expected_result) -> None:
        """Docstring: Parametrized test method for getter for student group_id"""
        student = Stud2()
        result = student.get_group_id()
        assert result == expected_result, "[ASSERT MESSAGE]: Group is incorrect!"

    @pytest.mark.parametrize('name, surname, patronymic, expected_result',
                             [('Alexey', 'Bobrikov', 'Valerievich',
                               'Bobrikov Alexey Valerievich is studying at the "IT STEP" in the "QA1823" group')])
    def test_03_10_get_student_all_info_with_sets(self, name, surname, patronymic, expected_result) -> None:
        """Docstring: Parametrized test method for method get_all_information with sets"""
        student = Stud2()
        student.set_name(name)
        student.set_surname(surname)
        student.set_patronymic(patronymic)
        result = student.get_all_information()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect!"

    @pytest.mark.parametrize('expected_result', ['!!! Information is not set !!!'])
    def test_03_11_get_student_all_info_without_sets(self, expected_result) -> None:
        """Docstring: Parametrized test method for method get_all_information without sets"""
        student = Stud2()
        result = student.get_all_information()
        assert result == expected_result, "[ASSERT MESSAGE]: Result of method is incorrect!"


class TestCaseHomework04:
    """Docstring: Test class (case) for tests for homework 04"""

    @pytest.mark.parametrize('expected_result', ['Minsk'])
    def test_04_01_get_address(self, expected_result) -> None:
        """Docstring: Parametrized test method for get address"""
        BookStore()
        result = BookStore.get_address()
        assert result == expected_result, "[ASSERT MESSAGE]: Address is incorrect!"

    @pytest.mark.parametrize('expected_result', [1])
    def test_04_02_add_book_and_get_books(self, expected_result) -> None:
        """Docstring: Parametrized test method for get book list"""
        bookstore = BookStore()
        book = NewBook(20, 12, 'Name', 'Author', 150, 10, 'ru', 'Belarus', True,
                       ('1st string', '2nd string', '3rd string'))
        bookstore.add_book(book)
        result = len(bookstore.get_books())
        assert result == expected_result, "[ASSERT MESSAGE]: Book didn't add to Bookstore!"

    @pytest.mark.parametrize('expected_result', [1])
    def test_04_03_add_customer_and_get_customers(self, expected_result) -> None:
        """Docstring: Parametrized test method for get customer list"""
        bookstore = BookStore()
        customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        bookstore.add_customer(customer)
        result = len(bookstore.get_customers())
        assert result == expected_result, "[ASSERT MESSAGE]: Customer didn't add to Bookstore!"

    @pytest.mark.parametrize('expected_result', ['Alexey'])
    def test_04_04_get_customer(self, expected_result) -> None:
        """Docstring: Parametrized test method for get book"""
        customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        result = customer.get_customer()['Name']
        assert result == expected_result, "[ASSERT MESSAGE]: Customer didn't create!"

    def test_04_05_get_order_id(self) -> None:
        """Docstring: Test method for get order id"""
        customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        order = Order(customer)
        result = order.get_order_id()
        expected_result = order.__hash__()
        assert result == expected_result, "[ASSERT MESSAGE]: Customer's id is incorrect!"

    @pytest.mark.parametrize('expected_result', ['Alexey'])
    def test_04_06_get_order_customer(self, expected_result) -> None:
        """Docstring: Parametrized test method for get order customer"""
        customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        order = Order(customer)
        result = order.get_order_customer().get_customer()['Name']
        assert result == expected_result, "[ASSERT MESSAGE]: Customer's name is incorrect!"

    @pytest.mark.parametrize('expected_result', [12])
    def test_04_07_get_order_total_with_sale(self, expected_result) -> None:
        """Docstring: Parametrized test method for get order total with sale"""
        bookstore = BookStore()
        customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        order = Order(customer)
        book = NewBook(20, 12, 'Name', 'Author', 150, 10, 'ru', 'Belarus', True,
                       ('1st string', '2nd string', '3rd string'))
        bookstore.add_book(book)
        order.add_book_in_order(book)
        result = order.get_order_total_with_sale()
        assert result == expected_result, "[ASSERT MESSAGE]: Total order price with sale is incorrect!"

    @pytest.mark.parametrize('expected_result', [1])
    def test_04_08_add_book_in_order_and_get_books_in_order(self, expected_result) -> None:
        """Docstring: Parametrized test method for method add_book_in_order"""
        bookstore = BookStore()
        customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        order = Order(customer)
        book = NewBook(20, 12, 'Name', 'Author', 150, 10, 'ru', 'Belarus', True,
                       ('1st string', '2nd string', '3rd string'))
        bookstore.add_book(book)
        order.add_book_in_order(book)
        result = len(order.get_books_in_order())
        assert result == expected_result, "[ASSERT MESSAGE]: Book didn't add to order!"

    def test_04_09_get_package(self) -> None:
        """Docstring: Test method for get package"""
        bookstore = BookStore()
        customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        order = Order(customer)
        book = NewBook(20, 12, 'Name', 'Author', 150, 10, 'ru', 'Belarus', True,
                       ('1st string', '2nd string', '3rd string'))
        bookstore.add_book(book)
        order.add_book_in_order(book)
        package = Package(order)
        result = package.get_package()['Order']
        expected_result = order
        assert result == expected_result, "[ASSERT MESSAGE]: Package didn't create!"

    @pytest.mark.parametrize('addr_from, addr_to, expected_result', [('Minsk', 'Minsk', 1), ('Minsk', 'Grodno', 2)])
    def test_04_10_get_quantity_stamps(self, addr_from, addr_to, expected_result) -> None:
        """Docstring: Parametrized test method for method get_quantity_stamps"""
        stamp = Stamp(addr_from, addr_to)
        result = stamp.get_quantity_stamps()
        assert result == expected_result, "[ASSERT MESSAGE]: Incorrect calculation of stamps!"

    @pytest.mark.parametrize('addr_to, expected_result', [('Minsk', 123000), ('Grodno', 225000), ('Brest', 321000)])
    def test_04_11_generate_code(self, addr_to, expected_result) -> None:
        """Docstring: Parametrized test method for method generate_code"""
        result = Envelop.generate_code(addr_to)
        assert result == expected_result, "[ASSERT MESSAGE]: Incorrect generating code!"

    @pytest.mark.parametrize('addr_to, expected_result', [('Minsk', 1), ('Grodno', 2)])
    def test_04_12_generate_stamp(self, addr_to, expected_result) -> None:
        """Docstring: Parametrized test method for method generate_stamp"""
        bookstore = BookStore()
        customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', addr_to, 'Card')
        order = Order(customer)
        book = NewBook(20, 12, 'Name', 'Author', 150, 10, 'ru', 'Belarus', True,
                       ('1st string', '2nd string', '3rd string'))
        bookstore.add_book(book)
        order.add_book_in_order(book)
        package = Package(order)
        envelop = Envelop(package)
        result = envelop.generate_stamp()
        assert result == expected_result, "[ASSERT MESSAGE]: Incorrect generating stamp!"


class TestCaseHomework05:
    """Docstring: Test class (case) for tests for homework 05"""

    @pytest.mark.parametrize('sal, new_sal, expected_result', [(500, 400, 500), (1000, 1200, 1200), (500, 4000, 1000)])
    def test_05_01_set_salary(self, sal, new_sal, expected_result) -> None:
        """Docstring: Parametrized test method for method set_salary"""
        employee = Employee(sal)
        employee.set_salary(new_sal)
        result = employee.get_salary()
        assert result == expected_result, "[ASSERT MESSAGE]: Salary after setter method is incorrect!"

    @pytest.mark.parametrize('rad, new_rad, expected_result', [(15, 20, 20)])
    def test_05_02_set_circle_radius(self, rad, new_rad, expected_result) -> None:
        """Docstring: Parametrized test method for method set_radius"""
        circle = Circle(rad)
        circle.radius = new_rad
        result = circle.radius
        assert result == expected_result, "[ASSERT MESSAGE]: New radius is incorrect!"

    @pytest.mark.parametrize('rad, new_rad, expected_result', [(15, 20, 20)])
    def test_05_03_set_another_circle_radius(self, rad, new_rad, expected_result) -> None:
        """Docstring: Parametrized test method for method set_radius"""
        circle = CircleAnother(rad)
        circle.radius = new_rad
        result = circle.radius
        assert result == expected_result, "[ASSERT MESSAGE]: New radius is incorrect!"

    @pytest.mark.parametrize('coord, new_coord, expected_result', [((5, 5), (7, 7), (5, 5))])
    def test_05_04_set_coordinates(self, coord, new_coord, expected_result) -> None:
        """Docstring: Parametrized test method for set coordinates of point"""
        point = Point(*coord)
        point.x = new_coord[0]
        point.y = new_coord[1]
        result = (point.x, point.y)
        assert result == expected_result, "[ASSERT MESSAGE]: New coordinates added! It's incorrect!"


class TestCaseHomework06:
    """Docstring: Test class (case) for tests for homework 06"""

    @pytest.mark.parametrize('name, expected_result', [('Alexey', 'Alexey'), ('Ivan', 'Ivan')])
    def test_06_01_get_person_name(self, name, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person name"""
        person = Pers3(name, 'Second name', 41)
        result = person.get_name()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's name is incorrect!"

    @pytest.mark.parametrize('second_name, expected_result', [('Bobrikov', 'Bobrikov'), ('Smith', 'Smith')])
    def test_06_02_get_person_second_name(self, second_name, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person second name"""
        person = Pers3('Name', second_name, 41)
        result = person.get_second_name()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's surname is incorrect!"

    @pytest.mark.parametrize('birth_year, expected_result', [(41, 41), (28, 28)])
    def test_06_03_get_person_birth_year(self, birth_year, expected_result) -> None:
        """Docstring: Parametrized test method for getter for person birth year"""
        person = Pers3('Name', 'Second name', birth_year)
        result = person.get_birth_year()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's birth date is incorrect!"

    @pytest.mark.parametrize('name, new_name, expected_result', [('Ivan', 'Alex', 'Alex'), ('Ian', 'Ivan', 'Ivan')])
    def test_06_04_set_person_name(self, name, new_name, expected_result) -> None:
        """Docstring: Parametrized test method for setter for person name"""
        person = Pers3(name, 'Second name', 41)
        person.set_name(new_name)
        result = person.get_name()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's name after setter method is incorrect!"

    @pytest.mark.parametrize('sec_name, new_sec_name, expected_result', [('Smith', 'Bobrikov', 'Bobrikov')])
    def test_06_05_set_person_second_name(self, sec_name, new_sec_name, expected_result) -> None:
        """Docstring: Parametrized test method for setter for person second name"""
        person = Pers3('Name', sec_name, 41)
        person.set_second_name(new_sec_name)
        result = person.get_second_name()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's surname after set method is incorrect!"

    @pytest.mark.parametrize('birth_year, new_birth_year, expected_result', [(28, 41, 41), (41, 28, 28)])
    def test_06_06_set_person_birth_year(self, birth_year, new_birth_year, expected_result) -> None:
        """Docstring: Parametrized test method for setter for person birth year"""
        person = Pers3('Name', 'Second name', birth_year)
        person.set_birth_year(new_birth_year)
        result = person.get_birth_year()
        assert result == expected_result, "[ASSERT MESSAGE]: Person's birth date after set method is incorrect!"

    @pytest.mark.parametrize('grade, expected_result', [('7 "A"', '7 "A"'), ('5 "B"', '5 "B"')])
    def test_06_07_get_schoolboy_grade(self, grade, expected_result) -> None:
        """Docstring: Parametrized test method for getter for schoolboy grade"""
        schoolboy = SchoolBoy(grade, 'Name', 'Second name', 13)
        result = schoolboy.get_grade()
        assert result == expected_result, "[ASSERT MESSAGE]: Schoolboy's grade is incorrect!"

    @pytest.mark.parametrize('grade, new_grade, expected_result', [('4 "E"', '7 "A"', '7 "A"')])
    def test_06_08_set_schoolboy_grade(self, grade, new_grade, expected_result) -> None:
        """Docstring: Parametrized test method for setter for schoolboy grade"""
        schoolboy = SchoolBoy(grade, 'Name', 'Second name', 13)
        schoolboy.set_grade(new_grade)
        result = schoolboy.get_grade()
        assert result == expected_result, "[ASSERT MESSAGE]: Schoolboy's grade after set method is incorrect!"

    @pytest.mark.parametrize('job_address, expected_result', [('Office', 'Office'), ('Home', 'Home')])
    def test_06_09_get_parent_job_address(self, job_address, expected_result) -> None:
        """Docstring: Parametrized test method for getter for parent job address"""
        parent = Parent1(job_address, 'Name', 'Second name', 35)
        result = parent.get_job_address()
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's job address is incorrect!"

    @pytest.mark.parametrize('job_addr, new_job_addr, expected_result', [('Home', 'Office', 'Office')])
    def test_06_10_set_parent_job_address(self, job_addr, new_job_addr, expected_result) -> None:
        """Docstring: Parametrized test method for setter for parent job address"""
        parent = Parent1(job_addr, 'Name', 'Second name', 35)
        parent.set_job_address(new_job_addr)
        result = parent.get_job_address()
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's job address after set method is incorrect!"

    @pytest.mark.parametrize('expected_result', [1])
    def test_06_11_add_child(self, expected_result) -> None:
        """Docstring: Parametrized test method for getter for method to add child"""
        parent = Parent1('Job address', 'Name', 'Second name', 35)
        schoolboy = SchoolBoy('Grade', 'Name', 'Second name', 13)
        parent.add_child(schoolboy)
        result = len(parent.children)
        assert result == expected_result, "[ASSERT MESSAGE]: Child didn't add to parent"


class TestCaseHomework07:
    """Docstring: Test class (case) for tests for homework 07"""

    @pytest.mark.parametrize('name, expected_result', [('Alexey', 'Alexey'), ('Ivan', 'Ivan')])
    def test_07_01_get_human_name(self, name, expected_result) -> None:
        """Docstring: Parametrized test method for getter for human name"""
        human = Human(name, 'Surname')
        result = human.name
        assert result == expected_result, "[ASSERT MESSAGE]: Human's name is incorrect!"

    @pytest.mark.parametrize('surname, expected_result', [('Bobrikov', 'Bobrikov'), ('Smith', 'Smith')])
    def test_07_02_get_human_surname(self, surname, expected_result) -> None:
        """Docstring: Parametrized test method for getter for human surname"""
        human = Human('Name', surname)
        result = human.surname
        assert result == expected_result, "[ASSERT MESSAGE]: Human's surname is incorrect!"

    @pytest.mark.parametrize('name, new_name, expected_result', [('Ivan', 'Alexey', 'Alexey'), ('Ian', 'Ivan', 'Ivan')])
    def test_07_03_set_human_name(self, name, new_name, expected_result) -> None:
        """Docstring: Parametrized test method for setter for human name"""
        human = Human(name, 'Surname')
        human.name = new_name
        result = human.name
        assert result == expected_result, "[ASSERT MESSAGE]: Human's name after set method is incorrect!"

    @pytest.mark.parametrize('surname, new_surname, expected_result', [('Smith', 'Bobrikov', 'Bobrikov')])
    def test_07_04_set_human_surname(self, surname, new_surname, expected_result) -> None:
        """Docstring: Parametrized test method for setter for human surname"""
        human = Human('Name', surname)
        human.surname = new_surname
        result = human.surname
        assert result == expected_result, "[ASSERT MESSAGE]: Human's surname after set method is incorrect!"

    @pytest.mark.parametrize('age, expected_result', [(41, 41), (28, 28)])
    def test_07_05_get_parent_age(self, age, expected_result) -> None:
        """Docstring: Parametrized test method for getter for parent age"""
        parent = Parent2("Name", "Surname", age, "Office", 1000, "High", 15000, "Soccer")
        result = parent.age
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's age is incorrect!"

    @pytest.mark.parametrize('job, expected_result', [('Office', 'Office'), ('Home', 'Home')])
    def test_07_06_get_parent_job(self, job, expected_result) -> None:
        """Docstring: Parametrized test method for getter for parent job"""
        parent = Parent2("Name", "Surname", 32, job, 1000, "High", 15000, "Soccer")
        result = parent.job
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's job is incorrect!"

    @pytest.mark.parametrize('salary, expected_result', [(1000, 1000), (1200, 1200)])
    def test_07_07_get_parent_salary(self, salary, expected_result) -> None:
        """Docstring: Parametrized test method for getter for parent salary"""
        parent = Parent2("Name", "Surname", 32, "Office", salary, "High", 15000, "Soccer")
        result = parent.salary
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's salary is incorrect!"

    @pytest.mark.parametrize('education, expected_result', [('High', 'High'), ('Medium', 'Medium')])
    def test_07_08_get_parent_education(self, education, expected_result) -> None:
        """Docstring: Parametrized test method for getter for parent education"""
        parent = Parent2("Name", "Surname", 32, "Office", 1500, education, 15000, "Soccer")
        result = parent.education
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's education is incorrect!"

    @pytest.mark.parametrize('accumulation, expected_result', [(100_000, 100_000), (50_000, 50_000)])
    def test_07_09_get_parent_accumulation(self, accumulation, expected_result) -> None:
        """Docstring: Parametrized test method for getter for parent accumulation"""
        parent = Parent2("Name", "Surname", 32, "Office", 1500, "High", accumulation, "Soccer")
        result = parent.accumulation
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's accumulation is incorrect!"

    @pytest.mark.parametrize('hobby, expected_result', [('Fishing', 'Fishing'), ('Hockey', 'Hockey')])
    def test_07_10_get_parent_hobby(self, hobby, expected_result) -> None:
        """Docstring: Parametrized test method for getter for parent hobby"""
        parent = Parent2("Name", "Surname", 32, "Office", 1500, "High", 15000, hobby)
        result = parent.hobby
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's hobby is incorrect!"

    @pytest.mark.parametrize('age, new_age, expected_result', [(28, 41, 41), (41, 28, 28)])
    def test_07_11_set_parent_age(self, age, new_age, expected_result) -> None:
        """Docstring: Parametrized test method for setter for parent age"""
        parent = Parent2("Name", "Surname", age, "Office", 1000, "High", 15000, "Soccer")
        parent.age = new_age
        result = parent.age
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's age after set method is incorrect!"

    @pytest.mark.parametrize('job, new_job, expected_result', [('Home', 'Office', 'Office')])
    def test_07_12_set_parent_job(self, job, new_job, expected_result) -> None:
        """Docstring: Parametrized test method for setter for parent job"""
        parent = Parent2("Name", "Surname", 32, job, 1000, "High", 15000, "Soccer")
        parent.job = new_job
        result = parent.job
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's job after set method is incorrect!"

    @pytest.mark.parametrize('salary, new_salary, expected_result', [(800, 1000, 1000), (1300, 1200, 1200)])
    def test_07_13_set_parent_salary(self, salary, new_salary, expected_result) -> None:
        """Docstring: Parametrized test method for setter for parent salary"""
        parent = Parent2("Name", "Surname", 32, "Office", salary, "High", 15000, "Soccer")
        parent.salary = new_salary
        result = parent.salary
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's salary after set method is incorrect!"

    @pytest.mark.parametrize('education, new_education, expected_result', [('Medium', 'High', 'High')])
    def test_07_14_set_parent_education(self, education, new_education, expected_result) -> None:
        """Docstring: Parametrized test method for setter for parent education"""
        parent = Parent2("Name", "Surname", 32, "Office", 1500, education, 15000, "Soccer")
        parent.education = new_education
        result = parent.education
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's education after set method is incorrect!"

    @pytest.mark.parametrize('accumulation, new_accumulation, expected_result', [(80_000, 100_000, 100_000)])
    def test_07_15_set_parent_accumulation(self, accumulation, new_accumulation, expected_result) -> None:
        """Docstring: Parametrized test method for setter for parent accumulation"""
        parent = Parent2("Name", "Surname", 32, "Office", 1500, "High", accumulation, "Soccer")
        parent.accumulation = new_accumulation
        result = parent.accumulation
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's accumulation after set method is incorrect!"

    @pytest.mark.parametrize('hobby, new_hobby, expected_result', [('Soccer', 'Fishing', 'Fishing')])
    def test_07_16_set_parent_hobby(self, hobby, new_hobby, expected_result) -> None:
        """Docstring: Parametrized test method for setter for parent hobby"""
        parent = Parent2("Name", "Surname", 32, "Office", 1500, "High", 15000, hobby)
        parent.hobby = new_hobby
        result = parent.hobby
        assert result == expected_result, "[ASSERT MESSAGE]: Parent's hobby after set method is incorrect!"

    @pytest.mark.parametrize('job, expected_result', [('School', 'School'), ('Home', 'Home')])
    def test_07_17_get_kid_job(self, job, expected_result) -> None:
        """Docstring: Parametrized test method for getter for kid job"""
        kid = Kid(job, "Name", "Surname")
        result = kid.job
        assert result == expected_result, "[ASSERT MESSAGE]: Kid's job is incorrect!"

    @pytest.mark.parametrize('job, new_job, expected_result', [('Home', 'School', 'School')])
    def test_07_18_set_kid_job(self, job, new_job, expected_result) -> None:
        """Docstring: Parametrized test method for setter for kid job"""
        kid = Kid(job, "Name", "Surname")
        kid.job = new_job
        result = kid.job
        assert result == expected_result, "[ASSERT MESSAGE]: Kid's job after set method is incorrect!"

# Homework 05 (2023.04.27)

# public -> variable
# protected -> _variable
# private -> __variable

from PythonQA_HW_05_Circles import Circle, CircleAnother, Point


class Employee:
    """Docstring: Class Employee"""

    def __init__(self, salary: (int, float)) -> None:
        """Docstring: Constructor for class Employee"""
        print(f'LOG_INFO: Create employee with salary = {salary}')
        self.__salary = salary

    def set_salary(self, new_salary: (int, float)) -> None:
        """Docstring: Setter for salary variable"""
        print(f'LOG_INFO: Call set_salary method. Preview value = {self.__salary}. New value = {new_salary}')
        the_salary = new_salary
        if new_salary < self.__salary:
            print('LOG_INFO: Can\'t decrease salary because of the law')
            the_salary = self.__salary
        if new_salary > 2 * self.__salary:
            print('LOG_INFO: New salary is too huge!')
            the_salary = 2 * self.__salary
            print(f'LOG_INFO: New value = {the_salary}')
        self.__salary = the_salary

    def get_salary(self) -> (int, float):
        """Docstring: Getter for salary variable"""
        print(f'LOG_INFO: Call get_salary method. Current value = {self.__salary}')
        return self.__salary


# Main program entry point
if __name__ == '__main__':
    print('\nHomework 05 (2023.04.27)')
    print()

    employee_1 = Employee(500)
    employee_2 = Employee(1000)
    employee_3 = Employee(500)

    employee_1.get_salary()
    employee_1.set_salary(400)
    employee_1.get_salary()

    employee_2.get_salary()
    employee_2.set_salary(1200)
    employee_2.get_salary()

    employee_3.get_salary()
    employee_3.set_salary(4000)
    employee_3.get_salary()

    # Work with 'Python properties' (module PythonQA_HW_05_Circles, class Circle):
    print()
    c = Circle(5)
    c.radius
    c.radius = 10
    c.radius
    del c.radius

    # Work with 'Python properties', another variant (module PythonQA_HW_05_Circles, class CircleAnother):
    print()
    cir = CircleAnother(50)
    cir.radius
    cir.radius = 100
    cir.radius
    del cir.radius

    # Work with 'Read-only' variables (module PythonQA_HW_05_Circles, class Point)
    print()
    pnt = Point(5, 10)
    pnt.x
    pnt.y
    pnt.x = 20
    pnt.x
    pnt.y = 50
    pnt.y

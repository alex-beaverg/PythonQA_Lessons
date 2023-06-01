# Homework 07 (2023.06.01)
# Classes

class Human:
    """Docstring: Parent class Human"""

    def __init__(self, name: str, surname: str) -> None:
        """Docstring: Constructor for class Human"""
        self.__name = name
        self.__surname = surname

    def __get_name(self) -> str:
        """Docstring: Private getter for name"""
        return self.__name

    def __get_surname(self) -> str:
        """Docstring: Private getter for surname"""
        return self.__surname

    def __set_name(self, name: str) -> None:
        """Docstring: Private setter for name"""
        self.__name = name

    def __set_surname(self, surname: str) -> None:
        """Docstring: Private setter for surname"""
        self.__surname = surname

    name = property(
        fget=__get_name,
        fset=__set_name,
        doc="The name property"
    )

    surname = property(
        fget=__get_surname,
        fset=__set_surname,
        doc="The surname property"
    )


class Parent(Human):
    """Docstring: Class Parent extends class Human"""

    def __init__(self, name: str, surname: str, age: int, job: str, salary: int, education: str, accumulation: int,
                 hobby: str) -> None:
        """Docstring: Constructor for class Parent"""
        super().__init__(name, surname)
        self.__age = age
        self.__job = job
        self.__salary = salary
        self.__education = education
        self.__accumulation = accumulation
        self.__hobby = hobby

    @property
    def age(self) -> int:
        """Docstring: Getter for age"""
        return self.__age

    @property
    def job(self) -> str:
        """Docstring: Getter for job"""
        return self.__job

    @property
    def salary(self) -> int:
        """Docstring: Getter for salary"""
        return self.__salary

    @property
    def education(self) -> str:
        """Docstring: Getter for education"""
        return self.__education

    @property
    def accumulation(self) -> int:
        """Docstring: Getter for accumulation"""
        return self.__accumulation

    @property
    def hobby(self) -> str:
        """Docstring: Getter for hobby"""
        return self.__hobby

    @age.setter
    def age(self, age: int) -> None:
        """Docstring: Setter for age"""
        self.__age = age

    @job.setter
    def job(self, job: str) -> None:
        """Docstring: Setter for job"""
        self.__job = job

    @salary.setter
    def salary(self, salary: int) -> None:
        """Docstring: Setter for salary"""
        self.__salary = salary

    @education.setter
    def education(self, education: str):
        """Docstring: Setter for education"""
        self.__education = education

    @accumulation.setter
    def accumulation(self, accumulation: int) -> None:
        """Docstring: Setter for accumulation"""
        self.__accumulation = accumulation

    @hobby.setter
    def hobby(self, hobby: str) -> None:
        """Docstring: Setter for hobby"""
        self.__hobby = hobby


class Kid(Human):
    """Docstring: Class Kid extends class Human"""

    def __init__(self, job: str, name: str, surname: str) -> None:
        """Docstring: Constructor for class Kid"""
        super().__init__(name, surname)
        self.__job = job

    @property
    def job(self) -> str:
        """Docstring: Getter for job"""
        return self.__job

    @job.setter
    def job(self, job: str) -> None:
        """Docstring: Setter for job"""
        self.__job = job

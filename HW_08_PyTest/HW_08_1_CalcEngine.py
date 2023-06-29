# Homework 08, file 1 (2023.06.08)
# Calculating Engine

import math

from multipledispatch import dispatch


class CalcEngine:
    """Docstring: Class CalcEngine"""

    def __init__(self) -> None:
        """Docstring: Constructor for class CalcEngine"""
        self.__result = 0

    def __del__(self) -> None:
        """Docstring: Destructor for class CalcEngine"""
        pass

    @dispatch((int, float), (int, float))
    def add(self, a, b) -> (int, float):
        """Docstring: Basic realization of method for addiction"""
        self.__result = a + b
        return self.__result

    @dispatch((int, float))
    def add(self, a) -> (int, float):
        """Docstring: Method overload for addiction"""
        self.__result += a
        return self.__result

    @dispatch((int, float), (int, float))
    def sub(self, a, b) -> (int, float):
        """Docstring: Basic realization of method for subtraction"""
        self.__result = a - b
        return self.__result

    @dispatch((int, float))
    def sub(self, a) -> (int, float):
        """Docstring: Method overload for subtraction"""
        self.__result -= a
        return self.__result

    @dispatch((int, float), (int, float))
    def mul(self, a, b) -> (int, float):
        """Docstring: Basic realization of method for multiply"""
        self.__result = a * b
        return self.__result

    @dispatch((int, float))
    def mul(self, a) -> (int, float):
        """Docstring: Method overload for multiply"""
        self.__result *= a
        return self.__result

    @dispatch((int, float), (int, float))
    def div(self, a, b) -> (int, float):
        """Docstring: Basic realization of method for division"""
        self.__result = a / b
        return self.__result

    @dispatch((int, float))
    def div(self, a) -> (int, float):
        """Docstring: Method overload for division"""
        self.__result /= a
        return self.__result

    def percent(self, a: (int, float), b: (int, float)) -> (int, float):
        """Docstring: Method to calculate percent"""
        self.__result = a * b / 100
        return self.__result

    def sqrt(self, a: (int, float)) -> (int, float):
        """Docstring: Method to calculate square root"""
        self.__result = math.sqrt(a)
        return self.__result

    @dispatch((int, float), (int, float))
    def exp(self, a, b) -> (int, float):
        """Docstring: Basic realization of method for exponentiation"""
        self.__result = a ** b
        return self.__result

    @dispatch((int, float))
    def exp(self, a) -> (int, float):
        """Docstring: Method overload for exponentiation"""
        self.__result **= a
        return self.__result

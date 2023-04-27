class Circle:
    """Docstring: Class Circle"""

    def __init__(self, radius: (int, float)) -> None:
        """Docstring: Constructor for class Circle"""
        print(f'LOG_INFO: Create circle with radius = {radius}')
        self.__radius = radius

    def __get_radius(self) -> (int, float):
        """Docstring: Getter for variable 'radius'"""
        print(f'LOG_INFO: Get radius with value = {self.__radius}')
        return self.__radius

    def __set_radius(self, value: (int, float)) -> None:
        """Docstring: Setter for variable 'radius'"""
        print(f'LOG_INFO: Set radius with value = {value}')
        self.__radius = value

    def __del_radius(self) -> None:
        """Docstring: Deleter for variable 'radius'"""
        print(f'LOG_INFO: Delete radius with value = {self.__radius}')
        del self.__radius

    radius = property(
        fget=__get_radius,
        fset=__set_radius,
        fdel=__del_radius,
        doc='The radius property')


class CircleAnother:
    """Docstring: Class CircleAnother"""

    def __init__(self, radius: (int, float)) -> None:
        """Docstring: Constructor for class CircleAnother"""
        print(f'LOG_INFO: Create circle with radius = {radius}')
        self.__radius = radius

    @property
    def radius(self) -> (int, float):
        """Docstring: Getter for variable 'radius'"""
        print(f'LOG_INFO: Get radius with value = {self.__radius}')
        return self.__radius

    @radius.setter
    def radius(self, value: (int, float)) -> None:
        """Docstring: Setter for variable 'radius'"""
        print(f'LOG_INFO: Set radius with value = {value}')
        self.__radius = value

    @radius.deleter
    def radius(self) -> None:
        """Docstring: Deleter for variable 'radius'"""
        print(f'LOG_INFO: Delete radius with value = {self.__radius}')
        del self.__radius


class WriteCoordinateError(Exception):
    """Docstring: Class WriteCoordinateError extends class Exception"""
    pass


class Point:
    """Docstring: Class Point"""
    def __init__(self, x: (int, float), y: (int, float)) -> None:
        """Docstring: Constructor for class Point"""
        print(f'LOG_INFO: Create point with coordinates: x = {x}, y = {y}')
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """Docstring: Getter for variable 'x'"""
        print(f'LOG_INFO: Get "x" with value = {self.__x}')
        return self.__x

    @property
    def y(self):
        """Docstring: Getter for variable 'y'"""
        print(f'LOG_INFO: Get "y" with value = {self.__y}')
        return self.__y

    @x.setter
    def x(self, value):
        """Docstring: Setter for variable 'x'"""
        print(f'LOG_INFO: Set "x" with value = {value}')
        try:
            raise WriteCoordinateError
        except WriteCoordinateError:
            print(f'ERROR_INFO: x coordinate is read-only')

    @y.setter
    def y(self, value):
        """Docstring: Setter for variable 'y'"""
        print(f'LOG_INFO: Set "y" with value = {value}')
        try:
            raise WriteCoordinateError
        except WriteCoordinateError:
            print(f'ERROR_INFO: y coordinate is read-only')

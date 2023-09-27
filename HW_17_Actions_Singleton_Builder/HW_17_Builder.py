# Homework 17, file 1 - (2023.09.19)
# Classwork -> Builder pattern example

from typing import Self


class SweetBoxBuilder:
    """Docstring: Class SweetBoxBuilder -> example of builder pattern"""

    def __init__(self) -> None:
        """Docstring: Constructor of SweetBoxBuilder class"""
        self.candy = ''
        self.chocolate = ''
        self.bubble_gum = ''
        self.marshmallow = ''
        self.marmalade = ''
        self.sweet_set_box = []

    def add_candy(self, candy_name: str) -> Self:
        """Docstring: Method to add candy to sweet box"""
        self.candy = candy_name
        self.sweet_set_box.append(self.candy)
        return self

    def add_chocolate(self, chocolate_name: str) -> Self:
        """Docstring: Method to add chocolate to sweet box"""
        self.chocolate = chocolate_name
        self.sweet_set_box.append(self.chocolate)
        return self

    def add_bubble_gum(self, bubble_gum_name: str) -> Self:
        """Docstring: Method to add bubble gum to sweet box"""
        self.bubble_gum = bubble_gum_name
        self.sweet_set_box.append(self.bubble_gum)
        return self

    def add_marshmallow(self, marshmallow_name: str) -> Self:
        """Docstring: Method to add marshmallow to sweet box"""
        self.marshmallow = marshmallow_name
        self.sweet_set_box.append(self.marshmallow)
        return self

    def add_marmalade(self, marmalade_name: str) -> Self:
        """Docstring: Method to add marmalade to sweet box"""
        self.marmalade = marmalade_name
        self.sweet_set_box.append(self.marmalade)
        return self

    def print_box(self) -> None:
        """Docstring: Method to print (build) sweet box"""
        print('Sweet box:')
        for sweet in self.sweet_set_box:
            print('\t' + sweet)


if __name__ == '__main__':
    SweetBoxBuilder()\
        .add_candy('Chupa Chups')\
        .add_candy('Lemon caramel')\
        .add_marmalade('Strawberry marmalade')\
        .add_marshmallow('Choco marshmallow')\
        .add_chocolate('Chocolate with peanuts')\
        .add_bubble_gum('Orbit without sugar')\
        .print_box()
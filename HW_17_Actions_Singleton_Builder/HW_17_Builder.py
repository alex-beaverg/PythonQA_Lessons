# Homework 17, file 1 - (2023.09.19)
# Classwork -> Builder pattern example

from typing import Self


class SweetSetBuilder:
    """Docstring: Class SweetSetBuilder -> example of builder pattern"""

    def __init__(self) -> None:
        """Docstring: Constructor of SweetSetBuilder class"""
        self.candy = ''
        self.chocolate = ''
        self.bubble_gum = ''
        self.marshmallow = ''
        self.marmalade = ''
        self.sweet_set_box = []

    def with_candy(self, candy_name: str) -> Self:
        """Docstring: Method to add candy to sweet set"""
        self.candy = candy_name
        self.sweet_set_box.append(self.candy)
        return self

    def with_chocolate(self, chocolate_name: str) -> Self:
        """Docstring: Method to add chocolate to sweet set"""
        self.chocolate = chocolate_name
        self.sweet_set_box.append(self.chocolate)
        return self

    def with_bubble_gum(self, bubble_gum_name: str) -> Self:
        """Docstring: Method to add bubble gum to sweet set"""
        self.bubble_gum = bubble_gum_name
        self.sweet_set_box.append(self.bubble_gum)
        return self

    def with_marshmallow(self, marshmallow_name: str) -> Self:
        """Docstring: Method to add marshmallow to sweet set"""
        self.marshmallow = marshmallow_name
        self.sweet_set_box.append(self.marshmallow)
        return self

    def with_marmalade(self, marmalade_name: str) -> Self:
        """Docstring: Method to add marmalade to sweet set"""
        self.marmalade = marmalade_name
        self.sweet_set_box.append(self.marmalade)
        return self

    def build(self) -> None:
        """Docstring: Method to build (print) sweet set"""
        print('Sweet set box:')
        for sweet in self.sweet_set_box:
            print('\t' + sweet)


if __name__ == '__main__':
    SweetSetBuilder()\
        .with_candy('Chupa Chups')\
        .with_candy('Lemon caramel')\
        .with_marmalade('Strawberry marmalade')\
        .with_marshmallow('Choco marshmallow')\
        .with_chocolate('Chocolate with peanuts')\
        .with_bubble_gum('Orbit without sugar')\
        .build()
# Homework 12, file 7 - (2023.07.13)
# Homework. Decorator

import json
import jsonpickle


def serializable(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, *args):
            return getattr(self.wrapped, *args)

        def serialize(self):
            return jsonpickle.encode(self.wrapped)

        @staticmethod
        def deserialize(ser_str):
            return jsonpickle.decode(ser_str)

        def write_book(self, path):
            with open(path, 'w') as file_write:
                json.dump(self.serialize(), file_write)

        @staticmethod
        def read_book(path):
            with open(path, 'r') as file_read:
                book = Book.deserialize(json.load(file_read))
            return book

    return Wrapper


@serializable
class Book:
    def __init__(self, title: str, author: str, preview: list) -> None:
        self.title = title
        self.author = author
        self.preview = preview


if __name__ == '__main__':
    book_1 = Book('Pook the Mouse', 'John Dick', ['Hello!', 'This is my life!', 'Good bye!'])
    book_2 = Book('Pook the Pig', 'John Pick', ['Arise!', 'This is my death!', 'Time to die!'])
    book_3 = Book('Pook the Horse', 'John Click', ['Morning!', 'Day!', 'Night!'])

    in_out_path = 'files/res_04_decorator/BOOK_INPUT_OUTPUT.json'

    book_2.write_book(in_out_path)

    book_4 = Book.read_book(in_out_path)
    print(book_4.title)

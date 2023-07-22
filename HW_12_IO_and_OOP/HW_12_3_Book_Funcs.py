# Homework 12, file 3 - (2023.07.13)
# Homework. Book Functions

import pickle
import json
import orjson
import jsonpickle
from xml.dom.minidom import parse, parseString
from xml.etree.ElementTree import parse as ET_parse
from lxml import etree as ETree
from xml.sax import parse as SAX_parse
from xml.sax.handler import ContentHandler
from HW_12_2_Classes import Book


class TxtBookFuncs:
    """Docstring: Class with in/out book functions to work with txt files"""

    @staticmethod
    def write_books_to_text_file(path: str, book: Book, mode='w') -> None:
        """Docstring: Function to write or add book to text file"""
        with open(path, mode) as file_write:
            file_write.write(str(book.id) + '\n')
            file_write.write(book.title + '\n')
            file_write.write(book.author + '\n')
            file_write.write(str(book.quantity) + '\n')
            file_write.write(str(book.price) + '\n')
            for place in book.places:
                file_write.write(place + '\n')
            file_write.write('\n')

    @staticmethod
    def read_books_from_text_file(path: str, single=True) -> (Book, list):
        """Docstring: Function to read books from text file"""
        lines = []
        books = []
        book = Book('', '', 0, 0)
        try:
            with open(path, 'r') as file_read:
                for line in file_read:
                    lines.append(line.strip())
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Book has not been created from text file')
        else:
            i = 0
            while i < len(lines):
                book.id = lines[i]
                i += 1
                book.title = lines[i]
                i += 1
                book.author = lines[i]
                i += 1
                book.quantity = lines[i]
                i += 1
                book.price = lines[i]
                i += 1
                while True:
                    if i == len(lines) or lines[i] == '':
                        i += 1
                        break
                    else:
                        book.places.append(lines[i])
                        i += 1
                if not single:
                    books.append(book)
                    book = Book('', '', 0, 0)
            if single:
                return book
            else:
                return books


class BinBookFuncs:
    """Docstring: Class with in/out book functions to work with binary files"""

    @staticmethod
    def write_books_to_binary_file(path: str, book: Book, mode='wb') -> None:
        """Docstring: Function to write or add book to binary file"""
        with open(path, mode) as file_write:
            pickle.dump(book, file_write)

    @staticmethod
    def read_books_from_binary_file(path: str, single=True) -> (Book, list):
        """Docstring: Function to read books from binary file"""
        try:
            if single:
                with open(path, 'rb') as file_read:
                    output = pickle.load(file_read)
            else:
                output = []
                with open(path, 'rb') as file_read:
                    while True:
                        try:
                            book = pickle.load(file_read)
                        except EOFError:
                            break
                        else:
                            output.append(book)
            return output
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Book has not been created from binary file')


class XmlMiniDomBookFuncs:
    """Docstring: Class with in/out book functions to work with xml files (minidom)"""

    @staticmethod
    def write_books_to_xml_file(path: str, book: Book, no_add=True) -> None:
        """Docstring: Function to write or add book to xml file"""
        doc = parseString('<books/>')
        root = doc.documentElement
        book_list = list()
        book_list.append(book)
        if not no_add:
            book_list += XmlMiniDomBookFuncs.read_books_from_xml_file(path, False)
        for book_from_list in book_list:
            book_element = doc.createElement('book')
            root.appendChild(book_element)
            book_id = doc.createElement('id')
            book_element.appendChild(book_id)
            book_id.appendChild(doc.createTextNode(str(book_from_list.id)))
            title = doc.createElement('title')
            book_element.appendChild(title)
            title.appendChild(doc.createTextNode(book_from_list.title))
            author = doc.createElement('author')
            book_element.appendChild(author)
            author.appendChild(doc.createTextNode(book_from_list.author))
            quantity = doc.createElement('quantity')
            book_element.appendChild(quantity)
            quantity.appendChild(doc.createTextNode(str(book_from_list.quantity)))
            price = doc.createElement('price')
            book_element.appendChild(price)
            price.appendChild(doc.createTextNode(str(book_from_list.price)))
            places = doc.createElement('places')
            book_element.appendChild(places)
            for place in book_from_list.places:
                place_element = doc.createElement('place')
                places.appendChild(place_element)
                place_element.appendChild(doc.createTextNode(place))
        with open(path, 'w') as file_write:
            file_write.write(doc.toprettyxml())

    @staticmethod
    def read_books_from_xml_file(path: str, single=True) -> (Book, list):
        """Docstring: Function to read books from xml file"""
        places, output = [], []
        try:
            with parse(path) as xml_doc:
                books = xml_doc.getElementsByTagName('book')
                for book in books:
                    book_id = book.getElementsByTagName('id')[0].firstChild.data
                    title = book.getElementsByTagName('title')[0].firstChild.data
                    author = book.getElementsByTagName('author')[0].firstChild.data
                    quantity = book.getElementsByTagName('quantity')[0].firstChild.data
                    price = book.getElementsByTagName('price')[0].firstChild.data

                    places_element = book.getElementsByTagName('places')[0]
                    place_list = places_element.getElementsByTagName('place')
                    for place_element in place_list:
                        place = place_element.firstChild.data
                        places.append(place)
                    if single:
                        output = Book(title, author, quantity, price)
                        output.id = book_id
                        output.places = places
                    else:
                        one_book = Book(title, author, quantity, price)
                        one_book.id = book_id
                        one_book.places = places
                        output.append(one_book)
                        places = []
            return output
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Book has not been created from xml file '
                  f'(minidom module)')


class XmlElementTreeBookFuncs:
    """Docstring: Class with in/out book functions to work with xml files (elementtree)"""

    @staticmethod
    def write_books_to_xml_file(path: str, book: Book, no_add=True) -> None:
        """Docstring: Function to write or add book to xml file"""
        root = ETree.Element('books')
        book_list = list()
        book_list.append(book)
        if not no_add:
            book_list += XmlElementTreeBookFuncs.read_books_from_xml_file(path, False)
        for book_from_list in book_list:
            book_element = ETree.SubElement(root, 'book')
            book_id = ETree.SubElement(book_element, 'id')
            book_id.text = str(book_from_list.id)
            title = ETree.SubElement(book_element, 'title')
            title.text = book_from_list.title
            author = ETree.SubElement(book_element, 'author')
            author.text = book_from_list.author
            quantity = ETree.SubElement(book_element, 'quantity')
            quantity.text = str(book_from_list.quantity)
            price = ETree.SubElement(book_element, 'price')
            price.text = str(book_from_list.price)
            places_element = ETree.SubElement(book_element, 'places')
            for place in book_from_list.places:
                place_element = ETree.SubElement(places_element, 'place')
                place_element.text = place
        tree = ETree.ElementTree(root)
        with open(path, "wb") as file_write:
            file_write.write(ETree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='utf-8'))

    @staticmethod
    def read_books_from_xml_file(path: str, single=True) -> (Book, list):
        """Docstring: Function to read books from xml file"""
        try:
            tree = ET_parse(path)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Book has not been created from xml file '
                  f'(elementtree module)')
        else:
            root = tree.getroot()
            output, title, author, quantity, price, places, book_id = [], '', '', 0, 0, [], ''
            for element in root.iter():
                if element.tag == 'places' or element.text.strip() != '':
                    if element.tag == 'id':
                        book_id = element.text
                    if element.tag == 'title':
                        title = element.text
                    if element.tag == 'author':
                        author = element.text
                    if element.tag == 'quantity':
                        quantity = element.text
                    if element.tag == 'price':
                        price = element.text
                    if element.tag == 'place':
                        places.append(element.text)
                if element.tag == 'book' and book_id != '':
                    one_book = Book(title, author, quantity, price)
                    one_book.id = book_id
                    one_book.places = places
                    output.append(one_book)
                    book_id, title, author, quantity, price, places = '', '', '', 0, 0, []
                    continue
            if single:
                output = Book(title, author, quantity, price)
                output.id = book_id
                output.places = places
            else:
                one_book = Book(title, author, quantity, price)
                one_book.id = book_id
                one_book.places = places
                output.append(one_book)
            return output


class JsonModuleBookFuncs:
    """Docstring: Class with in/out book functions to work with json files (json module)"""

    @staticmethod
    def write_books_to_json_file(path: str, book: Book, no_add=True) -> None:
        """Docstring: Function to write or add book to json file"""
        simple_obj = {'id': book.id, 'title': book.title, 'author': book.author, 'quantity': book.quantity,
                      'price': book.price, 'places': book.places}
        if not no_add:
            output = list()
            output.append(simple_obj)
            book_list = JsonModuleBookFuncs.read_books_from_json_file(path, False)
            for book_from_list in book_list:
                temp_book = {'id': book_from_list.id, 'title': book_from_list.title, 'author': book_from_list.author,
                             'quantity': book_from_list.quantity, 'price': book_from_list.price,
                             'places': book_from_list.places}
                output.append(temp_book)
            with open(path, 'w') as file_write:
                json.dump(output, file_write, indent=4)
        else:
            with open(path, 'w') as file_write:
                json.dump(simple_obj, file_write, indent=4)

    @staticmethod
    def read_books_from_json_file(path: str, single=True) -> (Book, list):
        """Docstring: Function to read books from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                income = json.load(file_read)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Book has not been created from json file '
                  f'(json module)')
        else:
            if single:
                output = Book(income['title'], income['author'], income['quantity'], income['price'])
                output.id = income['id']
                output.places = income['places']
            else:
                if type(income) == dict:
                    some_book = Book(income['title'], income['author'], income['quantity'], income['price'])
                    some_book.id = income['id']
                    some_book.places = income['places']
                    output.append(some_book)
                else:
                    for book_from_list in income:
                        some_book = Book(book_from_list['title'], book_from_list['author'], book_from_list['quantity'],
                                         book_from_list['price'])
                        some_book.id = book_from_list['id']
                        some_book.places = book_from_list['places']
                        output.append(some_book)
            return output


class OrjsonModuleBookFuncs:
    """Docstring: Class with in/out book functions to work with json files (orjson module)"""

    @staticmethod
    def write_books_to_json_file(path: str, book: Book, no_add=True) -> None:
        """Docstring: Function to write or add book to json file"""
        simple_obj = {'id': book.id, 'title': book.title, 'author': book.author, 'quantity': book.quantity,
                      'price': book.price, 'places': book.places}
        if not no_add:
            output = list()
            output.append(simple_obj)
            book_list = OrjsonModuleBookFuncs.read_books_from_json_file(path, False)
            for book_from_list in book_list:
                temp_book = {'id': book_from_list.id, 'title': book_from_list.title, 'author': book_from_list.author,
                             'quantity': book_from_list.quantity, 'price': book_from_list.price,
                             'places': book_from_list.places}
                output.append(temp_book)
            with open(path, 'wb') as file_write:
                text = orjson.dumps(output, option=orjson.OPT_INDENT_2)
                file_write.write(text)
        else:
            with open(path, 'wb') as file_write:
                text = orjson.dumps(simple_obj, option=orjson.OPT_INDENT_2)
                file_write.write(text)

    @staticmethod
    def read_books_from_json_file(path: str, single=True) -> (Book, list):
        """Docstring: Function to read books from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                text = file_read.read()
                income = orjson.loads(text)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Book has not been created from json file '
                  f'(orjson module)')
        else:
            if single:
                output = Book(income['title'], income['author'], income['quantity'], income['price'])
                output.id = income['id']
                output.places = income['places']
            else:
                if type(income) == dict:
                    some_book = Book(income['title'], income['author'], income['quantity'], income['price'])
                    some_book.id = income['id']
                    some_book.places = income['places']
                    output.append(some_book)
                else:
                    for book_from_list in income:
                        some_book = Book(book_from_list['title'], book_from_list['author'], book_from_list['quantity'],
                                         book_from_list['price'])
                        some_book.id = book_from_list['id']
                        some_book.places = book_from_list['places']
                        output.append(some_book)
            return output


class JsonPickleBookFuncs:
    """Docstring: Class with in/out book functions to work with json files (json pickle)"""

    @staticmethod
    def write_books_to_json_file(path: str, book: Book, no_add=True) -> None:
        """Docstring: Function to write or add book to json file"""
        simple_obj = {'id': book.id, 'title': book.title, 'author': book.author, 'quantity': book.quantity,
                      'price': book.price, 'places': book.places}
        if not no_add:
            output = list()
            output.append(simple_obj)
            book_list = JsonPickleBookFuncs.read_books_from_json_file(path, False)
            for book_from_list in book_list:
                temp_book = {'id': book_from_list.id, 'title': book_from_list.title, 'author': book_from_list.author,
                             'quantity': book_from_list.quantity, 'price': book_from_list.price,
                             'places': book_from_list.places}
                output.append(temp_book)
            with open(path, 'w') as file_write:
                jsonpickle.set_encoder_options('json', indent=4)
                text = jsonpickle.encode(output)
                file_write.write(text)
        else:
            with open(path, 'w') as file_write:
                jsonpickle.set_encoder_options('json', indent=4)
                text = jsonpickle.encode(simple_obj)
                file_write.write(text)

    @staticmethod
    def read_books_from_json_file(path: str, single=True) -> (Book, list):
        """Docstring: Function to read books from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                text = file_read.read()
                income = jsonpickle.decode(text)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Book has not been created from json file '
                  f'(jsonpickle module)')
        else:
            if single:
                output = Book(income['title'], income['author'], income['quantity'], income['price'])
                output.id = income['id']
                output.places = income['places']
            else:
                if type(income) == dict:
                    some_book = Book(income['title'], income['author'], income['quantity'], income['price'])
                    some_book.id = income['id']
                    some_book.places = income['places']
                    output.append(some_book)
                else:
                    for book_from_list in income:
                        some_book = Book(book_from_list['title'], book_from_list['author'], book_from_list['quantity'],
                                         book_from_list['price'])
                        some_book.id = book_from_list['id']
                        some_book.places = book_from_list['places']
                        output.append(some_book)
            return output


class XmlSaxReadBookFuncs(ContentHandler):
    """Docstring: Class with in/out book functions to work with xml files (SAX)"""

    def __init__(self) -> None:
        """Docstring: Constructor for class XmlSaxBookFuncs extends ContentHandler"""
        super().__init__()
        self.CurrentData = ''
        self.books = []
        self.book = Book('', '', 0, 0)
        self.book.id = ''

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def characters(self, content: str) -> None:
        """Docstring: Content list making method"""
        if content.strip() != "":
            if self.CurrentData == 'id':
                if self.book.id != '':
                    self.books.append(self.book)
                    self.book = Book('', '', 0, 0)
                    self.book.id = content
                else:
                    self.book.id = content
            if self.CurrentData == 'title':
                self.book.title = content
            if self.CurrentData == 'author':
                self.book.author = content
            if self.CurrentData == 'quantity':
                self.book.quantity = content
            if self.CurrentData == 'price':
                self.book.price = content
            if self.CurrentData == 'place':
                self.book.places.append(content)

    def get_books(self) -> list:
        """Docstring: Getter for books"""
        self.books.append(self.book)
        return self.books

    @staticmethod
    def read_books_from_xml_file(path: str) -> (Book, list):
        """Docstring: Function to read books from xml file"""
        handler = XmlSaxReadBookFuncs()
        try:
            SAX_parse(path, handler)
        except ValueError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Book has not been created from xml file (sax)')
        else:
            book_list = handler.get_books()
            if len(book_list) == 1:
                return book_list[0]
            else:
                return book_list

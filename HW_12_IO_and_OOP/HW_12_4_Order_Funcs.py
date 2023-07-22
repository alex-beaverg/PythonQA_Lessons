# Homework 12, file 4 - (2023.07.13)
# Homework. Order Functions

import pickle
import json
import orjson
import jsonpickle
from xml.dom.minidom import parse, parseString
from xml.etree.ElementTree import parse as ET_parse
from lxml import etree as ETree
from xml.sax import parse as SAX_parse
from xml.sax.handler import ContentHandler
from HW_12_2_Classes import Order


class TxtOrderFuncs:
    """Docstring: Class with in/out order functions to work with txt files"""

    @staticmethod
    def write_orders_to_text_file(path: str, order: Order, mode='w') -> None:
        """Docstring: Function to write or add order to text file"""
        with open(path, mode) as file_write:
            if mode == 'a':
                file_write.write('\n\n')
            file_write.write(order.id + '\n')
            file_write.write(order.status + '\n')
            for book, quantity in order.books.items():
                file_write.write(book + '\n')
                file_write.write(str(quantity) + '\n')
            file_write.write('\n')
            for place in order.places:
                file_write.write(place + '\n')

    @staticmethod
    def read_orders_from_text_file(path: str, single=True) -> (Order, list):
        """Docstring: Function to read orders from text file"""
        lines = []
        orders = []
        order = Order()
        try:
            with open(path, 'r') as file_read:
                for line in file_read:
                    lines.append(line.strip())
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Order has not been created from text file')
        else:
            i = 0
            while i < len(lines):
                order.id = lines[i]
                i += 1
                order.status = lines[i]
                i += 1
                while True:
                    if lines[i] == '':
                        i += 1
                        break
                    else:
                        order.books[lines[i]] = lines[i + 1]
                        i += 2
                while True:
                    if i == len(lines) or lines[i] == '':
                        i += 2
                        break
                    else:
                        order.places.append(lines[i])
                        i += 1
                if not single:
                    orders.append(order)
                    order = Order()
            if single:
                return order
            else:
                return orders


class BinOrderFuncs:
    """Docstring: Class with in/out order functions to work with binary files"""

    @staticmethod
    def write_orders_to_binary_file(path: str, order: Order, mode='wb') -> None:
        """Docstring: Function to write or add order to binary file"""
        with open(path, mode) as file_write:
            pickle.dump(order, file_write)

    @staticmethod
    def read_orders_from_binary_file(path: str, single=True) -> (Order, list):
        """Docstring: Function to read orders from binary file"""
        try:
            if single:
                with open(path, 'rb') as file_read:
                    output = pickle.load(file_read)
            else:
                output = []
                with open(path, 'rb') as file_read:
                    while True:
                        try:
                            order = pickle.load(file_read)
                        except EOFError:
                            break
                        else:
                            output.append(order)
            return output
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Order has not been created from binary file')


class XmlMiniDomOrderFuncs:
    """Docstring: Class with in/out order functions to work with xml files (minidom)"""

    @staticmethod
    def write_orders_to_xml_file(path: str, order: Order, no_add=True) -> None:
        """Docstring: Function to write or add order to xml file"""
        doc = parseString('<orders/>')
        root = doc.documentElement
        order_list = list()
        order_list.append(order)
        if not no_add:
            order_list += XmlMiniDomOrderFuncs.read_orders_from_xml_file(path, False)
        for order_from_list in order_list:
            order_element = doc.createElement('order')
            root.appendChild(order_element)
            order_id = doc.createElement('id')
            order_element.appendChild(order_id)
            order_id.appendChild(doc.createTextNode(str(order_from_list.id)))
            status = doc.createElement('status')
            order_element.appendChild(status)
            status.appendChild(doc.createTextNode(str(order_from_list.status)))
            books = doc.createElement('books')
            order_element.appendChild(books)
            for key, value in order_from_list.books.items():
                book = doc.createElement('book')
                books.appendChild(book)
                title = doc.createElement('title')
                book.appendChild(title)
                title.appendChild(doc.createTextNode(key))
                quantity = doc.createElement('quantity')
                book.appendChild(quantity)
                quantity.appendChild(doc.createTextNode(str(value)))
            places = doc.createElement('places')
            order_element.appendChild(places)
            for item in order_from_list.places:
                place = doc.createElement('place')
                places.appendChild(place)
                place.appendChild(doc.createTextNode(item))
        with open(path, 'w') as file_write:
            file_write.write(doc.toprettyxml())

    @staticmethod
    def read_orders_from_xml_file(path: str, single=True) -> (Order, list):
        """Docstring: Function to read orders from xml file"""
        books, places, output = {}, [], []
        try:
            with parse(path) as xml_doc:
                orders = xml_doc.getElementsByTagName('order')
                for order in orders:
                    order_id = order.getElementsByTagName('id')[0].firstChild.data
                    status = order.getElementsByTagName('status')[0].firstChild.data
                    books_element = order.getElementsByTagName('books')[0]
                    book_list = books_element.getElementsByTagName('book')
                    for book_element in book_list:
                        title = book_element.getElementsByTagName('title')[0].firstChild.data
                        quantity = book_element.getElementsByTagName('quantity')[0].firstChild.data
                        books[title] = int(quantity)
                    places_element = order.getElementsByTagName('places')[0]
                    place_list = places_element.getElementsByTagName('place')
                    for place_element in place_list:
                        place = place_element.firstChild.data
                        places.append(place)
                    if single:
                        output = Order()
                        output.id = order_id
                        output.status = status
                        output.books = books
                        output.places = places
                    else:
                        one_order = Order()
                        one_order.id = order_id
                        one_order.status = status
                        one_order.books = books
                        one_order.places = places
                        output.append(one_order)
                        books = {}
                        places = []
            return output
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Order has not been created from xml file '
                  f'(minidom module)')


class XmlElementTreeOrderFuncs:
    """Docstring: Class with in/out order functions to work with xml files (elementtree)"""

    @staticmethod
    def write_orders_to_xml_file(path: str, order: Order, no_add=True) -> None:
        """Docstring: Function to write or add order to xml file"""
        root = ETree.Element('orders')
        order_list = list()
        order_list.append(order)
        if not no_add:
            order_list += XmlElementTreeOrderFuncs.read_orders_from_xml_file(path, False)
        for order_from_list in order_list:
            order_element = ETree.SubElement(root, 'order')
            order_id = ETree.SubElement(order_element, 'id')
            order_id.text = str(order_from_list.id)
            status = ETree.SubElement(order_element, 'status')
            status.text = order_from_list.status
            books_element = ETree.SubElement(order_element, 'books')
            for key, value in order_from_list.books.items():
                book_element = ETree.SubElement(books_element, 'book')
                title = ETree.SubElement(book_element, 'title')
                title.text = key
                quantity = ETree.SubElement(book_element, 'quantity')
                quantity.text = str(value)
            places_element = ETree.SubElement(order_element, 'places')
            for item in order_from_list.places:
                place_element = ETree.SubElement(places_element, 'place')
                place_element.text = item
        tree = ETree.ElementTree(root)
        with open(path, "wb") as file_write:
            file_write.write(ETree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='utf-8'))

    @staticmethod
    def read_orders_from_xml_file(path: str, single=True) -> (Order, list):
        """Docstring: Function to read orders from xml file"""
        try:
            tree = ET_parse(path)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Order has not been created from xml file '
                  f'(elementtree module)')
        else:
            root = tree.getroot()
            output, title, quantity, order_id, status, books, places = [], '', '', '', '', {}, []
            for element in root.iter():
                if element.tag == 'books' or element.tag == 'places' or element.text.strip() != '':
                    if element.tag == 'id':
                        order_id = element.text
                    if element.tag == 'status':
                        status = element.text
                    if element.tag == 'title':
                        title = element.text
                    if element.tag == 'quantity':
                        quantity = element.text
                    if title != '' and quantity != '':
                        books[title] = quantity
                        title, quantity = '', ''
                    if element.tag == 'place':
                        places.append(element.text)
                if element.tag == 'order' and order_id != '':
                    one_order = Order()
                    one_order.id = order_id
                    one_order.status = status
                    one_order.books = books
                    one_order.places = places
                    output.append(one_order)
                    books, places, order_id, status = {}, [], '', ''
                    continue
            if single:
                output = Order()
                output.id = order_id
                output.status = status
                output.books = books
                output.places = places
            else:
                one_order = Order()
                one_order.id = order_id
                one_order.status = status
                one_order.books = books
                one_order.places = places
                output.append(one_order)
            return output


class JsonModuleOrderFuncs:
    """Docstring: Class with in/out order functions to work with json files (json module)"""

    @staticmethod
    def write_orders_to_json_file(path: str, order: Order, no_add=True) -> None:
        """Docstring: Function to write or add order to json file"""
        simple_obj = {'id': order.id, 'status': order.status, 'books': order.books, 'places': order.places}
        if not no_add:
            output = list()
            output.append(simple_obj)
            order_list = JsonModuleOrderFuncs.read_orders_from_json_file(path, False)
            for order_from_list in order_list:
                temp_order = {'id': order_from_list.id, 'status': order_from_list.status,
                              'books': order_from_list.books, 'places': order_from_list.places}
                output.append(temp_order)
            with open(path, 'w') as file_write:
                json.dump(output, file_write, indent=4)
        else:
            with open(path, 'w') as file_write:
                json.dump(simple_obj, file_write, indent=4)

    @staticmethod
    def read_orders_from_json_file(path: str, single=True) -> (Order, list):
        """Docstring: Function to read orders from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                income = json.load(file_read)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Order has not been created from json file '
                  f'(json module)')
        else:
            if single:
                output = Order()
                output.id = income['id']
                output.status = income['status']
                output.books = income['books']
                output.places = income['places']
            else:
                if type(income) == dict:
                    some_order = Order()
                    some_order.id = income['id']
                    some_order.status = income['status']
                    some_order.books = income['books']
                    some_order.places = income['places']
                    output.append(some_order)
                else:
                    for order_from_list in income:
                        some_order = Order()
                        some_order.id = order_from_list['id']
                        some_order.status = order_from_list['status']
                        some_order.books = order_from_list['books']
                        some_order.places = order_from_list['places']
                        output.append(some_order)
            return output


class OrjsonModuleOrderFuncs:
    """Docstring: Class with in/out order functions to work with json files (orjson module)"""

    @staticmethod
    def write_orders_to_json_file(path: str, order: Order, no_add=True) -> None:
        """Docstring: Function to write or add order to json file"""
        simple_obj = {'id': order.id, 'status': order.status, 'books': order.books, 'places': order.places}
        if not no_add:
            output = list()
            output.append(simple_obj)
            order_list = OrjsonModuleOrderFuncs.read_orders_from_json_file(path, False)
            for order_from_list in order_list:
                temp_order = {'id': order_from_list.id, 'status': order_from_list.status,
                              'books': order_from_list.books, 'places': order_from_list.places}
                output.append(temp_order)
            with open(path, 'wb') as file_write:
                text = orjson.dumps(output, option=orjson.OPT_INDENT_2)
                file_write.write(text)
        else:
            with open(path, 'wb') as file_write:
                text = orjson.dumps(simple_obj, option=orjson.OPT_INDENT_2)
                file_write.write(text)

    @staticmethod
    def read_orders_from_json_file(path: str, single=True) -> (Order, list):
        """Docstring: Function to read orders from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                text = file_read.read()
                income = orjson.loads(text)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Order has not been created from json file '
                  f'(orjson module)')
        else:
            if single:
                output = Order()
                output.id = income['id']
                output.status = income['status']
                output.books = income['books']
                output.places = income['places']
            else:
                if type(income) == dict:
                    some_order = Order()
                    some_order.id = income['id']
                    some_order.status = income['status']
                    some_order.books = income['books']
                    some_order.places = income['places']
                    output.append(some_order)
                else:
                    for order_from_list in income:
                        some_order = Order()
                        some_order.id = order_from_list['id']
                        some_order.status = order_from_list['status']
                        some_order.books = order_from_list['books']
                        some_order.places = order_from_list['places']
                        output.append(some_order)
            return output


class JsonPickleOrderFuncs:
    """Docstring: Class with in/out order functions to work with json files (jsonpickle module)"""

    @staticmethod
    def write_orders_to_json_file(path: str, order: Order, no_add=True) -> None:
        """Docstring: Function to write or add order to json file"""
        simple_obj = {'id': order.id, 'status': order.status, 'books': order.books, 'places': order.places}
        if not no_add:
            output = list()
            output.append(simple_obj)
            order_list = OrjsonModuleOrderFuncs.read_orders_from_json_file(path, False)
            for order_from_list in order_list:
                temp_order = {'id': order_from_list.id, 'status': order_from_list.status,
                              'books': order_from_list.books, 'places': order_from_list.places}
                output.append(temp_order)
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
    def read_orders_from_json_file(path: str, single=True) -> (Order, list):
        """Docstring: Function to read orders from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                text = file_read.read()
                income = jsonpickle.decode(text)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Order has not been created from json file '
                  f'(jsonpickle module)')
        else:
            if single:
                output = Order()
                output.id = income['id']
                output.status = income['status']
                output.books = income['books']
                output.places = income['places']
            else:
                if type(income) == dict:
                    some_order = Order()
                    some_order.id = income['id']
                    some_order.status = income['status']
                    some_order.books = income['books']
                    some_order.places = income['places']
                    output.append(some_order)
                else:
                    for order_from_list in income:
                        some_order = Order()
                        some_order.id = order_from_list['id']
                        some_order.status = order_from_list['status']
                        some_order.books = order_from_list['books']
                        some_order.places = order_from_list['places']
                        output.append(some_order)
            return output


class XmlSaxReadOrderFuncs(ContentHandler):
    """Docstring: Class with in/out order functions to work with xml files (SAX)"""

    def __init__(self) -> None:
        """Docstring: Constructor for class XmlSaxReadOrderFuncs extends ContentHandler"""
        super().__init__()
        self.CurrentData = ''
        self.orders = []
        self.order = Order()
        self.order.id = ''
        self.title = ''

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def characters(self, content: str) -> None:
        """Docstring: Content list making method"""
        if content.strip() != "":
            if self.CurrentData == 'id':
                if self.order.id != '':
                    self.orders.append(self.order)
                    self.order = Order()
                    self.order.id = content
                else:
                    self.order.id = content
            if self.CurrentData == 'status':
                self.order.status = content
            if self.CurrentData == 'title':
                self.title = content
            if self.CurrentData == 'quantity':
                self.order.books[self.title] = content
            if self.CurrentData == 'place':
                self.order.places.append(content)

    def get_orders(self) -> list:
        """Docstring: Getter for orders"""
        self.orders.append(self.order)
        return self.orders

    @staticmethod
    def read_orders_from_xml_file(path: str) -> (Order, list):
        """Docstring: Function to read books from xml file"""
        handler = XmlSaxReadOrderFuncs()
        try:
            SAX_parse(path, handler)
        except ValueError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Order has not been created from xml file '
                  f'(sax)')
        else:
            order_list = handler.get_orders()
            if len(order_list) == 1:
                return order_list[0]
            else:
                return order_list

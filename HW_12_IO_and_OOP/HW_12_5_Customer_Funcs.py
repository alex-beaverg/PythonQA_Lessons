# Homework 12, file 5 - (2023.07.13)
# Homework. Customer Functions

import pickle
import json
import orjson
import jsonpickle
from xml.dom.minidom import parse, parseString
from xml.etree.ElementTree import parse as ET_parse
from lxml import etree as ETree
from xml.sax import parse as SAX_parse
from xml.sax.handler import ContentHandler
from HW_12_2_Classes import Customer


class TxtCustomerFuncs:
    """Docstring: Class with in/out customer functions to work with txt files"""

    @staticmethod
    def write_customers_to_text_file(path: str, customer: Customer, mode='w') -> None:
        """Docstring: Function to write or add customer to text file"""
        with open(path, mode) as file_write:
            file_write.write(customer.name + '\n')
            file_write.write(customer.surname + '\n')
            file_write.write(customer.sex + '\n')
            file_write.write(str(customer.age) + '\n')
            for address_type, address in customer.addresses.items():
                file_write.write(address_type + '\n')
                file_write.write(address + '\n')
            file_write.write(customer.phone + '\n')
            file_write.write(customer.email + '\n')
            for order_id, status in customer.orders.items():
                file_write.write(str(order_id) + '\n')
                file_write.write(status + '\n')
            file_write.write('\n')

    @staticmethod
    def read_customers_from_text_file(path: str, single=True) -> (Customer, list):
        """Docstring: Function to read customers from text file"""
        lines = []
        customers = []
        customer = Customer('', '', '', 0, {}, '', '')
        try:
            with open(path, 'r') as file_read:
                for line in file_read:
                    lines.append(line.strip())
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Customer has not been created from text file')
        else:
            i = 0
            while i < len(lines):
                customer.name = lines[i]
                i += 1
                customer.surname = lines[i]
                i += 1
                customer.sex = lines[i]
                i += 1
                customer.age = lines[i]
                i += 1
                customer.addresses[lines[i]] = lines[i + 1]
                i += 2
                customer.addresses[lines[i]] = lines[i + 1]
                i += 2
                customer.phone = lines[i]
                i += 1
                customer.email = lines[i]
                i += 1
                while True:
                    if i == len(lines) or lines[i] == '':
                        i += 1
                        break
                    else:
                        customer.orders[lines[i]] = lines[i + 1]
                        i += 2
                if not single:
                    customers.append(customer)
                    customer = Customer('', '', '', 0, {}, '', '')
            if single:
                return customer
            else:
                return customers


class BinCustomerFuncs:
    """Docstring: Class with in/out customer functions to work with binary files"""

    @staticmethod
    def write_customers_to_binary_file(path: str, customer: Customer, mode='wb') -> None:
        """Docstring: Function to write or add customer to binary file"""
        with open(path, mode) as file_write:
            pickle.dump(customer, file_write)

    @staticmethod
    def read_customers_from_binary_file(path: str, single=True) -> (Customer, list):
        """Docstring: Function to read customers from binary file"""
        try:
            if single:
                with open(path, 'rb') as file_read:
                    output = pickle.load(file_read)
            else:
                output = []
                with open(path, 'rb') as file_read:
                    while True:
                        try:
                            customer = pickle.load(file_read)
                        except EOFError:
                            break
                        else:
                            output.append(customer)
            return output
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Customer has not been created from binary '
                  f'file')


class XmlMiniDomCustomerFuncs:
    """Docstring: Class with in/out customer functions to work with xml files (minidom)"""

    @staticmethod
    def write_customers_to_xml_file(path: str, customer: Customer, no_add=True) -> None:
        """Docstring: Function to write or add customer to xml file"""
        doc = parseString('<customers/>')
        root = doc.documentElement
        customer_list = list()
        customer_list.append(customer)
        if not no_add:
            customer_list += XmlMiniDomCustomerFuncs.read_customers_from_xml_file(path, False)
        for customer_from_list in customer_list:
            customer_element = doc.createElement('customer')
            root.appendChild(customer_element)
            name = doc.createElement('name')
            customer_element.appendChild(name)
            name.appendChild(doc.createTextNode(customer_from_list.name))
            surname = doc.createElement('surname')
            customer_element.appendChild(surname)
            surname.appendChild(doc.createTextNode(customer_from_list.surname))
            sex = doc.createElement('sex')
            customer_element.appendChild(sex)
            sex.appendChild(doc.createTextNode(customer_from_list.sex))
            age = doc.createElement('age')
            customer_element.appendChild(age)
            age.appendChild(doc.createTextNode(str(customer_from_list.age)))
            addresses = doc.createElement('addresses')
            customer_element.appendChild(addresses)
            for key, value in customer_from_list.addresses.items():
                address = doc.createElement('address')
                addresses.appendChild(address)
                address_type = doc.createElement('type')
                address.appendChild(address_type)
                address_type.appendChild(doc.createTextNode(key))
                address_text = doc.createElement('text')
                address.appendChild(address_text)
                address_text.appendChild(doc.createTextNode(value))
            phone = doc.createElement('phone')
            customer_element.appendChild(phone)
            phone.appendChild(doc.createTextNode(customer_from_list.phone))
            email = doc.createElement('email')
            customer_element.appendChild(email)
            email.appendChild(doc.createTextNode(customer_from_list.email))
            orders = doc.createElement('orders')
            customer_element.appendChild(orders)
            for key, value in customer_from_list.orders.items():
                order = doc.createElement('order')
                orders.appendChild(order)
                order_id = doc.createElement('id')
                order.appendChild(order_id)
                order_id.appendChild(doc.createTextNode(key))
                status = doc.createElement('status')
                order.appendChild(status)
                status.appendChild(doc.createTextNode(value))
        with open(path, 'w') as file_write:
            file_write.write(doc.toprettyxml())

    @staticmethod
    def read_customers_from_xml_file(path: str, single=True) -> (Customer, list):
        """Docstring: Function to read customers from xml file"""
        addresses, orders, output = {}, {}, []
        try:
            with parse(path) as xml_doc:
                customers = xml_doc.getElementsByTagName('customer')
                for customer in customers:
                    name = customer.getElementsByTagName('name')[0].firstChild.data
                    surname = customer.getElementsByTagName('surname')[0].firstChild.data
                    sex = customer.getElementsByTagName('sex')[0].firstChild.data
                    age = customer.getElementsByTagName('age')[0].firstChild.data

                    addresses_element = customer.getElementsByTagName('addresses')[0]
                    address_list = addresses_element.getElementsByTagName('address')
                    for address_element in address_list:
                        address_type = address_element.getElementsByTagName('type')[0].firstChild.data
                        address_text = address_element.getElementsByTagName('text')[0].firstChild.data
                        addresses[address_type] = address_text
                    phone = customer.getElementsByTagName('phone')[0].firstChild.data
                    email = customer.getElementsByTagName('email')[0].firstChild.data

                    orders_element = customer.getElementsByTagName('orders')[0]
                    order_list = orders_element.getElementsByTagName('order')
                    for order_element in order_list:
                        order_id = order_element.getElementsByTagName('id')[0].firstChild.data
                        status = order_element.getElementsByTagName('status')[0].firstChild.data
                        orders[order_id] = status
                    if single:
                        output = Customer(name, surname, sex, age, addresses, phone, email)
                        output.orders = orders
                    else:
                        one_customer = Customer(name, surname, sex, age, addresses, phone, email)
                        one_customer.orders = orders
                        output.append(one_customer)
                        addresses, orders = {}, {}
            return output
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Customer has not been created from xml file '
                  f'(minidom module)')


class XmlElementTreeCustomerFuncs:
    """Docstring: Class with in/out customer functions to work with xml files (elementtree)"""

    @staticmethod
    def write_customers_to_xml_file(path: str, customer: Customer, no_add=True) -> None:
        """Docstring: Function to write or add customer to xml file"""
        root = ETree.Element('customers')
        customer_list = list()
        customer_list.append(customer)
        if not no_add:
            customer_list += XmlElementTreeCustomerFuncs.read_customers_from_xml_file(path, False)
        for customer_from_list in customer_list:
            customer_element = ETree.SubElement(root, 'customer')
            name = ETree.SubElement(customer_element, 'name')
            name.text = customer_from_list.name
            surname = ETree.SubElement(customer_element, 'surname')
            surname.text = customer_from_list.surname
            sex = ETree.SubElement(customer_element, 'sex')
            sex.text = customer_from_list.sex
            age = ETree.SubElement(customer_element, 'age')
            age.text = str(customer_from_list.age)
            addresses_element = ETree.SubElement(customer_element, 'addresses')
            for key, value in customer_from_list.addresses.items():
                address_element = ETree.SubElement(addresses_element, 'address')
                address_type = ETree.SubElement(address_element, 'type')
                address_type.text = key
                address_text = ETree.SubElement(address_element, 'text')
                address_text.text = value
            phone = ETree.SubElement(customer_element, 'phone')
            phone.text = customer_from_list.phone
            email = ETree.SubElement(customer_element, 'email')
            email.text = customer_from_list.email
            orders_element = ETree.SubElement(customer_element, 'orders')
            for key, value in customer_from_list.orders.items():
                order_element = ETree.SubElement(orders_element, 'order')
                order_id = ETree.SubElement(order_element, 'id')
                order_id.text = key
                status = ETree.SubElement(order_element, 'status')
                status.text = value
        tree = ETree.ElementTree(root)
        with open(path, "wb") as file_write:
            file_write.write(ETree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='utf-8'))

    @staticmethod
    def read_customers_from_xml_file(path: str, single=True) -> (Customer, list):
        """Docstring: Function to read customers from xml file"""
        try:
            tree = ET_parse(path)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Customer has not been created from xml file '
                  f'(elementtree module)')
        else:
            root = tree.getroot()
            output, age, addresses, orders = [], 0, {}, {}
            name, surname, sex, phone, email, addr_type, addr_text, order_id, status = '', '', '', '', '', '', '', '', ''
            for element in root.iter():
                if element.tag == 'orders' or element.text.strip() != '':
                    if element.tag == 'name':
                        name = element.text
                    if element.tag == 'surname':
                        surname = element.text
                    if element.tag == 'sex':
                        sex = element.text
                    if element.tag == 'age':
                        age = element.text
                    if element.tag == 'type':
                        addr_type = element.text
                    if element.tag == 'text':
                        addr_text = element.text
                    if addr_type != '' and addr_text != '':
                        addresses[addr_type] = addr_text
                        addr_type, addr_text = '', ''
                    if element.tag == 'phone':
                        phone = element.text
                    if element.tag == 'email':
                        email = element.text
                    if element.tag == 'id':
                        order_id = element.text
                    if element.tag == 'status':
                        status = element.text
                    if order_id != '' and status != '':
                        orders[order_id] = status
                        order_id, status = '', ''
                if element.tag == 'customer' and name != '':
                    one_customer = Customer(name, surname, sex, age, addresses, phone, email)
                    one_customer.orders = orders
                    output.append(one_customer)
                    name, surname, sex, phone, email, age, addresses, orders = '', '', '', '', '', 0, {}, {}
                    continue
            if single:
                output = Customer(name, surname, sex, age, addresses, phone, email)
                output.orders = orders
            else:
                one_customer = Customer(name, surname, sex, age, addresses, phone, email)
                one_customer.orders = orders
                output.append(one_customer)
            return output


class JsonModuleCustomerFuncs:
    """Docstring: Class with in/out customer functions to work with json files (json module)"""

    @staticmethod
    def write_customers_to_json_file(path: str, customer: Customer, no_add=True) -> None:
        """Docstring: Function to write or add customer to json file"""
        simple_obj = {'name': customer.name, 'surname': customer.surname, 'sex': customer.sex, 'age': customer.age,
                      'addresses': customer.addresses, 'phone': customer.phone, 'email': customer.email,
                      'orders': customer.orders}
        if not no_add:
            output = list()
            output.append(simple_obj)
            customer_list = JsonModuleCustomerFuncs.read_customers_from_json_file(path, False)
            for customer_from_list in customer_list:
                temp_customer = {'name': customer_from_list.name, 'surname': customer_from_list.surname,
                                 'sex': customer_from_list.sex, 'age': customer_from_list.age,
                                 'addresses': customer_from_list.addresses, 'phone': customer_from_list.phone,
                                 'email': customer_from_list.email, 'orders': customer_from_list.orders}
                output.append(temp_customer)
            with open(path, 'w') as file_write:
                json.dump(output, file_write, indent=4)
        else:
            with open(path, 'w') as file_write:
                json.dump(simple_obj, file_write, indent=4)

    @staticmethod
    def read_customers_from_json_file(path: str, single=True) -> (Customer, list):
        """Docstring: Function to read customers from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                income = json.load(file_read)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Customer has not been created from json file '
                  f'(json module)')
        else:
            if single:
                output = Customer(income['name'], income['surname'], income['sex'], income['age'], income['addresses'],
                                  income['phone'], income['email'])
                output.orders = income['orders']
            else:
                if type(income) == dict:
                    some_customer = Customer(income['name'], income['surname'], income['sex'], income['age'],
                                             income['addresses'], income['phone'], income['email'])
                    some_customer.orders = income['orders']
                    output.append(some_customer)
                else:
                    for customer_from_list in income:
                        some_customer = Customer(customer_from_list['name'], customer_from_list['surname'],
                                                 customer_from_list['sex'], customer_from_list['age'],
                                                 customer_from_list['addresses'], customer_from_list['phone'],
                                                 customer_from_list['email'])
                        some_customer.orders = customer_from_list['orders']
                        output.append(some_customer)
            return output


class OrjsonModuleCustomerFuncs:
    """Docstring: Class with in/out customer functions to work with json files (orjson module)"""

    @staticmethod
    def write_customers_to_json_file(path: str, customer: Customer, no_add=True) -> None:
        """Docstring: Function to write or add customer to json file"""
        simple_obj = {'name': customer.name, 'surname': customer.surname, 'sex': customer.sex, 'age': customer.age,
                      'addresses': customer.addresses, 'phone': customer.phone, 'email': customer.email,
                      'orders': customer.orders}
        if not no_add:
            output = list()
            output.append(simple_obj)
            customer_list = OrjsonModuleCustomerFuncs.read_customers_from_json_file(path, False)
            for customer_from_list in customer_list:
                temp_customer = {'name': customer_from_list.name, 'surname': customer_from_list.surname,
                                 'sex': customer_from_list.sex, 'age': customer_from_list.age,
                                 'addresses': customer_from_list.addresses, 'phone': customer_from_list.phone,
                                 'email': customer_from_list.email, 'orders': customer_from_list.orders}
                output.append(temp_customer)
            with open(path, 'wb') as file_write:
                text = orjson.dumps(output, option=orjson.OPT_INDENT_2)
                file_write.write(text)
        else:
            with open(path, 'wb') as file_write:
                text = orjson.dumps(simple_obj, option=orjson.OPT_INDENT_2)
                file_write.write(text)

    @staticmethod
    def read_customers_from_json_file(path: str, single=True) -> (Customer, list):
        """Docstring: Function to read customers from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                text = file_read.read()
                income = orjson.loads(text)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Customer has not been created from json file '
                  f'(orjson module)')
        else:
            if single:
                output = Customer(income['name'], income['surname'], income['sex'], income['age'], income['addresses'],
                                  income['phone'], income['email'])
                output.orders = income['orders']
            else:
                if type(income) == dict:
                    some_customer = Customer(income['name'], income['surname'], income['sex'], income['age'],
                                             income['addresses'], income['phone'], income['email'])
                    some_customer.orders = income['orders']
                    output.append(some_customer)
                else:
                    for customer_from_list in income:
                        some_customer = Customer(customer_from_list['name'], customer_from_list['surname'],
                                                 customer_from_list['sex'], customer_from_list['age'],
                                                 customer_from_list['addresses'], customer_from_list['phone'],
                                                 customer_from_list['email'])
                        some_customer.orders = customer_from_list['orders']
                        output.append(some_customer)
            return output


class JsonPickleCustomerFuncs:
    """Docstring: Class with in/out customer functions to work with json files (jsonpickle module)"""

    @staticmethod
    def write_customers_to_json_file(path: str, customer: Customer, no_add=True) -> None:
        """Docstring: Function to write or add customer to json file"""
        simple_obj = {'name': customer.name, 'surname': customer.surname, 'sex': customer.sex, 'age': customer.age,
                      'addresses': customer.addresses, 'phone': customer.phone, 'email': customer.email,
                      'orders': customer.orders}
        if not no_add:
            output = list()
            output.append(simple_obj)
            customer_list = OrjsonModuleCustomerFuncs.read_customers_from_json_file(path, False)
            for customer_from_list in customer_list:
                temp_customer = {'name': customer_from_list.name, 'surname': customer_from_list.surname,
                                 'sex': customer_from_list.sex, 'age': customer_from_list.age,
                                 'addresses': customer_from_list.addresses, 'phone': customer_from_list.phone,
                                 'email': customer_from_list.email, 'orders': customer_from_list.orders}
                output.append(temp_customer)
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
    def read_customers_from_json_file(path: str, single=True) -> (Customer, list):
        """Docstring: Function to read customers from json file"""
        output = []
        try:
            with open(path, 'r') as file_read:
                text = file_read.read()
                income = jsonpickle.decode(text)
        except FileNotFoundError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Customer has not been created from json file '
                  f'(jsonpickle module)')
        else:
            if single:
                output = Customer(income['name'], income['surname'], income['sex'], income['age'], income['addresses'],
                                  income['phone'], income['email'])
                output.orders = income['orders']
            else:
                if type(income) == dict:
                    some_customer = Customer(income['name'], income['surname'], income['sex'], income['age'],
                                             income['addresses'], income['phone'], income['email'])
                    some_customer.orders = income['orders']
                    output.append(some_customer)
                else:
                    for customer_from_list in income:
                        some_customer = Customer(customer_from_list['name'], customer_from_list['surname'],
                                                 customer_from_list['sex'], customer_from_list['age'],
                                                 customer_from_list['addresses'], customer_from_list['phone'],
                                                 customer_from_list['email'])
                        some_customer.orders = customer_from_list['orders']
                        output.append(some_customer)
            return output


class XmlSaxReadCustomerFuncs(ContentHandler):
    """Docstring: Class with in/out customer functions to work with xml files (SAX)"""

    def __init__(self) -> None:
        """Docstring: Constructor for class XmlSaxReadCustomerFuncs extends ContentHandler"""
        super().__init__()
        self.CurrentData = ''
        self.customers = []
        self.customer = Customer('', '', '', 0, {}, '', '')
        self.type = ''
        self.order_id = ''

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def characters(self, content: str) -> None:
        """Docstring: Content list making method"""
        if content.strip() != "":
            if self.CurrentData == 'name':
                if self.customer.name != '':
                    self.customers.append(self.customer)
                    self.customer = Customer('', '', '', 0, {}, '', '')
                    self.customer.name = content
                else:
                    self.customer.name = content
            if self.CurrentData == 'surname':
                self.customer.surname = content
            if self.CurrentData == 'sex':
                self.customer.sex = content
            if self.CurrentData == 'age':
                self.customer.age = content
            if self.CurrentData == 'type':
                self.type = content
            if self.CurrentData == 'text':
                self.customer.addresses[self.type] = content
            if self.CurrentData == 'phone':
                self.customer.phone = content
            if self.CurrentData == 'email':
                self.customer.email = content
            if self.CurrentData == 'id':
                self.order_id = content
            if self.CurrentData == 'status':
                self.customer.orders[self.order_id] = content

    def get_customers(self) -> list:
        """Docstring: Getter for customers"""
        self.customers.append(self.customer)
        return self.customers

    @staticmethod
    def read_customers_from_xml_file(path: str) -> (Customer, list):
        """Docstring: Function to read books from xml file"""
        handler = XmlSaxReadCustomerFuncs()
        try:
            SAX_parse(path, handler)
        except ValueError:
            print(f'[ERROR]: No such file or directory: "{path}". Object Customer has not been created from xml file '
                  f'(sax)')
        else:
            customer_list = handler.get_customers()
            if len(customer_list) == 1:
                return customer_list[0]
            else:
                return customer_list

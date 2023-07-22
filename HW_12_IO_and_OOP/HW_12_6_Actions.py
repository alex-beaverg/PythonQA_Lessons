# Homework 12, file 6 - (2023.07.13)
# Homework. Actions

from HW_12_2_Classes import *
from HW_12_3_Book_Funcs import *
from HW_12_4_Order_Funcs import *
from HW_12_5_Customer_Funcs import *

# ----------------------
# ACTIONS WITH OBJECTS 1:
# Create books:
book_1 = Book('Chip and Dale', 'Dont Know', 25, 35)
book_2 = Book('Three mini pigs', 'Dont Know 2nd', 12, 10)
book_3 = Book('Bad guys II', 'Michael Bay', 23, 29)

print('\nBooks after creating them:')
book_1.print_information()
book_2.print_information()
print()

book_shop_1 = BookShop('Book Shop 1')
book_shop_1.add_book(book_1)
book_shop_1.add_book(book_2)

book_shop_2 = BookShop('Book Shop 2')
book_shop_2.add_book(book_1)
book_shop_2.add_book(book_1)
book_shop_2.add_book(book_3)

book_stock_1 = BookStock('Book Stock 1')
book_stock_1.add_book(book_3)
book_stock_1.add_book(book_2)
book_stock_1.add_book(book_1)

print('\nBooks after adding them to shops and stocks:')
book_1.print_information()
book_2.print_information()
print()

# -------------------------------------
# ACTIONS (I/O) WITH TEXT FILES (BOOKS):
path_books_text = 'files/res_01_book/BOOKS_TEXT.txt'
# Create text file with book:
TxtBookFuncs.write_books_to_text_file(path_books_text, book_1)

# Read text file with book:
book_1a = TxtBookFuncs.read_books_from_text_file(path_books_text)
print('Book from text file:')
book_1a.print_information()

# Add another book to text file:
TxtBookFuncs.write_books_to_text_file(path_books_text, book_2, 'a')

# Read text file with books:
books_1 = TxtBookFuncs.read_books_from_text_file(path_books_text, False)
print('\n2 books from text file:')
for book in books_1:
    book.print_information()
print()

# ---------------------------------------
# ACTIONS (I/O) WITH BINARY FILES (BOOKS):
path_books_binary = 'files/res_01_book/BOOKS_BINARY.binary'
# Create binary file with book:
BinBookFuncs.write_books_to_binary_file(path_books_binary, book_1)

# Read binary file with book:
book_1b = BinBookFuncs.read_books_from_binary_file(path_books_binary)
print('Book from binary file:')
book_1b.print_information()

# Add another book to binary file:
BinBookFuncs.write_books_to_binary_file(path_books_binary, book_2, 'ab')

# Read binary file with books:
books_2 = BinBookFuncs.read_books_from_binary_file(path_books_binary, False)
print('\n2 books from binary file:')
for book in books_2:
    book.print_information()
print()

# ----------------------------------------------
# ACTIONS (I/O) WITH XML FILES (MINIDOM) (BOOKS):
path_books_xml_md = 'files/res_01_book/BOOKS_XML_MD.xml'
# Create xml file with book:
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md, book_1)

# Read xml file with book:
book_1c = XmlMiniDomBookFuncs.read_books_from_xml_file(path_books_xml_md)
print('Book from xml file (minidom):')
book_1c.print_information()

# Add another book to xml file:
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md, book_2, False)

# Read xml file with books:
books_3 = XmlMiniDomBookFuncs.read_books_from_xml_file(path_books_xml_md, False)
print('\n2 books from xml file (minidom):')
for book in books_3:
    book.print_information()
print()

# --------------------------------------------------
# ACTIONS (I/O) WITH XML FILES (ELEMENTTREE) (BOOKS):
path_books_xml_et = 'files/res_01_book/BOOKS_XML_ET.xml'
# Create xml file with book:
XmlElementTreeBookFuncs.write_books_to_xml_file(path_books_xml_et, book_1)

# Read xml file with book:
book_1d = XmlElementTreeBookFuncs.read_books_from_xml_file(path_books_xml_et)
print('Book from xml file (elementtree):')
book_1d.print_information()

# Add another book to xml file:
XmlElementTreeBookFuncs.write_books_to_xml_file(path_books_xml_et, book_2, False)

# Read xml file with books:
books_4 = XmlElementTreeBookFuncs.read_books_from_xml_file(path_books_xml_et, False)
print('\n2 books from xml file (elementtree):')
for book in books_4:
    book.print_information()
print()

# ---------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (JSON MODULE) (BOOKS):
path_books_json = 'files/res_01_book/BOOKS_JSON.json'
# Create json file with book:
JsonModuleBookFuncs.write_books_to_json_file(path_books_json, book_1)

# Read json file with book:
book_1e = JsonModuleBookFuncs.read_books_from_json_file(path_books_json)
print('Book from json file:')
book_1e.print_information()

# Add another book to json file:
JsonModuleBookFuncs.write_books_to_json_file(path_books_json, book_2, False)

# Read json file with books:
books_5 = JsonModuleBookFuncs.read_books_from_json_file(path_books_json, False)
print('\n2 books from json file:')
for book in books_5:
    book.print_information()
print()

# -----------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (ORJSON MODULE) (BOOKS):
path_books_json_or = 'files/res_01_book/BOOKS_JSON_OR.json'
# Create json file with book:
OrjsonModuleBookFuncs.write_books_to_json_file(path_books_json_or, book_1)

# Read json file with book:
book_1f = OrjsonModuleBookFuncs.read_books_from_json_file(path_books_json_or)
print('Book from json file (orjson):')
book_1f.print_information()

# Add another book to json file:
OrjsonModuleBookFuncs.write_books_to_json_file(path_books_json_or, book_2, False)

# Read json file with books:
books_6 = OrjsonModuleBookFuncs.read_books_from_json_file(path_books_json_or, False)
print('\n2 books from json file (orjson):')
for book in books_6:
    book.print_information()
print()

# -----------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (JSON PICKLE) (BOOKS):
path_books_json_p = 'files/res_01_book/BOOKS_JSON_P.json'
# Create json file with book:
JsonPickleBookFuncs.write_books_to_json_file(path_books_json_p, book_1)

# Read json file with book:
book_1g = JsonPickleBookFuncs.read_books_from_json_file(path_books_json_p)
print('Book from json file (jsonpickle):')
book_1g.print_information()

# Add another book to json file:
JsonPickleBookFuncs.write_books_to_json_file(path_books_json_p, book_2, False)

# Read json file with books:
books_7 = JsonPickleBookFuncs.read_books_from_json_file(path_books_json_p, False)
print('\n2 books from json file (jsonpickle):')
for book in books_7:
    book.print_information()
print()

# ----------------------
# ACTIONS WITH OBJECTS 2:
# Create orders:
order_1 = Order()
order_1.add_book(book_2, 4)
order_1.add_book(book_1)
order_1.add_book(book_1)
print('Order after adding books:')
order_1.print_information()

order_1.change_status()
print('\nOrder after change status:')
order_1.print_information()

order_2 = Order()
order_2.add_book(book_3, 3)
order_2.add_book(book_1, 5)
order_2.add_book(book_2)
print('\nOrder after adding books:')
order_2.print_information()

# --------------------------------------
# ACTIONS (I/O) WITH TEXT FILES (ORDERS):
path_orders_text = 'files/res_02_order/ORDERS_TEXT.txt'
# Create text file with order:
TxtOrderFuncs.write_orders_to_text_file(path_orders_text, order_1)

# Read text file with order:
order_1a = TxtOrderFuncs.read_orders_from_text_file(path_orders_text)
print('\nOrder from text file:')
order_1a.print_information()

# Add another order to text file:
TxtOrderFuncs.write_orders_to_text_file(path_orders_text, order_2, 'a')

# Read text file with orders:
orders_1 = TxtOrderFuncs.read_orders_from_text_file(path_orders_text, False)
print('\n2 orders from text file:')
for order in orders_1:
    order.print_information()
print()

# ----------------------------------------
# ACTIONS (I/O) WITH BINARY FILES (ORDERS):
path_orders_binary = 'files/res_02_order/ORDERS_BINARY.binary'
# Create binary file with order:
BinOrderFuncs.write_orders_to_binary_file(path_orders_binary, order_1)

# Read binary file with order:
order_1b = BinOrderFuncs.read_orders_from_binary_file(path_orders_binary)
print('Order from binary file:')
order_1b.print_information()

# Add another order to binary file:
BinOrderFuncs.write_orders_to_binary_file(path_orders_binary, order_2, 'ab')

# Read binary file with orders:
orders_2 = BinOrderFuncs.read_orders_from_binary_file(path_orders_binary, False)
print('\n2 orders from binary file:')
for order in orders_2:
    order.print_information()
print()

# -----------------------------------------------
# ACTIONS (I/O) WITH XML FILES (MINIDOM) (ORDERS):
path_orders_xml_md = 'files/res_02_order/ORDERS_XML_MD.xml'
# Create xml file with order:
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md, order_1)

# Read xml file with order:
order_1c = XmlMiniDomOrderFuncs.read_orders_from_xml_file(path_orders_xml_md)
print('Order from xml file (minidom):')
order_1c.print_information()

# Add another order to xml file:
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md, order_2, False)

# Read xml file with orders:
orders_3 = XmlMiniDomOrderFuncs.read_orders_from_xml_file(path_orders_xml_md, False)
print('\n2 orders from xml file (minidom):')
for order in orders_3:
    order.print_information()
print()

# ---------------------------------------------------
# ACTIONS (I/O) WITH XML FILES (ELEMENTTREE) (ORDERS):
path_orders_xml_et = 'files/res_02_order/ORDERS_XML_ET.xml'
# Create xml file with order:
XmlElementTreeOrderFuncs.write_orders_to_xml_file(path_orders_xml_et, order_1)

# Read xml file with order:
order_1d = XmlElementTreeOrderFuncs.read_orders_from_xml_file(path_orders_xml_et)
print('Order from xml file (elementtree):')
order_1d.print_information()

# Add another order to xml file:
XmlElementTreeOrderFuncs.write_orders_to_xml_file(path_orders_xml_et, order_2, False)

# Read xml file with orders:
orders_4 = XmlElementTreeOrderFuncs.read_orders_from_xml_file(path_orders_xml_et, False)
print('\n2 orders from xml file (elementtree):')
for order in orders_4:
    order.print_information()
print()

# ----------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (JSON MODULE) (ORDERS):
path_orders_json = 'files/res_02_order/ORDERS_JSON.json'
# Create json file with order:
JsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json, order_1)

# Read json file with order:
order_1e = JsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json)
print('Order from json file:')
order_1e.print_information()

# Add another order to json file:
JsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json, order_2, False)

# Read json file with orders:
orders_5 = JsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json, False)
print('\n2 orders from json file:')
for order in orders_5:
    order.print_information()
print()

# ------------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (ORJSON MODULE) (ORDERS):
path_orders_json_or = 'files/res_02_order/ORDERS_JSON_OR.json'
# Create json file with order:
OrjsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_or, order_1)

# Read json file with order:
order_1f = OrjsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json_or)
print('Order from json file (orjson):')
order_1f.print_information()

# Add another order to json file:
OrjsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_or, order_2, False)

# Read json file with orders:
orders_6 = OrjsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json_or, False)
print('\n2 orders from json file (orjson):')
for order in orders_6:
    order.print_information()
print()

# ----------------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (JSONPICKLE MODULE) (ORDERS):
path_orders_json_p = 'files/res_02_order/ORDERS_JSON_P.json'
# Create json file with order:
JsonPickleOrderFuncs.write_orders_to_json_file(path_orders_json_p, order_1)

# Read json file with order:
order_1g = JsonPickleOrderFuncs.read_orders_from_json_file(path_orders_json_p)
print('Order from json file (jsonpickle):')
order_1g.print_information()

# Add another order to json file:
JsonPickleOrderFuncs.write_orders_to_json_file(path_orders_json_p, order_2, False)

# Read json file with orders:
orders_7 = JsonPickleOrderFuncs.read_orders_from_json_file(path_orders_json_p, False)
print('\n2 orders from json file (jsonpickle):')
for order in orders_7:
    order.print_information()
print()

# ----------------------
# ACTIONS WITH OBJECTS 3:
# Create customers:
customer_1 = Customer('John', 'Black', 'M', 25, {'Primary': 'Seattle', 'Secondary': 'New York'}, '+555-12-355-55-55',
                      'j.black@usmail.com')
customer_2 = Customer('Alex', 'Smith', 'M', 33, {'Primary': 'Chicago', 'Secondary': 'Toronto'}, '+578-19-122-33-55',
                      'a.smith@usmail.com')
customer_3 = Customer('Kate', 'Johnson', 'F', 29, {'Primary': 'Austin', 'Secondary': 'Montreal'}, '+529-23-366-44-11',
                      'k.johnson@usmail.com')

print('Customer after creating him:')
customer_1.print_information()

customer_1.add_order(order_1a)
customer_1.add_order(order_2)
customer_2.add_order(order_2)
customer_2.add_order(order_1)
customer_3.add_order(order_1e)

print('\nCustomer after adding orders:')
customer_1.print_information()

# -----------------------------------------
# ACTIONS (I/O) WITH TEXT FILES (CUSTOMERS):
path_customers_text = 'files/res_03_customer/CUSTOMERS_TEXT.txt'
# Create text file with customer:
TxtCustomerFuncs.write_customers_to_text_file(path_customers_text, customer_1)

# Read text file with customer:
customer_1a = TxtCustomerFuncs.read_customers_from_text_file(path_customers_text)
print('\nCustomer from text file:')
customer_1a.print_information()

# Add another customer to text file:
TxtCustomerFuncs.write_customers_to_text_file(path_customers_text, customer_2, 'a')

# Read text file with customers:
customers_1 = TxtCustomerFuncs.read_customers_from_text_file(path_customers_text, False)
print('\n2 customers from text file:')
for customer in customers_1:
    customer.print_information()
print()

# -------------------------------------------
# ACTIONS (I/O) WITH BINARY FILES (CUSTOMERS):
path_customers_binary = 'files/res_03_customer/CUSTOMERS_BINARY.binary'
# Create binary file with customer:
BinCustomerFuncs.write_customers_to_binary_file(path_customers_binary, customer_1)

# Read binary file with customer:
customer_1b = BinCustomerFuncs.read_customers_from_binary_file(path_customers_binary)
print('Customer from binary file:')
customer_1b.print_information()

# Add another customer to binary file:
BinCustomerFuncs.write_customers_to_binary_file(path_customers_binary, customer_2, 'ab')

# Read binary file with customers:
customers_2 = BinCustomerFuncs.read_customers_from_binary_file(path_customers_binary, False)
print('\n2 customers from binary file:')
for customer in customers_2:
    customer.print_information()
print()

# --------------------------------------------------
# ACTIONS (I/O) WITH XML FILES (MINIDOM) (CUSTOMERS):
path_customers_xml_md = 'files/res_03_customer/CUSTOMERS_XML_MD.xml'
# Create xml file with customer:
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md, customer_1)

# Read xml file with customer:
customer_1c = XmlMiniDomCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md)
print('Customer from xml file (minidom):')
customer_1c.print_information()

# Add another customer to xml file:
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md, customer_2, False)

# Read xml file with customers:
customers_3 = XmlMiniDomCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md, False)
print('\n2 customers from xml file (minidom):')
for customer in customers_3:
    customer.print_information()
print()

# ------------------------------------------------------
# ACTIONS (I/O) WITH XML FILES (ELEMENTTREE) (CUSTOMERS):
path_customers_xml_et = 'files/res_03_customer/CUSTOMERS_XML_ET.xml'
# Create xml file with customer:
XmlElementTreeCustomerFuncs.write_customers_to_xml_file(path_customers_xml_et, customer_1)

# Read xml file with customer:
customer_1d = XmlElementTreeCustomerFuncs.read_customers_from_xml_file(path_customers_xml_et)
print('Customer from xml file (elementtree):')
customer_1d.print_information()

# Add another customer to xml file:
XmlElementTreeCustomerFuncs.write_customers_to_xml_file(path_customers_xml_et, customer_2, False)

# Read xml file with customers:
customers_4 = XmlElementTreeCustomerFuncs.read_customers_from_xml_file(path_customers_xml_et, False)
print('\n2 customers from xml file (elementtree):')
for customer in customers_4:
    customer.print_information()
print()

# -------------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (JSON MODULE) (CUSTOMERS):
path_customers_json = 'files/res_03_customer/CUSTOMERS_JSON.json'
# Create json file with customer:
JsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json, customer_1)

# Read json file with customer:
customer_1e = JsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json)
print('Customer from json file:')
customer_1e.print_information()

# Add another customer to json file:
JsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json, customer_2, False)

# Read json file with customers:
customers_5 = JsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json, False)
print('\n2 customers from json file:')
for customer in customers_5:
    customer.print_information()
print()

# ---------------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (ORJSON MODULE) (CUSTOMERS):
path_customers_json_or = 'files/res_03_customer/CUSTOMERS_JSON_OR.json'
# Create json file with customer:
OrjsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_or, customer_1)

# Read json file with customer:
customer_1f = OrjsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json_or)
print('Customer from json file (orjson):')
customer_1f.print_information()

# Add another customer to json file:
OrjsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_or, customer_2, False)

# Read json file with customers:
customers_6 = OrjsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json_or, False)
print('\n2 customers from json file (orjson):')
for customer in customers_6:
    customer.print_information()
print()

# -------------------------------------------------------------
# ACTIONS (I/O) WITH JSON FILES (JSONPICKLE MODULE) (CUSTOMERS):
path_customers_json_p = 'files/res_03_customer/CUSTOMERS_JSON_P.json'
# Create json file with customer:
JsonPickleCustomerFuncs.write_customers_to_json_file(path_customers_json_p, customer_1)

# Read json file with customer:
customer_1g = JsonPickleCustomerFuncs.read_customers_from_json_file(path_customers_json_p)
print('Customer from json file (jsonpickle):')
customer_1g.print_information()

# Add another customer to json file:
JsonPickleCustomerFuncs.write_customers_to_json_file(path_customers_json_p, customer_2, False)

# Read json file with customers:
customers_6 = JsonPickleCustomerFuncs.read_customers_from_json_file(path_customers_json_p, False)
print('\n2 customers from json file (jsonpickle):')
for customer in customers_6:
    customer.print_information()
print()

# ------------------------------------------
# ACTIONS (I/O) WITH XML FILES (SAX) (BOOKS):
path_books_xml_md_and_sax = 'files/res_01_book/BOOKS_XML_MD_AND_SAX.xml'
# Create xml file with book (using minidom):
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_and_sax, book_1)

# Read XML file with book:
book_1h = XmlSaxReadBookFuncs.read_books_from_xml_file(path_books_xml_md_and_sax)
print('Book from xml file (SAX):')
book_1h.print_information()

# Add another book to xml file (using minidom):
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_and_sax, book_2, False)

# Read xml file with books:
books_8 = XmlSaxReadBookFuncs.read_books_from_xml_file(path_books_xml_md_and_sax)
print('\n2 books from xml file (SAX):')
for book in books_8:
    book.print_information()
print()

# -------------------------------------------
# ACTIONS (I/O) WITH XML FILES (SAX) (ORDERS):
path_orders_xml_md_and_sax = 'files/res_02_order/ORDERS_XML_MD_AND_SAX.xml'
# Create xml file with order (using minidom):
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_and_sax, order_1)

# Read XML file with order:
order_1h = XmlSaxReadOrderFuncs.read_orders_from_xml_file(path_orders_xml_md_and_sax)
print('Order from xml file (SAX):')
order_1h.print_information()

# Add another order to xml file (using minidom):
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_and_sax, order_2, False)

# Read xml file with orders:
orders_8 = XmlSaxReadOrderFuncs.read_orders_from_xml_file(path_orders_xml_md_and_sax)
print('\n2 orders from xml file (SAX):')
for order in orders_8:
    order.print_information()
print()

# ----------------------------------------------
# ACTIONS (I/O) WITH XML FILES (SAX) (CUSTOMERS):
path_customers_xml_md_and_sax = 'files/res_03_customer/CUSTOMERS_XML_MD_AND_SAX.xml'
# Create xml file with customer (using minidom):
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_and_sax, customer_1)

# Read XML file with customer:
customer_1h = XmlSaxReadCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md_and_sax)
print('Customer from xml file (SAX):')
customer_1h.print_information()

# Add another customer to xml file (using minidom):
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_and_sax, customer_2, False)

# Read xml file with customers:
customers_8 = XmlSaxReadCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md_and_sax)
print('\n2 customers from xml file (SAX):')
for customer in customers_8:
    customer.print_information()
print()

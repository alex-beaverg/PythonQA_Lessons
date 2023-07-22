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

# Add another books to text file:
TxtBookFuncs.write_books_to_text_file(path_books_text, book_2, 'a')
TxtBookFuncs.write_books_to_text_file(path_books_text, book_3, 'a')

# Read text file with books:
books_1 = TxtBookFuncs.read_books_from_text_file(path_books_text, False)
print('\n3 books from text file:')
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

# Add another books to binary file:
BinBookFuncs.write_books_to_binary_file(path_books_binary, book_2, 'ab')
BinBookFuncs.write_books_to_binary_file(path_books_binary, book_3, 'ab')

# Read binary file with books:
books_2 = BinBookFuncs.read_books_from_binary_file(path_books_binary, False)
print('\n3 books from binary file:')
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

# Add another books to xml file:
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md, book_2, False)
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md, book_3, False)

# Read xml file with books:
books_3 = XmlMiniDomBookFuncs.read_books_from_xml_file(path_books_xml_md, False)
print('\n3 books from xml file (minidom):')
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

# Add another books to xml file:
XmlElementTreeBookFuncs.write_books_to_xml_file(path_books_xml_et, book_2, False)
XmlElementTreeBookFuncs.write_books_to_xml_file(path_books_xml_et, book_3, False)

# Read xml file with books:
books_4 = XmlElementTreeBookFuncs.read_books_from_xml_file(path_books_xml_et, False)
print('\n3 books from xml file (elementtree):')
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

# Add another books to json file:
JsonModuleBookFuncs.write_books_to_json_file(path_books_json, book_2, False)
JsonModuleBookFuncs.write_books_to_json_file(path_books_json, book_3, False)

# Read json file with books:
books_5 = JsonModuleBookFuncs.read_books_from_json_file(path_books_json, False)
print('\n3 books from json file:')
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

# Add another books to json file:
OrjsonModuleBookFuncs.write_books_to_json_file(path_books_json_or, book_2, False)
OrjsonModuleBookFuncs.write_books_to_json_file(path_books_json_or, book_3, False)

# Read json file with books:
books_6 = OrjsonModuleBookFuncs.read_books_from_json_file(path_books_json_or, False)
print('\n3 books from json file (orjson):')
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

# Add another books to json file:
JsonPickleBookFuncs.write_books_to_json_file(path_books_json_p, book_2, False)
JsonPickleBookFuncs.write_books_to_json_file(path_books_json_p, book_3, False)

# Read json file with books:
books_7 = JsonPickleBookFuncs.read_books_from_json_file(path_books_json_p, False)
print('\n3 books from json file (jsonpickle):')
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

order_3 = Order()
order_3.add_book(book_2, 5)
order_3.add_book(book_3)

# --------------------------------------
# ACTIONS (I/O) WITH TEXT FILES (ORDERS):
path_orders_text = 'files/res_02_order/ORDERS_TEXT.txt'
# Create text file with order:
TxtOrderFuncs.write_orders_to_text_file(path_orders_text, order_1)

# Read text file with order:
order_1a = TxtOrderFuncs.read_orders_from_text_file(path_orders_text)
print('\nOrder from text file:')
order_1a.print_information()

# Add another orders to text file:
TxtOrderFuncs.write_orders_to_text_file(path_orders_text, order_2, 'a')
TxtOrderFuncs.write_orders_to_text_file(path_orders_text, order_3, 'a')

# Read text file with orders:
orders_1 = TxtOrderFuncs.read_orders_from_text_file(path_orders_text, False)
print('\n3 orders from text file:')
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

# Add another orders to binary file:
BinOrderFuncs.write_orders_to_binary_file(path_orders_binary, order_2, 'ab')
BinOrderFuncs.write_orders_to_binary_file(path_orders_binary, order_3, 'ab')

# Read binary file with orders:
orders_2 = BinOrderFuncs.read_orders_from_binary_file(path_orders_binary, False)
print('\n3 orders from binary file:')
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

# Add another orders to xml file:
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md, order_2, False)
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md, order_3, False)

# Read xml file with orders:
orders_3 = XmlMiniDomOrderFuncs.read_orders_from_xml_file(path_orders_xml_md, False)
print('\n3 orders from xml file (minidom):')
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

# Add another orders to xml file:
XmlElementTreeOrderFuncs.write_orders_to_xml_file(path_orders_xml_et, order_2, False)
XmlElementTreeOrderFuncs.write_orders_to_xml_file(path_orders_xml_et, order_3, False)

# Read xml file with orders:
orders_4 = XmlElementTreeOrderFuncs.read_orders_from_xml_file(path_orders_xml_et, False)
print('\n3 orders from xml file (elementtree):')
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

# Add another orders to json file:
JsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json, order_2, False)
JsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json, order_3, False)

# Read json file with orders:
orders_5 = JsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json, False)
print('\n3 orders from json file:')
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

# Add another orders to json file:
OrjsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_or, order_2, False)
OrjsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_or, order_3, False)

# Read json file with orders:
orders_6 = OrjsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json_or, False)
print('\n3 orders from json file (orjson):')
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

# Add another orders to json file:
JsonPickleOrderFuncs.write_orders_to_json_file(path_orders_json_p, order_2, False)
JsonPickleOrderFuncs.write_orders_to_json_file(path_orders_json_p, order_3, False)

# Read json file with orders:
orders_7 = JsonPickleOrderFuncs.read_orders_from_json_file(path_orders_json_p, False)
print('\n3 orders from json file (jsonpickle):')
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

# Add another customers to text file:
TxtCustomerFuncs.write_customers_to_text_file(path_customers_text, customer_2, 'a')
TxtCustomerFuncs.write_customers_to_text_file(path_customers_text, customer_3, 'a')

# Read text file with customers:
customers_1 = TxtCustomerFuncs.read_customers_from_text_file(path_customers_text, False)
print('\n3 customers from text file:')
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

# Add another customers to binary file:
BinCustomerFuncs.write_customers_to_binary_file(path_customers_binary, customer_2, 'ab')
BinCustomerFuncs.write_customers_to_binary_file(path_customers_binary, customer_3, 'ab')

# Read binary file with customers:
customers_2 = BinCustomerFuncs.read_customers_from_binary_file(path_customers_binary, False)
print('\n3 customers from binary file:')
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

# Add another customers to xml file:
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md, customer_2, False)
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md, customer_3, False)

# Read xml file with customers:
customers_3 = XmlMiniDomCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md, False)
print('\n3 customers from xml file (minidom):')
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

# Add another customers to xml file:
XmlElementTreeCustomerFuncs.write_customers_to_xml_file(path_customers_xml_et, customer_2, False)
XmlElementTreeCustomerFuncs.write_customers_to_xml_file(path_customers_xml_et, customer_3, False)

# Read xml file with customers:
customers_4 = XmlElementTreeCustomerFuncs.read_customers_from_xml_file(path_customers_xml_et, False)
print('\n3 customers from xml file (elementtree):')
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

# Add another customers to json file:
JsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json, customer_2, False)
JsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json, customer_3, False)

# Read json file with customers:
customers_5 = JsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json, False)
print('\n3 customers from json file:')
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

# Add another customers to json file:
OrjsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_or, customer_2, False)
OrjsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_or, customer_3, False)

# Read json file with customers:
customers_6 = OrjsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json_or, False)
print('\n3 customers from json file (orjson):')
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

# Add another customers to json file:
JsonPickleCustomerFuncs.write_customers_to_json_file(path_customers_json_p, customer_2, False)
JsonPickleCustomerFuncs.write_customers_to_json_file(path_customers_json_p, customer_3, False)

# Read json file with customers:
customers_6 = JsonPickleCustomerFuncs.read_customers_from_json_file(path_customers_json_p, False)
print('\n3 customers from json file (jsonpickle):')
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

# Add another books to xml file (using minidom):
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_and_sax, book_2, False)
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_and_sax, book_3, False)

# Read xml file with books:
books_8 = XmlSaxReadBookFuncs.read_books_from_xml_file(path_books_xml_md_and_sax)
print('\n3 books from xml file (SAX):')
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

# Add another orders to xml file (using minidom):
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_and_sax, order_2, False)
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_and_sax, order_3, False)

# Read xml file with orders:
orders_8 = XmlSaxReadOrderFuncs.read_orders_from_xml_file(path_orders_xml_md_and_sax)
print('\n3 orders from xml file (SAX):')
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

# Add another customers to xml file (using minidom):
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_and_sax, customer_2, False)
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_and_sax, customer_3, False)

# Read xml file with customers:
customers_8 = XmlSaxReadCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md_and_sax)
print('\n3 customers from xml file (SAX):')
for customer in customers_8:
    customer.print_information()
print()

# ------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH TEXT FILES (BOOKS):
# Create books:
book_4 = Book('Chip and Dale. Part 2', 'Dont Know', 30, 15)
book_5 = Book('Three mini pigs. Part 2', 'Dont Know 2nd', 15, 18)
book_6 = Book('Bad guys III', 'Michael Bay', 51, 35)
path_books_text_without_places = 'files/res_01_book/BOOKS_TEXT_WITHOUT_PLACES.txt'
# Create text file with book without places:
TxtBookFuncs.write_books_to_text_file(path_books_text_without_places, book_4)

# Read text file with book without places:
book_2a = TxtBookFuncs.read_books_from_text_file(path_books_text_without_places)
print('Book without places from text file:')
book_2a.print_information()

# Add another books without places to text file:
TxtBookFuncs.write_books_to_text_file(path_books_text_without_places, book_5, 'a')
TxtBookFuncs.write_books_to_text_file(path_books_text_without_places, book_6, 'a')

# Read text file with books without places:
books_11 = TxtBookFuncs.read_books_from_text_file(path_books_text_without_places, False)
print('\n3 books without places from text file:')
for book in books_11:
    book.print_information()
print()

# --------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH BINARY FILES (BOOKS):
path_books_binary_without_places = 'files/res_01_book/BOOKS_BINARY_WITHOUT_PLACES.binary'
# Create binary file with book without places:
BinBookFuncs.write_books_to_binary_file(path_books_binary_without_places, book_4)

# Read binary file with book without places:
book_2b = BinBookFuncs.read_books_from_binary_file(path_books_binary_without_places)
print('Book without places from binary file:')
book_2b.print_information()

# Add another books without places to binary file:
BinBookFuncs.write_books_to_binary_file(path_books_binary_without_places, book_5, 'ab')
BinBookFuncs.write_books_to_binary_file(path_books_binary_without_places, book_6, 'ab')

# Read binary file with books without places:
books_12 = BinBookFuncs.read_books_from_binary_file(path_books_binary_without_places, False)
print('\n3 books without places from binary file:')
for book in books_12:
    book.print_information()
print()

# ---------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (MINIDOM) (BOOKS):
path_books_xml_md_without_places = 'files/res_01_book/BOOKS_XML_MD_WITHOUT_PLACES.xml'
# Create xml file with book without places:
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_without_places, book_4)

# Read xml file with book without places:
book_2c = XmlMiniDomBookFuncs.read_books_from_xml_file(path_books_xml_md_without_places)
print('Book without places from xml file (minidom):')
book_2c.print_information()

# Add another books without places to xml file:
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_without_places, book_5, False)
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_without_places, book_6, False)

# Read xml file with books without places:
books_13 = XmlMiniDomBookFuncs.read_books_from_xml_file(path_books_xml_md_without_places, False)
print('\n3 books without places from xml file (minidom):')
for book in books_13:
    book.print_information()
print()

# -------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (ELEMENTTREE) (BOOKS):
path_books_xml_et_without_places = 'files/res_01_book/BOOKS_XML_ET_WITHOUT_PLACES.xml'
# Create xml file with book without places:
XmlElementTreeBookFuncs.write_books_to_xml_file(path_books_xml_et_without_places, book_4)

# Read xml file with book without places:
book_2d = XmlElementTreeBookFuncs.read_books_from_xml_file(path_books_xml_et_without_places)
print('Book without places from xml file (elementtree):')
book_2d.print_information()

# Add another books without places to xml file:
XmlElementTreeBookFuncs.write_books_to_xml_file(path_books_xml_et_without_places, book_5, False)
XmlElementTreeBookFuncs.write_books_to_xml_file(path_books_xml_et_without_places, book_6, False)

# Read xml file with books without places:
books_14 = XmlElementTreeBookFuncs.read_books_from_xml_file(path_books_xml_et_without_places, False)
print('\n3 books without places from xml file (elementtree):')
for book in books_14:
    book.print_information()
print()

# --------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (JSON MODULE) (BOOKS):
path_books_json_without_places = 'files/res_01_book/BOOKS_JSON_WITHOUT_PLACES.json'
# Create json file with book without places:
JsonModuleBookFuncs.write_books_to_json_file(path_books_json_without_places, book_4)

# Read json file with book without places:
book_2e = JsonModuleBookFuncs.read_books_from_json_file(path_books_json_without_places)
print('Book without places from json file:')
book_2e.print_information()

# Add another books without places to json file:
JsonModuleBookFuncs.write_books_to_json_file(path_books_json_without_places, book_5, False)
JsonModuleBookFuncs.write_books_to_json_file(path_books_json_without_places, book_6, False)

# Read json file with books without places:
books_15 = JsonModuleBookFuncs.read_books_from_json_file(path_books_json_without_places, False)
print('\n3 books without places from json file:')
for book in books_15:
    book.print_information()
print()

# ----------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (ORJSON MODULE) (BOOKS):
path_books_json_or_without_places = 'files/res_01_book/BOOKS_JSON_OR_WITHOUT_PLACES.json'
# Create json file with book without places:
OrjsonModuleBookFuncs.write_books_to_json_file(path_books_json_or_without_places, book_4)

# Read json file with book without places:
book_2f = OrjsonModuleBookFuncs.read_books_from_json_file(path_books_json_or_without_places)
print('Book without places from json file (orjson):')
book_2f.print_information()

# Add another books without places to json file:
OrjsonModuleBookFuncs.write_books_to_json_file(path_books_json_or_without_places, book_5, False)
OrjsonModuleBookFuncs.write_books_to_json_file(path_books_json_or_without_places, book_6, False)

# Read json file with books without places:
books_16 = OrjsonModuleBookFuncs.read_books_from_json_file(path_books_json_or_without_places, False)
print('\n3 books without places from json file (orjson):')
for book in books_16:
    book.print_information()
print()

# --------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (JSON PICKLE) (BOOKS):
path_books_json_p_without_places = 'files/res_01_book/BOOKS_JSON_P_WITHOUT_PLACES.json'
# Create json file with book without places:
JsonPickleBookFuncs.write_books_to_json_file(path_books_json_p_without_places, book_4)

# Read json file with book without places:
book_2g = JsonPickleBookFuncs.read_books_from_json_file(path_books_json_p_without_places)
print('Book without places from json file (jsonpickle):')
book_2g.print_information()

# Add another books without places to json file:
JsonPickleBookFuncs.write_books_to_json_file(path_books_json_p_without_places, book_5, False)
JsonPickleBookFuncs.write_books_to_json_file(path_books_json_p_without_places, book_6, False)

# Read json file with books without places:
books_17 = JsonPickleBookFuncs.read_books_from_json_file(path_books_json_p_without_places, False)
print('\n3 books without places from json file (jsonpickle):')
for book in books_17:
    book.print_information()
print()

# -----------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (SAX) (BOOKS):
path_books_xml_md_and_sax_without_places = 'files/res_01_book/BOOKS_XML_MD_AND_SAX_WP.xml'
# Create xml file with book without places (using minidom):
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_and_sax_without_places, book_4)

# Read XML file with book without places:
book_2h = XmlSaxReadBookFuncs.read_books_from_xml_file(path_books_xml_md_and_sax_without_places)
print('Book without places from xml file (SAX):')
book_2h.print_information()

# Add another books without places to xml file (using minidom):
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_and_sax_without_places, book_5, False)
XmlMiniDomBookFuncs.write_books_to_xml_file(path_books_xml_md_and_sax_without_places, book_6, False)

# Read xml file with books without places:
books_18 = XmlSaxReadBookFuncs.read_books_from_xml_file(path_books_xml_md_and_sax_without_places)
print('\n3 books without places from xml file (SAX):')
for book in books_18:
    book.print_information()
print()

# -------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH TEXT FILES (ORDERS):
# Create orders:
order_4 = Order()
order_5 = Order()
order_6 = Order()
path_orders_text_without_adds = 'files/res_02_order/ORDERS_TEXT_WITHOUT_ADDS.txt'
# Create text file with order without adds:
TxtOrderFuncs.write_orders_to_text_file(path_orders_text_without_adds, order_4)

# Read text file with order without adds:
order_2a = TxtOrderFuncs.read_orders_from_text_file(path_orders_text_without_adds)
print('Order without adds from text file:')
order_2a.print_information()

# Add another orders without adds to text file:
TxtOrderFuncs.write_orders_to_text_file(path_orders_text_without_adds, order_5, 'a')
TxtOrderFuncs.write_orders_to_text_file(path_orders_text_without_adds, order_6, 'a')

# Read text file with orders without adds:
orders_11 = TxtOrderFuncs.read_orders_from_text_file(path_orders_text_without_adds, False)
print('\n3 orders without adds from text file:')
for order in orders_11:
    order.print_information()
print()

# ---------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH BINARY FILES (ORDERS):
path_orders_binary_without_adds = 'files/res_02_order/ORDERS_BINARY_WITHOUT_ADDS.binary'
# Create binary file with order without adds:
BinOrderFuncs.write_orders_to_binary_file(path_orders_binary_without_adds, order_4)

# Read binary file with order without adds:
order_2b = BinOrderFuncs.read_orders_from_binary_file(path_orders_binary_without_adds)
print('Order without adds from binary file:')
order_2b.print_information()

# Add another orders without adds to binary file:
BinOrderFuncs.write_orders_to_binary_file(path_orders_binary_without_adds, order_5, 'ab')
BinOrderFuncs.write_orders_to_binary_file(path_orders_binary_without_adds, order_6, 'ab')

# Read binary file with orders without adds:
orders_12 = BinOrderFuncs.read_orders_from_binary_file(path_orders_binary_without_adds, False)
print('\n3 orders without adds from binary file:')
for order in orders_12:
    order.print_information()
print()

# ----------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (MINIDOM) (ORDERS):
path_orders_xml_md_without_adds = 'files/res_02_order/ORDERS_XML_MD_WITHOUT_ADDS.xml'
# Create xml file with order without adds:
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_without_adds, order_4)

# Read xml file with order without adds:
order_2c = XmlMiniDomOrderFuncs.read_orders_from_xml_file(path_orders_xml_md_without_adds)
print('Order without adds from xml file (minidom):')
order_2c.print_information()

# Add another orders without adds to xml file:
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_without_adds, order_5, False)
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_without_adds, order_6, False)

# Read xml file with orders without adds:
orders_13 = XmlMiniDomOrderFuncs.read_orders_from_xml_file(path_orders_xml_md_without_adds, False)
print('\n3 orders without adds from xml file (minidom):')
for order in orders_13:
    order.print_information()
print()

# --------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (ELEMENTTREE) (ORDERS):
path_orders_xml_et_without_adds = 'files/res_02_order/ORDERS_XML_ET_WITHOUT_ADDS.xml'
# Create xml file with order without adds:
XmlElementTreeOrderFuncs.write_orders_to_xml_file(path_orders_xml_et_without_adds, order_4)

# Read xml file with order without adds:
order_2d = XmlElementTreeOrderFuncs.read_orders_from_xml_file(path_orders_xml_et_without_adds)
print('Order without adds from xml file (elementtree):')
order_2d.print_information()

# Add another orders without adds to xml file:
XmlElementTreeOrderFuncs.write_orders_to_xml_file(path_orders_xml_et_without_adds, order_5, False)
XmlElementTreeOrderFuncs.write_orders_to_xml_file(path_orders_xml_et_without_adds, order_6, False)

# Read xml file with orders without adds:
orders_14 = XmlElementTreeOrderFuncs.read_orders_from_xml_file(path_orders_xml_et_without_adds, False)
print('\n3 orders without adds from xml file (elementtree):')
for order in orders_14:
    order.print_information()
print()

# ---------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (JSON MODULE) (ORDERS):
path_orders_json_without_adds = 'files/res_02_order/ORDERS_JSON_WITHOUT_ADDS.json'
# Create json file with order without adds:
JsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_without_adds, order_4)

# Read json file with order without adds:
order_2e = JsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json_without_adds)
print('Order without adds from json file:')
order_2e.print_information()

# Add another orders without adds to json file:
JsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_without_adds, order_5, False)
JsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_without_adds, order_6, False)

# Read json file with orders without adds:
orders_15 = JsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json_without_adds, False)
print('\n3 orders without adds from json file:')
for order in orders_15:
    order.print_information()
print()

# -----------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (ORJSON MODULE) (ORDERS):
path_orders_json_or_without_adds = 'files/res_02_order/ORDERS_JSON_OR_WITHOUT_ADDS.json'
# Create json file with order without adds:
OrjsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_or_without_adds, order_4)

# Read json file with order without adds:
order_2f = OrjsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json_or_without_adds)
print('Order without adds from json file (orjson):')
order_2f.print_information()

# Add another orders without adds to json file:
OrjsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_or_without_adds, order_5, False)
OrjsonModuleOrderFuncs.write_orders_to_json_file(path_orders_json_or_without_adds, order_6, False)

# Read json file with orders without adds:
orders_16 = OrjsonModuleOrderFuncs.read_orders_from_json_file(path_orders_json_or_without_adds, False)
print('\n3 orders without adds from json file (orjson):')
for order in orders_16:
    order.print_information()
print()

# ---------------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (JSONPICKLE MODULE) (ORDERS):
path_orders_json_p_without_adds = 'files/res_02_order/ORDERS_JSON_P_WITHOUT_ADDS.json'
# Create json file with order without adds:
JsonPickleOrderFuncs.write_orders_to_json_file(path_orders_json_p_without_adds, order_4)

# Read json file with order without adds:
order_2g = JsonPickleOrderFuncs.read_orders_from_json_file(path_orders_json_p_without_adds)
print('Order without adds from json file (jsonpickle):')
order_2g.print_information()

# Add another orders without adds to json file:
JsonPickleOrderFuncs.write_orders_to_json_file(path_orders_json_p_without_adds, order_5, False)
JsonPickleOrderFuncs.write_orders_to_json_file(path_orders_json_p_without_adds, order_6, False)

# Read json file with orders without adds:
orders_17 = JsonPickleOrderFuncs.read_orders_from_json_file(path_orders_json_p_without_adds, False)
print('\n3 orders without adds from json file (jsonpickle):')
for order in orders_17:
    order.print_information()
print()

# ------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (SAX) (ORDERS):
path_orders_xml_md_and_sax_woa = 'files/res_02_order/ORDERS_XML_MD_AND_SAX_WOA.xml'
# Create xml file with order without adds (using minidom):
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_and_sax_woa, order_4)

# Read XML file with order without adds:
order_2h = XmlSaxReadOrderFuncs.read_orders_from_xml_file(path_orders_xml_md_and_sax_woa)
print('Order without adds from xml file (SAX):')
order_2h.print_information()

# Add another orders without adds to xml file (using minidom):
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_and_sax_woa, order_5, False)
XmlMiniDomOrderFuncs.write_orders_to_xml_file(path_orders_xml_md_and_sax_woa, order_6, False)

# Read xml file with orders without adds:
orders_18 = XmlSaxReadOrderFuncs.read_orders_from_xml_file(path_orders_xml_md_and_sax_woa)
print('\n3 orders without adds from xml file (SAX):')
for order in orders_18:
    order.print_information()
print()

# ----------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH TEXT FILES (CUSTOMERS):
# Create customers:
customer_4 = Customer('Mister', 'X', 'M', 40, {'Primary': 'Oslo', 'Secondary': 'Berlin'}, '+322-10-356-58-95',
                      'mister.x@eumail.com')
customer_5 = Customer('Harold', 'Eugen', 'M', 31, {'Primary': 'Paris', 'Secondary': 'Madrid'}, '+311-14-651-89-75',
                      'h.eugen@eumail.com')
customer_6 = Customer('Mary', 'Simpson', 'F', 21, {'Primary': 'London', 'Secondary': 'Vienna'}, '+315-17-622-33-16',
                      'm.simpson@eumail.com')
path_customers_text_without_orders = 'files/res_03_customer/CUSTOMERS_TEXT_WITHOUT_ORDERS.txt'
# Create text file with customer without orders:
TxtCustomerFuncs.write_customers_to_text_file(path_customers_text_without_orders, customer_4)

# Read text file with customer without orders:
customer_2a = TxtCustomerFuncs.read_customers_from_text_file(path_customers_text_without_orders)
print('\nCustomer without orders from text file:')
customer_2a.print_information()

# Add another customers without orders to text file:
TxtCustomerFuncs.write_customers_to_text_file(path_customers_text_without_orders, customer_5, 'a')
TxtCustomerFuncs.write_customers_to_text_file(path_customers_text_without_orders, customer_6, 'a')

# Read text file with customers without orders:
customers_11 = TxtCustomerFuncs.read_customers_from_text_file(path_customers_text_without_orders, False)
print('\n3 customers without orders from text file:')
for customer in customers_11:
    customer.print_information()
print()

# ------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH BINARY FILES (CUSTOMERS):
path_customers_binary_without_orders = 'files/res_03_customer/CUSTOMERS_BINARY_WITHOUT_ORDERS.binary'
# Create binary file with customer without orders:
BinCustomerFuncs.write_customers_to_binary_file(path_customers_binary_without_orders, customer_4)

# Read binary file with customer without orders:
customer_2b = BinCustomerFuncs.read_customers_from_binary_file(path_customers_binary_without_orders)
print('Customer without orders from binary file:')
customer_2b.print_information()

# Add another customers without orders to binary file:
BinCustomerFuncs.write_customers_to_binary_file(path_customers_binary_without_orders, customer_5, 'ab')
BinCustomerFuncs.write_customers_to_binary_file(path_customers_binary_without_orders, customer_6, 'ab')

# Read binary file with customers without orders:
customers_12 = BinCustomerFuncs.read_customers_from_binary_file(path_customers_binary_without_orders, False)
print('\n3 customers without orders from binary file:')
for customer in customers_12:
    customer.print_information()
print()

# -------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (MINIDOM) (CUSTOMERS):
path_customers_xml_md_without_orders = 'files/res_03_customer/CUSTOMERS_XML_MD_WITHOUT_ORDERS.xml'
# Create xml file with customer without orders:
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_without_orders, customer_4)

# Read xml file with customer without orders:
customer_2c = XmlMiniDomCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md_without_orders)
print('Customer without orders from xml file (minidom):')
customer_2c.print_information()

# Add another customers without orders to xml file:
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_without_orders, customer_5, False)
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_without_orders, customer_6, False)

# Read xml file with customers without orders:
customers_13 = XmlMiniDomCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md_without_orders, False)
print('\n3 customers without orders from xml file (minidom):')
for customer in customers_13:
    customer.print_information()
print()

# -----------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (ELEMENTTREE) (CUSTOMERS):
path_customers_xml_et_without_orders = 'files/res_03_customer/CUSTOMERS_XML_ET_WITHOUT_ORDERS.xml'
# Create xml file with customer without orders:
XmlElementTreeCustomerFuncs.write_customers_to_xml_file(path_customers_xml_et_without_orders, customer_4)

# Read xml file with customer without orders:
customer_2d = XmlElementTreeCustomerFuncs.read_customers_from_xml_file(path_customers_xml_et_without_orders)
print('Customer without orders from xml file (elementtree):')
customer_2d.print_information()

# Add another customers without orders to xml file:
XmlElementTreeCustomerFuncs.write_customers_to_xml_file(path_customers_xml_et_without_orders, customer_5, False)
XmlElementTreeCustomerFuncs.write_customers_to_xml_file(path_customers_xml_et_without_orders, customer_6, False)

# Read xml file with customers without orders:
customers_14 = XmlElementTreeCustomerFuncs.read_customers_from_xml_file(path_customers_xml_et_without_orders, False)
print('\n3 customers without orders from xml file (elementtree):')
for customer in customers_14:
    customer.print_information()
print()

# ------------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (JSON MODULE) (CUSTOMERS):
path_customers_json_without_orders = 'files/res_03_customer/CUSTOMERS_JSON_WITHOUT_ORDERS.json'
# Create json file with customer without orders:
JsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_without_orders, customer_4)

# Read json file with customer without orders:
customer_2e = JsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json_without_orders)
print('Customer without orders from json file:')
customer_2e.print_information()

# Add another customers without orders to json file:
JsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_without_orders, customer_5, False)
JsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_without_orders, customer_6, False)

# Read json file with customers without orders:
customers_15 = JsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json_without_orders, False)
print('\n3 customers without orders from json file:')
for customer in customers_15:
    customer.print_information()
print()

# --------------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (ORJSON MODULE) (CUSTOMERS):
path_customers_json_or_without_orders = 'files/res_03_customer/CUSTOMERS_JSON_OR_WITHOUT_ORDERS.json'
# Create json file with customer without orders:
OrjsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_or_without_orders, customer_4)

# Read json file with customer without orders:
customer_2f = OrjsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json_or_without_orders)
print('Customer without orders from json file (orjson):')
customer_2f.print_information()

# Add another customers without orders to json file:
OrjsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_or_without_orders, customer_5, False)
OrjsonModuleCustomerFuncs.write_customers_to_json_file(path_customers_json_or_without_orders, customer_6, False)

# Read json file with customers without orders:
customers_16 = OrjsonModuleCustomerFuncs.read_customers_from_json_file(path_customers_json_or_without_orders, False)
print('\n3 customers without orders from json file (orjson):')
for customer in customers_16:
    customer.print_information()
print()

# ------------------------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH JSON FILES (JSONPICKLE MODULE) (CUSTOMERS):
path_customers_json_p_without_orders = 'files/res_03_customer/CUSTOMERS_JSON_P_WITHOUT_ORDERS.json'
# Create json file with customer without orders:
JsonPickleCustomerFuncs.write_customers_to_json_file(path_customers_json_p_without_orders, customer_4)

# Read json file with customer without orders:
customer_2g = JsonPickleCustomerFuncs.read_customers_from_json_file(path_customers_json_p_without_orders)
print('Customer without orders from json file (jsonpickle):')
customer_2g.print_information()

# Add another customers without orders to json file:
JsonPickleCustomerFuncs.write_customers_to_json_file(path_customers_json_p_without_orders, customer_5, False)
JsonPickleCustomerFuncs.write_customers_to_json_file(path_customers_json_p_without_orders, customer_6, False)

# Read json file with customers without orders:
customers_16 = JsonPickleCustomerFuncs.read_customers_from_json_file(path_customers_json_p_without_orders, False)
print('\n3 customers without orders from json file (jsonpickle):')
for customer in customers_16:
    customer.print_information()
print()

# ---------------------------------------------------------
# ADDITIONAL ACTIONS (I/O) WITH XML FILES (SAX) (CUSTOMERS):
path_customers_xml_md_and_sax_woo = 'files/res_03_customer/CUSTOMERS_XML_MD_AND_SAX_WOO.xml'
# Create xml file with customer without orders (using minidom):
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_and_sax_woo, customer_4)

# Read XML file with customer without orders:
customer_2h = XmlSaxReadCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md_and_sax_woo)
print('Customer without orders from xml file (SAX):')
customer_2h.print_information()

# Add another customers without orders to xml file (using minidom):
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_and_sax_woo, customer_5, False)
XmlMiniDomCustomerFuncs.write_customers_to_xml_file(path_customers_xml_md_and_sax_woo, customer_6, False)

# Read xml file with customers without orders:
customers_18 = XmlSaxReadCustomerFuncs.read_customers_from_xml_file(path_customers_xml_md_and_sax_woo)
print('\n3 customers without orders from xml file (SAX):')
for customer in customers_18:
    customer.print_information()
print()

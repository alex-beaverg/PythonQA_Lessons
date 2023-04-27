# Homework 04 (2023.04.13)

from PythonQA_HW_03_alexey_bobrikov import Book


class BookStore:
    """Docstring: Class BookStore"""
    __address = 'Minsk'

    def __init__(self) -> None:
        """Docstring: Constructor for class BookStore"""
        print('LOG_INFO: Create bookstore with empty dictionaries of books and customers')
        self.__books = dict()
        self.__customers = dict()

    @staticmethod
    def get_address() -> str:
        """Docstring: Method to get address"""
        print('LOG_INFO: Get address')
        return BookStore.__address

    def add_book(self, book) -> None:
        """Docstring: Method to add book to BookStore"""
        print('LOG_INFO: Add book to BookStore')
        self.__books[book.get_book()["ID"]] = book.get_book()

    def add_customer(self, customer) -> None:
        """Docstring: Method to add customer to BookStore"""
        print('LOG_INFO: Add customer to BookStore')
        self.__customers[f'{customer.get_customer()["Name"]} {customer.get_customer()["Surname"]}'] = \
            customer.get_customer()

    def print_summary_of_all_bookstore(self) -> None:
        """Docstring: Function for print summary of all books in BookStore"""
        print('LOG_INFO: Print summary of all books in BookStore')
        print('List of books in BookStore:')
        for book_info in self.__books.values():
            print(f'\tTitle: {book_info["Title"]:25s}Author: {book_info["Author"]:20s}'
                  f'ID: {book_info["ID"]:<15}Amount: {book_info["Amount"]:<5}Price: {book_info["Price"]} BYN', end='\n')
        print()

    def print_summary_of_all_customers(self) -> None:
        """Docstring: Function for print summary of all customers in BookStore"""
        print('LOG_INFO: Print summary of all customers in BookStore')
        print('Orders of customers in BookStore:')
        for cust_info in self.__customers.values():
            print(f'\t{cust_info["Name"] + " " + cust_info["Surname"]:20s}: {cust_info["Orders"]}', end='\n')
        print()


class NewBook(Book):
    """Docstring: Class NewBook extends class Book from module 'PythonQA_HW_03_alexey_bobrikov'"""

    def __init__(self, amount: int, price: int, *args: (str, int, bool)) -> None:
        """Docstring: Constructor for class NewBook"""
        super().__init__(*args)
        print('LOG_INFO: Add extra parameters to creating book')
        super().get_book()['Amount'] = amount
        super().get_book()['Price'] = price


class Customer:
    """Class Customer"""

    def __init__(self, *args: (str, dict)) -> None:
        """Constructor for class Customer"""
        print('LOG_INFO: Create customer with parameters')
        self.__new_customer = {
            'ID': self.__hash__(),
            'Name': args[0],
            'Surname': args[1],
            'Login': args[2],
            'Password': args[3],
            'Address': args[4],
            'Payment method': args[5],
            'Orders': dict()
        }

    def get_customer(self) -> dict:
        """Docstring: Method to get customer"""
        print('LOG_INFO: Get customer')
        return self.__new_customer


class Order:
    """Docstring: Class Order"""

    def __init__(self, customer: Customer) -> None:
        """Docstring: Constructor for class Order"""
        print(f'LOG_INFO: Create order for customer {customer} without parameters')
        self.__id = self.__hash__()
        self.__customer = customer
        self.__books = []
        self.__total = 0
        self.__total_with_sale = 0

    def get_order_id(self) -> int:
        """Docstring: Method to get order ID"""
        print('LOG_INFO: Get order ID')
        return self.__id

    def get_order_customer(self) -> Customer:
        """Docstring: Method to get order customer"""
        print('LOG_INFO: Get order customer')
        return self.__customer

    def get_order_total_with_sale(self) -> (int, float):
        """Docstring: Method to get order total with sale"""
        print('LOG_INFO: Get order total with sale')
        return self.__total_with_sale

    def add_book_in_order(self, book: NewBook) -> None:
        """Docstring: Method to add book in order"""
        print('LOG_INFO: Add book in order')
        count = 0
        sale_coefficient = 0.5
        if book.get_book()['Amount'] > 0:
            for item in self.__books:
                if item == book:
                    count += 1
            if count > 0:
                self.__total_with_sale += book.get_book()["Price"] * sale_coefficient
            else:
                self.__total_with_sale += book.get_book()["Price"]
            self.__total += book.get_book()["Price"]
            self.__books.append(book)
            book.get_book()['Amount'] -= 1

    def print_info_order(self) -> None:
        """Docstring: Print information about order"""
        print('LOG_INFO: Print information about order')
        print(f'ORDER №_{self.__hash__()}:')
        print('-' * 28)
        print(f'Customer: {self.__customer.get_customer()["Name"]} {self.__customer.get_customer()["Surname"]}')
        print('Books in order:')
        for book in self.__books:
            print(f'\t{book.get_book()["Title"]}, Price: {book.get_book()["Price"]} BYN')
        print(f'Total price: {self.__total} BYN')
        print(f'Total price with sale: {self.__total_with_sale} BYN')
        print(f'Sale: {self.__total - self.__total_with_sale}')


class Package:
    """Docstring: Class Package"""
    def __init__(self, order: Order) -> None:
        """Constructor for class Package"""
        print('LOG_INFO: Create new package')
        self.__order = order
        stamps_quantity = Stamp(BookStore.get_address(), order.get_order_customer().get_customer()['Address'])\
            .get_quantity_stamps()
        stamp_price = 3.5
        self.__package = {
            'Order': self.__order,
            'Stamps quantity': stamps_quantity,
            'Package price': order.get_order_total_with_sale() + stamp_price * stamps_quantity
        }
        order.get_order_customer().get_customer()['Orders'][f'Order №_{order.get_order_id()}'] = \
            str(order.get_order_total_with_sale()) + ' BYN'

    def get_package(self):
        """Docstring: Method to get package"""
        print('LOG_INFO: Get package')
        return self.__package

    def print_package_info(self) -> None:
        """Docstring: Method to print information about package"""
        print('LOG_INFO: Print information about package')
        print('Package with')
        self.__order.print_info_order()
        print(f'Package price: {self.__package["Package price"]}')


class Stamp:
    """Docstring: Class Stamp"""
    __stamps_quantity = 0

    def __init__(self, adr_from: str, adr_to: str) -> None:
        """Docstring: Constructor for class Stamp"""
        print('LOG_INFO: Create new stamp')
        self.__adr_from = adr_from
        self.__adr_to = adr_to

    def get_quantity_stamps(self) -> int:
        """Docstring: Method to return quantity stamps"""
        print('LOG_INFO: Get quantity stamps')
        if self.__adr_from == self.__adr_to:
            self.__stamps_quantity = 1
        else:
            self.__stamps_quantity = 2
        return self.__stamps_quantity


class CodeTable:
    """Docstring: Class CodeTable"""
    __MAIL_CODES = {
        "Minsk": 123000,
        "Grodno": 225000,
        "Brest": 321000,
        "Gomel": 555000,
        "Vitebsk": 100200,
        "Mogilev": 666000
    }

    @staticmethod
    def get_mail_codes() -> dict:
        """Docstring: Method to get mail codes"""
        print('LOG_INFO: Get mail codes')
        return CodeTable.__MAIL_CODES


class Envelop:
    """Docstring: Class Envelop"""

    def __init__(self, package: Package) -> None:
        """Docstring: Constructor for class Envelop"""
        print('LOG_INFO: Create new envelop')
        self.__adr_from = BookStore.get_address()
        self.__adr_to = package.get_package()['Order'].get_order_customer().get_customer()['Address']
        self.__mail_code = self.generate_code(self.__adr_to)
        self.__mail_stamp = self.generate_stamp()
        self.__package = package
        self.__status = "Not sent"

    @staticmethod
    def generate_code(adr_to) -> int:
        """Docstring: Method to generate mail code"""
        print('LOG_INFO: Generate mail code')
        return CodeTable.get_mail_codes().get(adr_to)

    def generate_stamp(self) -> int:
        """Docstring: Method to generate of quantity mail stamps"""
        print('LOG_INFO: Generate of quantity mail stamps')
        return Stamp(self.__adr_from, self.__adr_to).get_quantity_stamps()

    def print_info(self) -> None:
        """Docstring: Method to print information about letter"""
        print('LOG_INFO: Print information about letter')
        print("Information about letter:")
        print(f'Address FROM: {self.__adr_from}')
        print(f'Address TO: {self.__adr_to}')
        print(f'Mail code: {self.__mail_code}')
        print(f'Quantity of mail stamps: {self.__mail_stamp}')
        self.__package.print_package_info()
        print(f'Status: {self.__status}')
        print()

    def send_mail(self):
        """Docstring: Method to send mail"""
        print('LOG_INFO: Send mail')
        self.__status = "Sent"


# Main program entry point
if __name__ == '__main__':
    def print_everything() -> None:
        """Docstring: Method to print all information from all methods"""
        print('\nHomework 04 (2023.04.13)')
        print('-' * 24)
        print()
        print('LOG_INFO: Launch method "print_everything"')
        my_bookstore = BookStore()
        first_book = NewBook(20, 12, 'Chook and Gek', 'Arcadii Gaidar', 150, 10, 'ru', 'Belarus', True,
                             ('Chook and Gek were brothers.',
                              'They received a telegram but quarreled.',
                              'And the story began...'))
        my_bookstore.add_book(first_book)
        primer_book = NewBook(15, 5, 'Primer Book', 'Group of authors', 100, 3, 'en', 'US', True,
                              ('A - Apple.',
                               'B - Banana.',
                               'C - Cucumber.'))
        my_bookstore.add_book(primer_book)
        blue_book = NewBook(100, 25, 'Blue Book', 'Blue Author', 666, 18, 'by', 'Belarus', True,
                            ('My name is Alexey and I am an alcoholic.',
                             'I really like to drink beer.',
                             'And I will be drink it every week!'))
        my_bookstore.add_book(blue_book)
        b_a_book = NewBook(5, 50, 'Murder in the Front Row', 'Brian Lew', 272, 18, 'US', 'United States', True,
                           ('This is a story about roots of thrash metal.',
                            'It began at the Bay Area in San Francisco.',
                            'It was in the early eighties...'))
        my_bookstore.add_book(b_a_book)
        about_mouse = NewBook(1, 100, 'Pook the mouse', 'Steeve Edgard', 94, 6, 'UK', 'United Kingdom', True,
                              ('There lived a little mouse Pook.',
                               'She liked to fart very loudly.',
                               'So no one was friends with her...'))
        my_bookstore.add_book(about_mouse)

        my_bookstore.print_summary_of_all_bookstore()

        first_customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        my_bookstore.add_customer(first_customer)
        second_customer = Customer('Ivan', 'Ivanov', 'ivan_i', '123456', 'Grodno', 'Card')
        my_bookstore.add_customer(second_customer)
        my_bookstore.print_summary_of_all_customers()

        first_book.print_book_description()
        first_book.print_first_three_pages_preview()
        primer_book.print_book_description()
        primer_book.print_first_three_pages_preview()
        blue_book.print_book_description()
        blue_book.print_first_three_pages_preview()
        b_a_book.print_book_description()
        b_a_book.print_first_three_pages_preview()
        about_mouse.print_book_description()
        about_mouse.print_first_three_pages_preview()

        first_order = Order(first_customer)
        first_order.add_book_in_order(primer_book)
        first_order.add_book_in_order(primer_book)
        first_order.add_book_in_order(blue_book)
        first_order.add_book_in_order(about_mouse)
        first_order.print_info_order()
        print()

        second_order = Order(second_customer)
        second_order.add_book_in_order(first_book)
        second_order.add_book_in_order(blue_book)
        second_order.add_book_in_order(blue_book)
        second_order.add_book_in_order(b_a_book)
        second_order.add_book_in_order(b_a_book)
        second_order.print_info_order()
        print()

        third_order = Order(first_customer)
        third_order.add_book_in_order(blue_book)
        third_order.add_book_in_order(blue_book)
        third_order.add_book_in_order(about_mouse)
        third_order.print_info_order()
        print()

        first_package = Package(first_order)
        second_package = Package(second_order)
        third_package = Package(third_order)
        first_package.print_package_info()
        print()
        second_package.print_package_info()
        print()
        third_order.print_info_order()
        print()

        # Create and send first letter
        first_letter = Envelop(first_package)
        first_letter.send_mail()
        first_letter.print_info()

        # Create and send second letter
        second_letter = Envelop(second_package)
        second_letter.send_mail()
        second_letter.print_info()

        # Create and send second letter
        third_letter = Envelop(third_package)
        third_letter.send_mail()
        third_letter.print_info()

        print('After orders:')
        my_bookstore.print_summary_of_all_bookstore()
        my_bookstore.print_summary_of_all_customers()

    def print_bookstore_only_before_and_after() -> None:
        """Docstring: Method to print information about bookstore catalog before and after orders"""
        print('\nHomework 04 (2023.04.13)')
        print('-' * 24)
        print()
        print('LOG_INFO: Launch method "print_bookstore_only_before_and_after"')
        my_bookstore = BookStore()
        first_book = NewBook(20, 12, 'Chook and Gek', 'Arcadii Gaidar', 150, 10, 'ru', 'Belarus', True,
                             ('Chook and Gek were brothers.',
                              'They received a telegram but quarreled.',
                              'And the story began...'))
        my_bookstore.add_book(first_book)
        primer_book = NewBook(15, 5, 'Primer Book', 'Group of authors', 100, 3, 'en', 'US', True,
                              ('A - Apple.',
                               'B - Banana.',
                               'C - Cucumber.'))
        my_bookstore.add_book(primer_book)
        blue_book = NewBook(100, 25, 'Blue Book', 'Blue Author', 666, 18, 'by', 'Belarus', True,
                            ('My name is Alexey and I am an alcoholic.',
                             'I really like to drink beer.',
                             'And I will be drink it every week!'))
        my_bookstore.add_book(blue_book)
        b_a_book = NewBook(5, 50, 'Murder in the Front Row', 'Brian Lew', 272, 18, 'US', 'United States', True,
                           ('This is a story about roots of thrash metal.',
                            'It began at the Bay Area in San Francisco.',
                            'It was in the early eighties...'))
        my_bookstore.add_book(b_a_book)
        about_mouse = NewBook(1, 100, 'Pook the mouse', 'Steeve Edgard', 94, 6, 'UK', 'United Kingdom', True,
                              ('There lived a little mouse Pook.',
                               'She liked to fart very loudly.',
                               'So no one was friends with her...'))
        my_bookstore.add_book(about_mouse)

        first_customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', 'Minsk', 'Card')
        my_bookstore.add_customer(first_customer)
        second_customer = Customer('Ivan', 'Ivanov', 'ivan_i', '123456', 'Grodno', 'Card')
        my_bookstore.add_customer(second_customer)

        print('Before orders:')
        my_bookstore.print_summary_of_all_bookstore()
        my_bookstore.print_summary_of_all_customers()

        first_order = Order(first_customer)
        first_order.add_book_in_order(primer_book)
        first_order.add_book_in_order(primer_book)
        first_order.add_book_in_order(blue_book)
        first_order.add_book_in_order(about_mouse)

        second_order = Order(second_customer)
        second_order.add_book_in_order(first_book)
        second_order.add_book_in_order(blue_book)
        second_order.add_book_in_order(blue_book)
        second_order.add_book_in_order(b_a_book)
        second_order.add_book_in_order(b_a_book)

        third_order = Order(first_customer)
        third_order.add_book_in_order(blue_book)
        third_order.add_book_in_order(blue_book)
        third_order.add_book_in_order(about_mouse)

        first_package = Package(first_order)
        second_package = Package(second_order)
        third_package = Package(third_order)

        first_letter = Envelop(first_package)
        first_letter.send_mail()

        second_letter = Envelop(second_package)
        second_letter.send_mail()

        third_letter = Envelop(third_package)
        third_letter.send_mail()

        print('After orders:')
        my_bookstore.print_summary_of_all_bookstore()
        my_bookstore.print_summary_of_all_customers()

    # Print all information from all methods:
    print_everything()

    # Print information about bookstore catalog before and after orders:
    print_bookstore_only_before_and_after()
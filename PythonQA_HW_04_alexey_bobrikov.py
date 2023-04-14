# Homework 04 (2023.04.13)
from PythonQA_HW_03_alexey_bobrikov import Book


class BookStore:
    """Docstring: Class BookStore"""
    address = 'Minsk'

    def __init__(self) -> None:
        """Docstring: Constructor for class BookStore"""
        self.books = dict()
        self.customers = dict()

    def print_summary_of_all_bookstore(self) -> None:
        """Docstring: Function for print summary of all books in BookStore"""
        print('List of books in BookStore:')
        for book_info in self.books.values():
            print(f'\tTitle: {book_info["Title"]:25s}Author: {book_info["Author"]:20s}'
                  f'ID: {book_info["ID"]:<15}Amount: {book_info["Amount"]:<5}Price: {book_info["Price"]:<5}', end='\n')
        print()

    def print_summary_of_all_customers(self) -> None:
        """Docstring: Function for print summary of all customers in BookStore"""
        print('Orders of customers in BookStore:')
        for cust_info in self.customers.values():
            print(f'\t{cust_info["Name"] + " " + cust_info["Surname"]:20s}: {cust_info["Orders"]}', end='\n')
        print()


class NewBook(Book):
    """Docstring: Class NewBook extends class Book from module 'PythonQA_HW_03_alexey_bobrikov'"""

    def __init__(self, amount: int, price: int, *args: (str, int, bool, dict)) -> None:
        """Docstring: Constructor for class NewBook"""
        super().__init__(*args)
        args[7][f'{self.__hash__()}']['Amount'] = amount
        args[7][f'{self.__hash__()}']['Price'] = price


class Customer:
    """Class Customer"""

    def __init__(self, *args: (str, dict)) -> None:
        """Constructor for class Customer"""
        self.new_customer = {
            'ID': self.__hash__(),
            'Name': args[0],
            'Surname': args[1],
            'Login': args[2],
            'Password': args[3],
            'Address': args[5],
            'Payment method': args[6],
            'Orders': dict()
        }
        args[4][f'{self.new_customer["Name"]} {self.new_customer["Surname"]}'] = self.new_customer


class Order:
    """Docstring: Class Order"""

    def __init__(self, customer: Customer) -> None:
        """Docstring: Constructor for class Order"""
        self.id = self.__hash__()
        self.customer = customer
        self.books = []
        self.total = 0
        self.total_with_sale = 0

    def add_book_in_order(self, book: NewBook) -> None:
        """Docstring: Method to add book in order"""
        count = 0
        sale_coefficient = 0.5
        if book.my_book['Amount'] > 0:
            for item in self.books:
                if item == book:
                    count += 1
            if count > 0:
                self.total_with_sale += book.my_book["Price"] * sale_coefficient
            else:
                self.total_with_sale += book.my_book["Price"]
            self.total += book.my_book["Price"]
            self.books.append(book)
            book.my_book['Amount'] -= 1

    def print_info_order(self) -> None:
        """Docstring: Print information about order"""
        print(f'ORDER №_{self.__hash__()}:')
        print('-' * 28)
        print(f'Customer: {self.customer.new_customer["Name"]} {self.customer.new_customer["Surname"]}')
        print('Books in order:')
        for book in self.books:
            print(f'\t{book.my_book["Title"]}, Price: {book.my_book["Price"]} BYN')
        print(f'Total price: {self.total} BYN')
        print(f'Total price with sale: {self.total_with_sale} BYN')
        print(f'Sale: {self.total - self.total_with_sale}')


class Package:
    """Docstring: Class Package"""
    def __init__(self, order: Order) -> None:
        self.order = order
        stamps_quantity = Stamp(BookStore.address, order.customer.new_customer['Address']).get_quantity_stamps()
        stamp_price = 3.5
        self.package = {
            'Order': self.order,
            'Stamps quantity': stamps_quantity,
            'Package price': order.total_with_sale + stamp_price * stamps_quantity
        }
        order.customer.new_customer['Orders'][f'Order №_{order.id}'] = str(order.total_with_sale) + ' BYN'

    def print_package_info(self) -> None:
        """Docstring: Method to print information about package"""
        print('Package with')
        self.order.print_info_order()
        print(f'Package price: {self.package["Package price"]}')


class Stamp:
    """Docstring: Class Stamp"""
    stamps_quantity = 0

    def __init__(self, adr_from: str, adr_to: str) -> None:
        """Docstring: Constructor for class Stamp"""
        self.adr_from = adr_from
        self.adr_to = adr_to

    def get_quantity_stamps(self) -> int:
        """Docstring: Method to return quantity stamps"""
        if self.adr_from == self.adr_to:
            self.stamps_quantity = 1
        else:
            self.stamps_quantity = 2
        return self.stamps_quantity


class CodeTable:
    """Docstring: Class CodeTable"""
    MAIL_CODES = {
        "Minsk": 123000,
        "Grodno": 225000,
        "Brest": 321000,
        "Gomel": 555000,
        "Vitebsk": 100200,
        "Mogilev": 666000
    }


class Envelop:
    """Docstring: Class Envelop"""

    def __init__(self, package: Package) -> None:
        """Docstring: Constructor for class Envelop"""
        self.adr_from = BookStore.address
        self.adr_to = package.package['Order'].customer.new_customer['Address']
        self.mail_code = self.generate_code(self.adr_to)
        self.mail_stamp = self.generate_stamp()
        self.package = package
        self.status = "Not sent"

    @staticmethod
    def generate_code(adr_to) -> int:
        """Docstring: Method to generate mail code"""
        return CodeTable.MAIL_CODES.get(adr_to)

    def generate_stamp(self) -> int:
        """Docstring: Method to generate of quantity mail stamps"""
        return Stamp(self.adr_from, self.adr_to).get_quantity_stamps()

    def print_info(self) -> None:
        """Docstring: Method to print information about letter"""
        print("Information about letter:")
        print(f'Address FROM: {self.adr_from}')
        print(f'Address TO: {self.adr_to}')
        print(f'Mail code: {self.mail_code}')
        print(f'Quantity of mail stamps: {self.mail_stamp}')
        self.package.print_package_info()
        print(f'Status: {self.status}')
        print()

    def send_mail(self):
        """Docstring: Method to send mail"""
        self.status = "Sent"


# Main program entry point
if __name__ == '__main__':
    def print_everything() -> None:
        """Docstring: Method to print all information from all methods"""
        print('\nHomework 04 (2023.04.13)')
        print('-' * 24)
        print()
        my_bookstore = BookStore()
        first_book = NewBook(20, 12, 'Chook and Gek', 'Arcadii Gaidar', 150, 10, 'ru', 'Belarus', True,
                             my_bookstore.books,
                             ('Chook and Gek were brothers.',
                              'They received a telegram but quarreled.',
                              'And the story began...'))
        primer_book = NewBook(15, 5, 'Primer Book', 'Group of authors', 100, 3, 'en', 'US', True,
                              my_bookstore.books,
                              ('A - Apple.',
                               'B - Banana.',
                               'C - Cucumber.'))
        blue_book = NewBook(100, 25, 'Blue Book', 'Blue Author', 666, 18, 'by', 'Belarus', True,
                            my_bookstore.books,
                            ('My name is Alexey and I am an alcoholic.',
                             'I really like to drink beer.',
                             'And I will be drink it every week!'))
        b_a_book = NewBook(5, 50, 'Murder in the Front Row', 'Brian Lew', 272, 18, 'US', 'United States', True,
                           my_bookstore.books,
                           ('This is a story about roots of thrash metal.',
                            'It began at the Bay Area in San Francisco.',
                            'It was in the early eighties...'))
        about_mouse = NewBook(1, 100, 'Pook the mouse', 'Steeve Edgard', 94, 6, 'UK', 'United Kingdom', True,
                              my_bookstore.books,
                              ('There lived a little mouse Pook.',
                               'She liked to fart very loudly.',
                               'So no one was friends with her...'))

        my_bookstore.print_summary_of_all_bookstore()

        first_customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', my_bookstore.customers, 'Minsk', 'Card')
        second_customer = Customer('Ivan', 'Ivanov', 'ivan_i', '123456', my_bookstore.customers, 'Grodno', 'Card')
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
        my_bookstore = BookStore()
        first_book = NewBook(20, 12, 'Chook and Gek', 'Arcadii Gaidar', 150, 10, 'ru', 'Belarus', True,
                             my_bookstore.books,
                             ('Chook and Gek were brothers.',
                              'They received a telegram but quarreled.',
                              'And the story began...'))
        primer_book = NewBook(15, 5, 'Primer Book', 'Group of authors', 100, 3, 'en', 'US', True,
                              my_bookstore.books,
                              ('A - Apple.',
                               'B - Banana.',
                               'C - Cucumber.'))
        blue_book = NewBook(100, 25, 'Blue Book', 'Blue Author', 666, 18, 'by', 'Belarus', True,
                            my_bookstore.books,
                            ('My name is Alexey and I am an alcoholic.',
                             'I really like to drink beer.',
                             'And I will be drink it every week!'))
        b_a_book = NewBook(5, 50, 'Murder in the Front Row', 'Brian Lew', 272, 18, 'US', 'United States', True,
                           my_bookstore.books,
                           ('This is a story about roots of thrash metal.',
                            'It began at the Bay Area in San Francisco.',
                            'It was in the early eighties...'))
        about_mouse = NewBook(1, 100, 'Pook the mouse', 'Steeve Edgard', 94, 6, 'UK', 'United Kingdom', True,
                              my_bookstore.books,
                              ('There lived a little mouse Pook.',
                               'She liked to fart very loudly.',
                               'So no one was friends with her...'))

        first_customer = Customer('Alexey', 'Bobrikov', 'alex_b', 'qwerty', my_bookstore.customers, 'Minsk', 'Card')
        second_customer = Customer('Ivan', 'Ivanov', 'ivan_i', '123456', my_bookstore.customers, 'Grodno', 'Card')

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

    # print_everything()
    print_bookstore_only_before_and_after()
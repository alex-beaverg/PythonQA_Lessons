# Homework 12, file 2 - (2023.07.13)
# Homework. Classes

class Book:
    """Docstring: Class Book"""

    def __init__(self, title: str, author: str, quantity: int, price: int) -> None:
        """Docstring: Constructor for class Book"""
        self.id = self.__hash__()
        self.title = title
        self.author = author
        self.quantity = quantity
        self.price = price
        self.places = []

    def add_place(self, place) -> None:
        """Docstring: Method to add place"""
        self.places.append(place.name)

    def print_information(self) -> None:
        """Docstring: Print information about book"""
        print(f'\nBook ID: {self.id}')
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Quantity: {self.quantity}')
        print(f'Price: {self.price}')
        print('Places:')
        for place in self.places:
            print(f'\t{place}')


class BookCompany:
    """Docstring: class BookCompany"""
    pass


class BookShop(BookCompany):
    """Docstring: class BookShop extends class BookCompany"""

    def __init__(self, name: str) -> None:
        """Docstring: Constructor for class BookShop"""
        self.name = name
        self.books = []

    def add_book(self, book: Book) -> None:
        """Docstring: Method to add book to BookShop"""
        if self.name not in book.places:
            self.books.append(book)
            book.add_place(self)
        else:
            print(f"""Book "{book.title}" has not been added to "{self.name}" """)


class BookStock(BookCompany):
    """Docstring: class BookStock extends class BookCompany"""

    def __init__(self, name: str) -> None:
        """Docstring: Constructor for class BookStock"""
        self.name = name
        self.books = []

    def add_book(self, book: Book) -> None:
        """Docstring: Method to add book to BookStock"""
        if self.name not in book.places:
            self.books.append(book)
            book.add_place(self)
        else:
            print(f"""Book "{book.title}" has not been added to "{self.name}" """)


class Order:
    """Docstring: class Order"""

    def __init__(self) -> None:
        """Docstring: Constructor for class Order"""
        self.id = str(self.__hash__())[-4:]
        self.books = {}
        self.statuses = ['in progress', 'paid', 'gathered', 'delivered']
        self.status = self.statuses[0]
        self.places = []

    def add_book(self, book: Book, quantity=1) -> None:
        """Docstring: Method to add book to Order"""
        if book.title in self.books:
            self.books[book.title] += quantity
        else:
            self.books[book.title] = quantity
        for place in book.places:
            if place not in self.places:
                if len(self.places) == 0:
                    self.places.append(place)
                elif 'Shop' in self.places[0] and 'Shop' in place:
                    self.places.append(place)
                elif 'Stock' in self.places[0] and 'Stock' in place:
                    self.places.append(place)

    def change_status(self):
        """Docstring: Method to change status of order"""
        if self.statuses.index(self.status) < 4:
            self.status = self.statuses[self.statuses.index(self.status) + 1]

    def print_information(self) -> None:
        """Docstring: Print information about order"""
        print(f'\nOrder ID: {self.id}')
        print(f'Status: {self.status}')
        print('Books:')
        for book, quantity in self.books.items():
            print(f'\t{book}: {quantity}')
        print('Places:')
        for place in self.places:
            print(f'\t{place}')


class Customer:
    """Docstring: class Customer"""

    def __init__(self, name: str, surname: str, sex: str, age: int, addresses: dict, phone: str, email: str) -> None:
        """Docstring: Constructor for class Customer"""
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.addresses = addresses
        self.phone = phone
        self.email = email
        self.orders = {}

    def add_order(self, order: Order) -> None:
        """Docstring: Method to add order to Customer"""
        self.orders[order.id] = order.status

    def print_information(self) -> None:
        """Docstring: Print information about customer"""
        print(f'\nName: {self.name}')
        print(f'Surname: {self.surname}')
        print(f'Sex: {self.sex}')
        print(f'Age: {self.age}')
        print('Addresses:')
        for address_type, address in self.addresses.items():
            print(f'\t{address_type}: {address}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')
        print('Orders:')
        for order_id, status in self.orders.items():
            print(f'\t{order_id}: {status}')

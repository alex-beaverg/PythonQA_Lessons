# Homework 09, file 2 (2023.06.12)
# Homework

def some_actions_with_list() -> None:
    """Docstring: Method to some actions with container list()"""
    print("\nTask 1. Actions with list:")
    print("=" * 26)

    # Create empty list:
    list_for_lists = list()

    # Print list_for_lists before all actions:
    print("\nPrint list_for_lists before all actions:")
    print(list_for_lists)

    # Generate 3 lists:
    list1 = list(range(1, 4))
    list2 = list(i ** 2 for i in range(1, 4))
    list3 = list(i + i for i in range(1, 4))

    # Add 3 lists to empty list:
    list_for_lists.append(list1)
    list_for_lists.append(list2)
    list_for_lists.append(list3)

    # Print list_for_lists as a matrix after appends:
    print("\nPrint list_for_lists as a matrix after appends:")
    print(*list_for_lists, sep="\n")

    # Change items im main diagonal in matrix:
    for i in range(len(list_for_lists)):
        for j in range(len(list_for_lists[0])):
            if i == j:
                list_for_lists[i][j] = 0

    # Print list_for_lists as a matrix after main diagonal changes:
    print("\nPrint list_for_lists as a matrix after main diagonal changes:")
    print(*list_for_lists, sep="\n")

    # Change items higher than main diagonal in matrix:
    for i in range(len(list_for_lists)):
        for j in range(len(list_for_lists[0])):
            if i < j:
                list_for_lists[i][j] = 1

    # Print list_for_lists as a matrix after changes items higher than main diagonal:
    print("\nPrint list_for_lists as a matrix after changes items higher than main diagonal:")
    print(*list_for_lists, sep="\n")

    # Change items lower than main diagonal in matrix:
    for i in range(len(list_for_lists)):
        for j in range(len(list_for_lists[0])):
            if i > j:
                list_for_lists[i][j] = 2

    # Print list_for_lists as a matrix after changes items lower than main diagonal:
    print("\nPrint list_for_lists as a matrix after changes items lower than main diagonal:")
    print(*list_for_lists, sep="\n")

    # All changes in one double cycle:
    for i in range(len(list_for_lists)):
        for j in range(len(list_for_lists[0])):
            if i == j:
                list_for_lists[i][j] = 3
            elif i < j:
                list_for_lists[i][j] = 5
            else:
                list_for_lists[i][j] = 7

    # Print list_for_lists as a matrix after changes items in one double cycle:
    print("\nPrint list_for_lists as a matrix after changes items in one double cycle:")
    print(*list_for_lists, sep="\n")


def some_actions_with_tuple() -> None:
    """Docstring: Method to some actions with container tuple()"""
    print("\n\nTask 2. Actions with tuple:")
    print("=" * 27)

    # Generate tuple with tuples:
    tuple_with_tuples = tuple(tuple(range(i, i + 3)) for i in range(1, 7, 2))

    # Print tuple_with_tuples as a matrix:
    print("\nPrint tuple_with_tuples as a matrix:")
    print(*tuple_with_tuples, sep="\n")

    # Print indexes of tuple_with_tuples as a matrix:
    print("\nPrint indexes of tuple_with_tuples as a matrix:")
    for i in range(len(tuple_with_tuples)):
        for j in range(len(tuple_with_tuples[0])):
            print(f"({i}, {j})", end=" ")
        print()

    # Print sum of tuple_with_tuples items:
    print("\nPrint sum of tuple_with_tuples items:")
    summa = 0
    for i in range(len(tuple_with_tuples)):
        for j in range(len(tuple_with_tuples[0])):
            summa += tuple_with_tuples[i][j]
    print(summa)

    # Print sum of tuple_with_tuples items in main diagonal:
    print("\nPrint sum of tuple_with_tuples items in main diagonal:")
    summa = 0
    for i in range(len(tuple_with_tuples)):
        for j in range(len(tuple_with_tuples[0])):
            if i == j:
                summa += tuple_with_tuples[i][j]
    print(summa)

    # Print sum of tuple_with_tuples items out of main diagonal:
    print("\nPrint sum of tuple_with_tuples items out of main diagonal:")
    summa = 0
    for i in range(len(tuple_with_tuples)):
        for j in range(len(tuple_with_tuples[0])):
            if i != j:
                summa += tuple_with_tuples[i][j]
    print(summa)

    # Print sum of tuple_with_tuples items in not main diagonal:
    print("\nPrint sum of tuple_with_tuples items in not main diagonal:")
    summa = 0
    for i in range(len(tuple_with_tuples)):
        for j in range(len(tuple_with_tuples[0])):
            if i + j == len(tuple_with_tuples) - 1:
                summa += tuple_with_tuples[i][j]
    print(summa)


def some_actions_with_dict() -> None:
    """Docstring: Method to some actions with container dict()"""
    print("\n\nTask 3. Actions with dict:")
    print("=" * 26)

    # Create empty dict:
    dictionary = dict()

    # Print dictionary before all actions:
    print("\nPrint dictionary before all actions:")
    print(dictionary)

    # Add elements to dictionary:
    dictionary['name'] = 'Alexey'
    dictionary['surname'] = 'Bobrikov'
    dictionary['education'] = 'IT Step'
    dictionary['address'] = 'Minsk'

    # Print dictionary after adding elements:
    print("\nPrint dictionary after adding elements:")
    print(dictionary)

    # Print dictionary after adding elements as an elements:
    print("\nPrint dictionary after adding elements as an elements:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

    # Change elements in dictionary:
    dictionary['name'] = 'John'
    dictionary['surname'] = 'Black'
    dictionary['address'] = 'Seattle'

    # Print dictionary after changes:
    print("\nPrint dictionary after changes as an elements:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

    # Get and print value of element 'name' from dictionary:
    print("\nGet and print value of element 'name' from dictionary:")
    print(dictionary.get('name'))

    # Delete elements 'education' and 'address' from dictionary:
    dictionary.pop('education')
    dictionary.pop('address')

    # Print dictionary after deleting elements:
    print("\nPrint dictionary after deleting elements:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

    # Clear dictionary:
    dictionary.clear()

    # Print dictionary after clearing:
    print("\nPrint dictionary after clearing:")
    print(dictionary)


class ShoppingList:
    """Docstring: class ShoppingList as a dictionary container"""

    def __init__(self):
        """Docstring: Constructor for class ShoppingList"""
        self.items = dict()

    def __contains__(self, item):
        """Docstring: If contains..."""
        return item in self.items

    def __setitem__(self, key, value):
        """Docstring: Setter"""
        self.items[key] = value

    def __getitem__(self, item):
        """Docstring: Getter"""
        return self.items[item]


def some_actions_with_shopping_list() -> None:
    """Docstring: Method to some actions with container ShoppingList()"""
    print("\n\nTask 4. Actions with ShoppingList:")
    print("=" * 34)

    # Create empty dict:
    my_shopping_list = ShoppingList().items

    # Print my_shopping_list before all actions:
    print("\nPrint my_shopping_list before all actions:")
    print(my_shopping_list)

    # Add groceries to my_shopping_list:
    my_shopping_list['beer'] = 5
    my_shopping_list['chips'] = 2
    my_shopping_list['bread'] = 0.5
    my_shopping_list['butter'] = 1
    my_shopping_list['tomato'] = 4
    my_shopping_list['sausage'] = 1

    # Print my_shopping_list after adding groceries:
    print("\nPrint my_shopping_list after adding groceries:")
    print(my_shopping_list)

    # Print my_shopping_list after adding groceries as an elements:
    print("\nPrint my_shopping_list after adding groceries as an elements:")
    for key, value in my_shopping_list.items():
        print(f"{key}: {value}")

    # Print message if condition is true or false [true]:
    print("\nPrint message if condition is true or false [true]:")
    if 'beer' in my_shopping_list and my_shopping_list['beer'] >= 4:
        print("I'm really happy!!!")
    else:
        print("I'm so sad...")

    # Print message if condition is true or false [false]:
    print("\nPrint message if condition is true or false [false]:")
    if 'beer' in my_shopping_list and my_shopping_list['beer'] > 10:
        print("I'm really happy!!!")
    else:
        print("I'm so sad...")

    # Delete groceries from my_shopping_list after going to store:
    my_shopping_list.pop('beer')
    my_shopping_list.pop('chips')
    my_shopping_list.pop('sausage')

    # Print message if condition is true or false after going to store [true]:
    print("\nPrint message if condition is true or false after going to store [true]:")
    if 'beer' not in my_shopping_list or my_shopping_list['beer'] < 2:
        print("I'm really happy!!!")
    else:
        print("I'm so sad...")

    # Print my_shopping_list after going to store as an elements:
    print("\nPrint my_shopping_list after going to store as an elements:")
    for key, value in my_shopping_list.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    some_actions_with_list()
    some_actions_with_tuple()
    some_actions_with_dict()
    some_actions_with_shopping_list()

# Homework 12, file 1 - (2023.07.13)
# Classwork

import pickle
from xml.dom.minidom import parse


class IOEngine:
    """Docstring: class IOEngine (Input/Output Engine)"""

    @staticmethod
    def read_text_files() -> list:
        """Docstring: Method to read information from text files_for_classwork"""
        with open('files_for_classwork/file_for_reading_1.txt', 'r') as file_read_1:
            lines = []
            for line in file_read_1:
                lines.append(line.strip())
            with open('files_for_classwork/file_for_reading_2.txt', 'r') as file_read_2:
                for line in file_read_2:
                    lines.append(line.strip())
        print('\nAll lines from two files_for_classwork:')
        print('=' * 38)
        for line in lines:
            print(line)
        return lines

    @staticmethod
    def write_text_file() -> None:
        """Docstring: Method to write information to text file"""
        all_lines = IOEngine.read_text_files()
        print('\nOnly "String" lines from two files_for_classwork into result file:')
        print('=' * 65)
        with open('files_for_classwork/file_for_result.txt', 'w') as file_write:
            for line in all_lines:
                if 'String' in line:
                    print(line)
                    file_write.write(line + '\n')

    @staticmethod
    def write_binary_file() -> None:
        """Docstring: Method to write information to binary file"""
        text = 'Secret binary information!!!'
        with open('files_for_classwork/file_for_result_bin.binary', 'wb') as bin_write:
            pickle.dump(text, bin_write)

    @staticmethod
    def read_binary_file() -> None:
        """Docstring: Method to read information from binary file"""
        with open('files_for_classwork/file_for_result_bin.binary', 'rb') as bin_read:
            result = pickle.load(bin_read)
            print(f'\nInfo from binary file:\n{"=" * 21}\n{result}')

    @staticmethod
    def read_xml_file_minidom() -> None:
        """Docstring: Method to read information from XML file"""
        with parse('files_for_classwork/file_with_xml.xml') as xml_doc:
            packages = xml_doc.getElementsByTagName('package')
            print('\nTravel Packages:')
            print('=' * 15)
            for package in packages:
                package_id = package.getAttribute('id')
                description = package.getElementsByTagName('description')[0].firstChild.data
                price = package.getElementsByTagName('price')[0].firstChild.data
                duration = package.getElementsByTagName('duration')[0].firstChild.data
                quantity = int(package.getElementsByTagName('quantity')[0].firstChild.data)
                print(f'Package ID: {package_id}')
                print(f'Description: {description}')
                print(f'Price: {price}')
                print(f'Duration: {duration}')
                print(f'Quantity: {quantity}\n')


if __name__ == "__main__":
    IOEngine.write_text_file()

    IOEngine.write_binary_file()
    IOEngine.read_binary_file()

    IOEngine.read_xml_file_minidom()

# Homework 23 - (2023.10.19)
# Homework -> File processing decorator, User Interface, Builder Pattern

from typing import Self
from pyunpack import Archive
from patoolib.util import PatoolError
import patoolib
from tkinter import *
from tkinter import ttk


def processing_decorator(decorated_func: ()) -> ():
    """Function -> File processing decorator"""

    def wrapper(*args) -> ():
        """Function to wrapp around the original function"""
        action = ActionsForFileProcessing()
        action \
            .unzip_file(args[0] + '.zip', 'files/') \
            .unrar_file(args[0] + '.rar', 'files/')
        decorated_func(*args)

    return wrapper


class ActionsForFileProcessing:
    """Class with builder actions for file processing"""

    def unzip_file(self, file_path: str, dir_path: str) -> Self:
        """Method to unzip file"""
        try:
            Archive(file_path).extractall(dir_path)
        except ValueError:
            print('Unzip ERROR')
        return self

    def unrar_file(self, file_path: str, dir_path: str) -> Self:
        """Method to unrar file"""
        try:
            patoolib.extract_archive(file_path, outdir=dir_path)
        except PatoolError:
            print('Unrar ERROR')
        return self


class Application:
    """Docstring: Class Application for User Interface for unpacking files"""

    def __init__(self):
        """Docstring: Constructor for class Application"""
        self.__root = Tk()
        self.__unzip_checkbutton_selection = False
        self.__unrar_checkbutton_selection = False

    def run_app(self):
        """Docstring: Method to run application"""
        self.__create_app()
        self.__create_content()

    def __create_app(self):
        """Docstring: Method to create application"""
        self.__root.title('Unpacking text file application')
        self.__root.iconbitmap(default='files/favicon.ico')
        self.__root.geometry('400x120+760+100')
        self.__root.resizable(False, False)
        self.__root.protocol("WM_DELETE_WINDOW", self.__finish)

    def __create_content(self):
        """Docstring: Method to create content for application"""
        self.__create_label()
        self.__create_unzip_checkbutton()
        self.__create_unrar_checkbutton()
        self.__create_read_file_button()
        self.__root.mainloop()

    def __create_label(self):
        """Docstring: Method to create label"""
        self.__label = ttk.Label(text='Choose unpack parameters:')
        self.__label.pack(padx=20, pady=3, anchor=NW)

    def __create_unrar_checkbutton(self):
        """Docstring: Method to create unrar checkbutton"""
        self.__enabled_unrar = IntVar()
        self.__enabled_unrar.set(0)
        self.__unrar_checkbutton = ttk.Checkbutton(text='UnRAR', variable=self.__enabled_unrar, command=self.__select)
        self.__unrar_checkbutton.pack(padx=20, pady=3, anchor=NW)

    def __create_unzip_checkbutton(self):
        """Docstring: Method to create unzip checkbutton"""
        self.__enabled_unzip = IntVar()
        self.__enabled_unzip.set(0)
        self.__unzip_checkbutton = ttk.Checkbutton(text='UnZIP', variable=self.__enabled_unzip, command=self.__select)
        self.__unzip_checkbutton.pack(padx=20, pady=3, anchor=NW)

    def __create_read_file_button(self):
        """Docstring: Method to create to read file button"""
        self.__read_file_button = ttk.Button(text='Read file', command=self.__click_read_file_button)
        self.__read_file_button.pack(padx=20, pady=3, anchor=NW)

    def __click_read_file_button(self):
        """Docstring: Method to get results after click to read file button"""
        if self.__unzip_checkbutton_selection and self.__unrar_checkbutton_selection:
            self.__read_info_from_file('files/textfile')
        self.__finish()

    def __select(self):
        """Docstring: Check selection check buttons"""
        if self.__enabled_unzip.get() == 1:
            self.__unzip_checkbutton_selection = True
        if self.__enabled_unrar.get() == 1:
            self.__unrar_checkbutton_selection = True

    def __finish(self):
        self.__root.destroy()

    @staticmethod
    @processing_decorator
    def __read_info_from_file(path_from: str, mode='r') -> None:
        """Docstring: Function to read info from file"""
        lines = []
        try:
            with open(path_from + '.txt', mode) as file_read:
                for line in file_read:
                    lines.append(line.strip())
        except FileNotFoundError:
            pass
        else:
            Application.__write_info_to_text_file('files/textfile_result.txt', lines)

    @staticmethod
    def __write_info_to_text_file(path_to: str, info: [], mode='w') -> None:
        """Docstring: Function to write info to text file"""
        try:
            with open(path_to, mode) as file_write:
                for element in info:
                    try:
                        elem = eval(element)
                    except SyntaxError:
                        elem = element
                    finally:
                        file_write.write(str(elem) + '\n')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = Application()
    app.run_app()

# Homework 21, file 1 - (2023.10.12)
# Homework -> Using nested decorators


from pyunpack import Archive
from patoolib.util import PatoolError
import patoolib


def unzip_decorator(decorated_func: ()) -> ():
    """Function -> Custom unzip decorator"""

    def wrapper(*args) -> ():
        """Function to wrapp around the original function"""
        try:
            Archive(args[0] + '.zip').extractall('./')
        except ValueError:
            pass
        finally:
            decorated_func(*args)
    return wrapper


def unrar_decorator(decorated_func: ()) -> ():
    """Function -> Custom unrar decorator"""

    def wrapper(*args) -> ():
        """Function to wrapp around the original function"""
        try:
            patoolib.extract_archive(args[0] + '.rar', outdir='./')
        except PatoolError:
            pass
        finally:
            decorated_func(*args)
    return wrapper


@unzip_decorator
@unrar_decorator
def read_info_from_file(path_from: str, mode='r') -> None:
    """Docstring: Function to read info from file"""
    lines = []
    try:
        with open(path_from + '.txt', mode) as file_read:
            for line in file_read:
                lines.append(line.strip())
    except FileNotFoundError:
        pass
    else:
        write_info_to_text_file('textfile_result.txt', lines, 'w')


def write_info_to_text_file(path_to: str, info: [], mode='w') -> None:
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
    read_info_from_file('textfile', 'r')
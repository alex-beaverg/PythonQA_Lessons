# Homework 10, file 3 - copy (2023.06.15)
# Custom Logging Decorator


def log_decorator(decorated_func: ()) -> ():
    """Function -> Custom logging decorator"""

    def wrapper(*args) -> None:
        """Function to wrapp around the original function"""
        print(f"\n[LOG_INFO]: Run {decorated_func.__name__}(): '{decorated_func.__doc__}'")
        try:
            decorated_func(*args)
        except BaseException as e:
            print(f"** [ERROR]: Function {decorated_func.__name__}() was caused an Exception -> [{e}]")
        else:
            if len(args) == 1:
                print(f"[LOG_INFO]: Function {decorated_func.__name__}() has been executed with argument: {args[0]}")
            elif len(args) > 1:
                print(f"[LOG_INFO]: Function {decorated_func.__name__}() has been executed with arguments: {args}")

    return wrapper


@log_decorator
def first_decorating_function() -> None:
    """First function with custom logging decorator and no arguments"""
    print("- - - function does something - - -")


@log_decorator
def second_decorating_function(arg1) -> None:
    """Second function with custom logging decorator and 1 argument"""
    print(f"- - - function does something with {arg1} - - -")


@log_decorator
def third_decorating_function(arg1, arg2) -> None:
    """Third function with custom logging decorator and 2 arguments"""
    print(f"- - - function does something with {arg1} and {arg2} - - -")


@log_decorator
def fourth_decorating_function(arg1, arg2) -> None:
    """Fourth function with custom logging decorator, 2 arguments and might error"""
    print(f"- - - function divides {arg1} by {arg2} - - -")
    result = arg1 / arg2
    print(f"- - - Result = {result} - - -")


@log_decorator
def fifth_decorating_function(arg1, arg2) -> None:
    """Fourth function with custom logging decorator, 2 arguments and might error"""
    print(f"- - - function multiplies {arg1} and {arg2} - - -")
    result = arg1 + arg2
    print(f"- - - Result = {result} - - -")


@log_decorator
def sixth_decorating_function(arg1, arg2, arg3) -> None:
    """Third function with custom logging decorator and 2 arguments"""
    print(f"- - - function does something with {arg1}, {arg2} and {arg3} - - -")


if __name__ == '__main__':
    first_decorating_function()
    second_decorating_function(100)
    third_decorating_function(100, 200)
    fourth_decorating_function(100, 10)
    fourth_decorating_function(100, 0)
    fifth_decorating_function(5, 10)
    fifth_decorating_function(5, 'SECOND ARG')
    sixth_decorating_function('FIRST ARG', 'SECOND ARG', 'THIRD ARG')

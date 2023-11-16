def log_decorator(test_method: ()) -> ():
    """Function -> Custom test logging decorator"""

    def wrapper(*args) -> ():
        """Function to wrapp around the original test method"""
        print(f"\n[LOG_INFO]: Run test method: {test_method.__name__}()")
        test_method(*args)
        print(f"[LOG_INFO]: Test method {test_method.__name__}() has been executed")

    return wrapper

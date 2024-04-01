import inspect
import os
from datetime import datetime


def get_current_function_name() -> str:
    """
    return present function's name
    """
    return inspect.currentframe().f_back.f_code.co_name


def get_cwd():
    print("__file__", __file__)
    print(os.path.abspath(__file__))
    return os.getcwd()


def get_datetime_str():
    """
    2024_04_01_10_01_31
    """
    return datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S")


def path_join(*args):
    return os.path.join(*args)


def get_abs_path(file):
    """
    Args:
        file (str): __file__

    return abs_path(__file__)
    """
    return os.path.abspath(file)

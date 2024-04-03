import inspect
import os
from datetime import datetime
import torch
import random
import numpy


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


def set_seed(
    seed: int = 0,
    numpy_flag: bool = True,
    random_flag: bool = True,
    torch_flag: bool = True,
):
    if numpy_flag:
        numpy.random.seed(seed)
    if random_flag:
        random.seed(seed)
    if torch_flag:
        # https://pytorch.org/docs/stable/notes/randomness.html#pytorch-random-number-generator
        # You can use torch.manual_seed() to seed the RNG for all devices (both CPU and CUDA):
        torch.manual_seed(seed)

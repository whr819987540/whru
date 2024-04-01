from whru import utils


def example_function():
    print("当前正在执行的函数是:", utils.get_current_function_name())


if __name__ == "__main__":
    example_function()
    print(utils.get_datetime_str())
    utils.path_join("111", "222", "333")

    import os

    print(os.path.join("1", "222", "333"))

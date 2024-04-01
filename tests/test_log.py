from whru.log import get_logger
from whru.utils import path_join, get_abs_path, get_datetime_str

if __name__ == "__main__":
    logger = get_logger("INFO", "test", path_join(get_abs_path(__file__), "../test_data", f"{get_datetime_str()}.log"))
    logger.info("hello world")

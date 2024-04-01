from whru.tensorboard import get_SummaryWriter
from whru.utils import get_datetime_str, path_join, get_abs_path

if __name__ == "__main__":
    print(get_abs_path(__file__), get_datetime_str())
    writer = get_SummaryWriter(
        path_join(get_abs_path(__file__), "../test_data", get_datetime_str())
    )
    writer.add_scalar("acc", 0.1, 0)

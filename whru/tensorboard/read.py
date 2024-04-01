from tensorboard.backend.event_processing.event_accumulator import EventAccumulator


def read_tensorboard(path:str):
    """
        step, value, wall_time
    """
    ea = EventAccumulator(path)
    ea.Reload()
    return ea


def test():
    pass


if __name__ == "__main__":
    ea = read_tensorboard("./test_data")
    print(ea.Tags())
    print(ea.Scalars("test_acc"))

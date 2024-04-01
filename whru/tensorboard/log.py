from torch.utils.tensorboard import SummaryWriter


def get_SummaryWriter(tensorboard_log_path):
    return SummaryWriter(tensorboard_log_path)

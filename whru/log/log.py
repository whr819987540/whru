import logging


def get_logger(log_level, logger_name, log_file:str=None):
    # 2023-08-02 19:23:44 [0] "/home/whr/fs_gnn/dist_gcn_train.py", line 844, DEBUG: torch.Size([512, 500])
    # note: 如果是多进程，对logging模块的初始化需要在每个进程中都运行一次
    # 并且，logging模块是线程安全的，但并不是进程安全的
    # 如果要保证进程安全，需要将其它进程的消息汇总到一个进程，然后由同一进程中的某些logger（标识进程）来完成
    log_format = f'%(asctime)s %(name)s "%(pathname)s", line %(lineno)d, %(levelname)s: %(message)s\n'

    assert (
        log_level in logging._nameToLevel.keys()
    ), f"log_level should be one of {logging._nameToLevel.keys()}"

    handler = logging.StreamHandler()
    handler.setLevel(logging._nameToLevel[log_level])
    formatter = logging.Formatter(fmt=log_format)
    handler.setFormatter(formatter)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging._nameToLevel[log_level])
    logger.addHandler(handler)

    if log_file:
        handler_file = logging.FileHandler(log_file)
        handler_file.setLevel(logging._nameToLevel[log_level])
        handler_file.setFormatter(formatter)
        logger.addHandler(handler_file)

    return logger

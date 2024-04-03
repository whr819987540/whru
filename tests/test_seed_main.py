from test_seed import test
import torch

if __name__ == "__main__":
    # 支持跨module
    test()
    print(torch.randint(0, 10, (3, 3)))
    print(torch.randint(0, 10, (3, 3)))

import torch


def test():
    torch.manual_seed(1)


if __name__ == "__main__":
    print(torch.randint(0, 10, (3, 3)))
    print(torch.randint(0, 10, (3, 3)))
    print("-" * 10)
    test()
    print(torch.randint(0, 10, (3, 3)))
    print(torch.randint(0, 10, (3, 3)))

    # whether manual_seed set seed for gpu
    # ANS: yes
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        print(torch.randint(0, 10, (3, 3), device=device))

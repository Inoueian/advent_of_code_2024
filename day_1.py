import bisect
from collections import defaultdict


def get_two_lists(data):
    list_0 = []
    list_1 = []
    for line in data.splitlines():
        str_0, str_1 = line.split()
        bisect.insort(list_0, int(str_0))
        bisect.insort(list_1, int(str_1))
    return list_0, list_1


def get_sum(data):
    list_0, list_1 = get_two_lists(data)
    return sum(abs(int_0 - int_1) for int_0, int_1 in zip(list_0, list_1))


def process_part_2(data):
    list_ = []
    dict_ = defaultdict(int)
    for line in data.splitlines():
        str_0, str_1 = line.split()
        list_.append(int(str_0))
        dict_[int(str_1)] += 1
    return list_, dict_


def get_product_sum(data):
    list_, dict_ = process_part_2(data)
    return sum(num * dict_[num] for num in list_)


if __name__ == "__main__":
    with open("data/day_1_input.txt", "r") as f:
        data = f.read()

    part_1 = get_sum(data)
    part_2 = get_product_sum(data)

    print(part_1)
    print(part_2)

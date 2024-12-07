import re


def parse_muls(data):
    pattern = r"mul\((\d+),(\d+)\)"
    str_pairs = re.findall(pattern, data)
    return [(int(str_0), int(str_1)) for str_0, str_1 in str_pairs]


def parse_muls_2(data):
    split_by_dos = data.split("do()")
    before_donts = [string.split("don't()")[0] for string in split_by_dos]
    muls = []
    for string in before_donts:
        muls += parse_muls(string)
    return muls


def get_product_sum(data, part_2=False):
    if part_2:
        return sum(int_0 * int_1 for int_0, int_1 in parse_muls_2(data))
    else:
        return sum(int_0 * int_1 for int_0, int_1 in parse_muls(data))


if __name__ == "__main__":
    with open("data/day_3_input.txt", "r") as f:
        data = f.read()

    part_1 = get_product_sum(data)
    part_2 = get_product_sum(data, part_2=True)

    print(part_1)
    print(part_2)

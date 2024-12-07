def is_safe(ints):
    diff = ints[1] - ints[0]
    if 1 <= abs(diff) <= 3:
        decreasing = (diff < 0)
    else:
        return False
    for int_0, int_1 in zip(ints[1:-1], ints[2:]):
        abs_diff = (int_1 - int_0) * (-1)**decreasing
        if (abs_diff < 1) or (abs_diff > 3):
            return False
    return True


def count_safe(data, part_2=False):
    lines = data.splitlines()
    count = 0
    for line in lines:
        ints = [int(str_) for str_ in line.split()]
        if part_2:
            count += is_safe_2(ints)
        else:
            count += is_safe(ints)
    return count


def is_safe_with_omission(ints, index):
    new_ints = ints.copy()
    new_ints.pop(index)
    return is_safe(new_ints)


def is_safe_2(ints):
    # need the first 4 integers to see if the safe sequence is increasing or decreasing
    num_decreasing = sum((int_1 < int_0) for int_0, int_1 in zip(ints[:4], ints[1:5]))
    decreasing = (num_decreasing >= 2)
    for (idx_0, int_0), (_, int_1) in zip(enumerate(ints[:-1]),
                                          enumerate(ints[1:])):
        abs_diff = (int_1 - int_0) * (-1)**decreasing
        if (abs_diff < 1) or (abs_diff > 3):
            return (is_safe_with_omission(ints, idx_0) or
                    is_safe_with_omission(ints, idx_0 + 1))
    return True


if __name__ == "__main__":
    with open("data/day_2_input.txt", "r") as f:
        data = f.read()

    part_1 = count_safe(data)
    part_2 = count_safe(data, part_2=True)

    print(part_1)
    print(part_2)

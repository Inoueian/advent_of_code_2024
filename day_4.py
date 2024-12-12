dirs = ((-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1))


def is_xmas(lines, coord, dir_):
    x_0, y_0 = coord
    x_inc, y_inc = dir_
    for num in range(4):
        x = x_0 + num * x_inc
        y = y_0 + num * y_inc
        try:
            if (x < 0) or (y < 0):
                return False
            elif lines[x][y] != "XMAS"[num]:
                return False
        except IndexError:
            return False
    return True


def count_xmas(data):
    lines = data.splitlines()
    count = 0
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "X":
                count_from_char = sum(is_xmas(lines, (x, y), dir_)
                                      for dir_ in dirs)
                count += count_from_char
    return count


def is_x_mas(lines, coord):
    x, y = coord
    if ((lines[x][y] == "A") and
            ({lines[x - 1][y - 1], lines[x + 1][y + 1]} == {"M", "S"}) and
            ({lines[x - 1][y + 1], lines[x + 1][y - 1]} == {"M", "S"})):
        return True
    else:
        return False


def count_x_mas(data):
    lines = data.splitlines()
    count = 0
    for x in range(1, len(lines) - 1):
        line = lines[x]
        for y in range(1, len(line) - 1):
            if line[y] == "A":
                count += is_x_mas(lines, (x, y))
    return count


if __name__ == "__main__":
    with open("data/day_4_input.txt", "r") as f:
        data = f.read()

    part_1 = count_xmas(data)
    part_2 = count_x_mas(data)

    print(part_1)
    print(part_2)

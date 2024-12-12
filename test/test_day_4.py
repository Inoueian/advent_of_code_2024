from day_4 import *


data = ("MMMSXXMASM\n" +
        "MSAMXMSMSA\n" +
        "AMXSXMAAMM\n" +
        "MSAMASMSMX\n" +
        "XMASAMXAMM\n" +
        "XXAMMXXAMA\n" +
        "SMSMSASXSS\n" +
        "SAXAMASAAA\n" +
        "MAMMMXMMMM\n" +
        "MXMXAXMASX")


def test_is_xmas():
    lines = data.splitlines()
    assert is_xmas(lines, (0, 4), dir_=(1, 1))
    assert not is_xmas(lines, (0, 4), dir_=(0, 1))
    assert is_xmas(lines, (3, 9), dir_=(1, 0))
    assert not is_xmas(lines, (0, 3), dir_=(1, -1))
    assert not is_xmas(lines, (2, 0), dir_=(-1, 0))
    assert not is_xmas(lines, (0, 2), dir_=(0, -1))
    assert not is_xmas(lines, (3, 9), dir_=(0, 1))


def test_count_xmas():
    assert count_xmas(data) == 18


def test_is_x_mas():
    lines = data.splitlines()
    assert is_x_mas(lines, (1, 2))
    assert is_x_mas(lines, (2, 6))
    assert is_x_mas(lines, (7, 1))
    assert not is_x_mas(lines, (0, 1))
    assert not is_x_mas(lines, (1, 1))
    assert not is_x_mas(lines, (4, 4))


def test_count_x_mas():
    assert count_x_mas(data) == 9

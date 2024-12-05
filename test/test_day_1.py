from day_1 import *

data = ("3   4\n" +
        "4   3\n" +
        "2   5\n" +
        "1   3\n" +
        "3   9\n" +
        "3   3")


def test_get_two_lists():
    assert get_two_lists(data) == ([1, 2, 3, 3, 3, 4],
                                   [3, 3, 3, 4, 5, 9])


def test_get_sum():
    assert get_sum(data) == 11


def test_process_part_2():
    list_, dict_ = process_part_2(data)
    assert list_ == [3, 4, 2, 1, 3, 3]
    assert dict_[4] == 1
    assert dict_[3] == 3
    assert dict_[5] == 1
    assert dict_[9] == 1


def test_get_product_sum():
    assert get_product_sum(data) == 31

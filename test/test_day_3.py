from day_3 import *

data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
data_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_parse_muls():
    assert parse_muls(data) == [(2, 4),
                                (5, 5),
                                (11, 8),
                                (8, 5)]


def test_get_product_sum():
    assert get_product_sum(data) == 161


def test_parse_muls_2():
    assert parse_muls_2(data_2) == [(2, 4),
                                    (8, 5)]


def test_get_product_sum_2():
    assert get_product_sum(data_2, part_2=True) == 48

from day_2 import *

data = ("7 6 4 2 1\n" +
        "1 2 7 8 9\n" +
        "9 7 6 2 1\n" +
        "1 3 2 4 5\n" +
        "8 6 4 4 1\n" +
        "1 3 6 7 9")


def test_is_safe():
    assert is_safe([7, 6, 4, 2, 1])
    assert not is_safe([1, 2, 7, 8, 9])
    assert not is_safe([9, 7, 6, 2, 1])
    assert not is_safe([1, 3, 2, 4, 5])
    assert not is_safe([8, 6, 4, 4, 1])
    assert is_safe([1, 3, 6, 7, 9])


def test_count_safe():
    assert count_safe(data) == 2


def test_is_safe_with_omission():
    assert is_safe_with_omission([7, 6, 4, 2, 1], 0)
    assert not is_safe_with_omission([1, 2, 7, 8, 9], 1)
    assert not is_safe_with_omission([9, 7, 6, 2, 1], 2)
    assert is_safe_with_omission([1, 3, 2, 4, 5], 1)
    assert not is_safe_with_omission([1, 3, 2, 4, 5], 0)
    assert not is_safe_with_omission([8, 6, 4, 4, 1], 1)
    assert is_safe_with_omission([8, 6, 4, 4, 1], 2)
    assert is_safe_with_omission([1, 3, 6, 7, 9], 3)
    assert not is_safe_with_omission([72, 73, 75, 77, 79, 82, 79, 85], 5)
    assert is_safe_with_omission([72, 73, 75, 77, 79, 82, 79, 85], 6)


def test_is_safe_2():
    assert is_safe_2([7, 6, 4, 2, 1])
    assert not is_safe_2([1, 2, 7, 8, 9])
    assert not is_safe_2([9, 7, 6, 2, 1])
    assert is_safe_2([1, 3, 2, 4, 5])
    assert is_safe_2([8, 6, 4, 4, 1])
    assert is_safe_2([1, 3, 6, 7, 9])
    assert is_safe_2([72, 73, 75, 77, 79, 82, 79, 85])


def test_count_safe_2():
    assert count_safe(data, part_2=True) == 4

from day_5 import *

data = ("47|53\n" +
        "97|13\n" +
        "97|61\n" +
        "97|47\n" +
        "75|29\n" +
        "61|13\n" +
        "75|53\n" +
        "29|13\n" +
        "97|29\n" +
        "53|29\n" +
        "61|53\n" +
        "97|53\n" +
        "61|29\n" +
        "47|13\n" +
        "75|47\n" +
        "97|75\n" +
        "47|61\n" +
        "75|61\n" +
        "47|29\n" +
        "75|13\n" +
        "53|13\n" +
        "\n" +
        "75,47,61,53,29\n" +
        "97,61,53,29,13\n" +
        "75,29,13\n" +
        "75,97,47,61,53\n" +
        "61,13,29\n" +
        "97,13,75,29,47")


def test_printer():
    printer = Printer(data)
    assert len(printer.rules) == 21
    assert len(printer.updates) == 6


def test_is_valid():
    printer = Printer(data)
    assert printer.is_valid(["75", "47", "61", "53", "29"])
    assert printer.is_valid(["97", "61", "53", "29", "13"])
    assert printer.is_valid(["75", "29", "13"])
    assert not printer.is_valid(["75", "97", "47", "61", "53"])
    assert not printer.is_valid(["61", "13", "29"])
    assert not printer.is_valid(["97", "13", "75", "29", "47"])


def test_get_middle_page_sum():
    assert get_middle_page_sum(data) == 143


def test_fix_incorrect_update():
    printer = Printer(data)
    assert printer.fix_incorrect_update(["75", "97", "47", "61", "53"]) == ["97", "75", "47", "61", "53"]
    assert printer.fix_incorrect_update(["61", "13", "29"]) == ["61", "29", "13"]
    assert printer.fix_incorrect_update(["97", "13", "75", "29", "47"]) == ["97", "75", "47", "29", "13"]


def test_get_middle_page_sum_2():
    assert get_middle_page_sum(data, part_2=True) == 123

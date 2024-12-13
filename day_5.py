from collections import defaultdict


class Printer:
    def __init__(self, data):
        rules_str, updates_str = data.split("\n\n")
        rules_lines = rules_str.splitlines()
        self.rules = [line.split("|") for line in rules_lines]
        updates_lines = updates_str.splitlines()
        self.updates = [line.split(",") for line in updates_lines]

    def is_valid(self, num_strs):
        forbidden = set()
        for num_str in num_strs:
            if num_str in forbidden:
                return False
            else:
                for str_0, str_1 in self.rules:
                    if num_str == str_1:
                        forbidden.add(str_0)
        return True

    def fix_incorrect_update(self, num_strs):
        new_update = []
        put_before_dict = defaultdict(list)
        for str_0, str_1 in self.rules:
            if (str_0 in num_strs) and (str_1 in num_strs):
                put_before_dict[str_0].append(str_1)
        for num_str in num_strs:
            is_added = False
            for index, str_ in enumerate(new_update):
                if str_ in put_before_dict[num_str]:
                    new_update.insert(index, num_str)
                    is_added = True
                    break
            if not is_added:
                new_update.append(num_str)
        return new_update

    def middle_page_sum(self, part_2=False):
        total = 0
        for update in self.updates:
            if part_2:
                if not self.is_valid(update):
                    new_update = self.fix_incorrect_update(update)
                    length = len(new_update)
                    middle_page = int(new_update[(length - 1) // 2])
                    total += middle_page
            else:
                if self.is_valid(update):
                    length = len(update)
                    middle_page = int(update[(length - 1) // 2])
                    total += middle_page
        return total


def get_middle_page_sum(data, part_2=False):
    printer = Printer(data)
    return printer.middle_page_sum(part_2=part_2)


if __name__ == "__main__":
    with open("data/day_5_input.txt", "r") as f:
        data = f.read()

    part_1 = get_middle_page_sum(data)
    part_2 = get_middle_page_sum(data, part_2=True)

    print(part_1)
    print(part_2)

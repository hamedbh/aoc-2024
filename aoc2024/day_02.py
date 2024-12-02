from aoc2024 import utils

with open("data/day_02.txt", "r") as f:
    reports = [
        [int(number_string) for number_string in line.strip().split(" ")]
        for line in f
    ]


def is_safe(levels):
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    is_monotonic = all(diff > 0 for diff in diffs) or all(
        diff < 0 for diff in diffs
    )
    is_close = all(0 < abs(diff) <= 3 for diff in diffs)
    return is_monotonic and is_close


answer1 = sum([is_safe(levels) for levels in reports])


def is_safe_dampened(levels):
    if is_safe(levels):
        return True
    else:
        for i in range(len(levels)):
            dampened = levels.copy()
            dampened.pop(i)
            # dampened = levels[:i] + levels[i + 1:]
            if is_safe(dampened):
                return True
    return False


answer2 = sum([is_safe_dampened(levels) for levels in reports])
utils.print_day(2, answer1, answer2)

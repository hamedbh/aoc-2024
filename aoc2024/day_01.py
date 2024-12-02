from collections import Counter

from aoc2024 import utils

with open("data/day_01.txt", "r") as f:
    lines = [line.strip() for line in f]
numbers = [line.split("   ") for line in lines]
left = [int(number[0]) for number in numbers]
right = [int(number[1]) for number in numbers]
left.sort()
right.sort()
answer1 = sum(
    [
        abs(left_number - right_number)
        for left_number, right_number in zip(left, right)
    ]
)

counts = Counter(right)
answer2 = sum([x * counts[x] for x in left])
utils.print_day(1, answer1, answer2)

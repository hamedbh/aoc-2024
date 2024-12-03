import re

from aoc2024 import utils

with open("data/day_03.txt", "r") as f:
    corrupted = f.read()

p1 = re.compile(r"mul\((\d+),(\d+)\)")
answer1 = sum([int(a) * int(b) for (a, b) in p1.findall(corrupted)])

p2 = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")
instructions = p2.findall(corrupted)
system_on = True
answer2 = 0

for instruction in instructions:
    match instruction[0]:
        case "do()":
            system_on = True
        case "don't()":
            system_on = False
        case _ if system_on:
            answer2 += int(instruction[1]) * int(instruction[2])

utils.print_day(3, answer1, answer2)

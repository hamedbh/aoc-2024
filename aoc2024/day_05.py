from graphlib import TopologicalSorter

from aoc2024 import utils

# with open("example.txt", "r") as f:
#     input = [line.strip() for line in f.readlines()]
with open("data/day_05.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

rules = [tuple(map(int, line.split("|"))) for line in input if "|" in line]
updates = [
    tuple(map(int, line.split(",")))
    for line in input
    if "|" not in line and len(line) > 0
]

assert len(rules) + len(updates) + 1 == len(input)


def get_valid_order(
    rules: list[tuple[int, int]], subset: set[int] | None = None
) -> list[int]:
    graph = {}
    for rule in rules:
        if subset and not set(rule).issubset(subset):
            continue
        k, v = rule
        if k not in graph:
            graph[k] = set([v])
        else:
            graph[k] = set.union(graph[k], set([v]))
    ts = TopologicalSorter(graph)
    # Need to reverse the order of the list as TopologicalSorter sorts
    # value before key
    return list(ts.static_order())[::-1]


good_updates = []
fixed_updates = []
for update in updates:
    correct_order = get_valid_order(rules, subset=set(update))
    if list(update) == correct_order:
        good_updates.append(update)
    else:
        fixed_updates.append(correct_order)

answer1 = sum(update[len(update) // 2] for update in good_updates)

answer2 = sum(update[len(update) // 2] for update in fixed_updates)

utils.print_day(5, answer1, answer2)

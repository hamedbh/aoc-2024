from aoc2024 import utils

with open("data/day_04.txt", "r") as f:
    square = [line.strip() for line in f.readlines()]

transposed = ["".join([row[i] for row in square]) for i in range(len(square))]


def get_diagonals(square: list[str]) -> list[str]:
    size = len(square[0])
    # Get the starting indexes for the left-to-right diagonals
    lr_diag_starts = [(0, i) for i in range(size)] + [
        (i, 0) for i in range(1, size)
    ]
    # Then the full set of indexes for each diagonal
    lr_diag_indexes = [
        [(i, j) for i, j in zip(range(x[0], size), range(x[1], size))]
        for x in lr_diag_starts
    ]
    # Use those diagonals to get the right-left diagonals
    rl_diag_indexes = [
        [(j, size - 1 - i) for j, i in diag] for diag in lr_diag_indexes
    ]
    return [
        "".join([square[i][j] for i, j in diag_indexes])
        for diag_indexes in lr_diag_indexes + rl_diag_indexes
    ]


diagonals = get_diagonals(square)

all_permutations = square + transposed + diagonals
answer1 = sum(
    line.count("XMAS") + line.count("SAMX") for line in all_permutations
)

answer2 = 0
more_letters = {"M", "S"}
for i in range(1, len(square) - 1):
    for j in range(1, len(square[0]) - 1):
        if square[i][j] == "A":
            if (
                {square[i - 1][j - 1], square[i + 1][j + 1]}
                == {square[i - 1][j + 1], square[i + 1][j - 1]}
                == more_letters
            ):
                answer2 += 1

utils.print_day(4, answer1, answer2)

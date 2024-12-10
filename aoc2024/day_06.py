import json

from aoc2024 import utils

# with open("example.txt", "r") as f:
#     input = [line.strip() for line in f.readlines()]

with open("data/day_06.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]
for i, row in enumerate(input):
    if row.find("^") >= 0:
        start_pos = (i, row.find("^"))
lab_map = [list(x) for x in input]


def run_patrol(
    lab_map: list[list[str]],
    start_pos: tuple[int, int],
    current_direction: int,
):
    grid_size = (len(lab_map), len(lab_map[0]))

    all_directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    positions_visited = set()
    positions_visited.add(start_pos)

    visit_path = {}
    current_pos = start_pos
    while True:
        direction = all_directions[current_direction]
        next_pos = (
            current_pos[0] + direction[0],
            current_pos[1] + direction[1],
        )

        if (
            next_pos[0] < 0
            or next_pos[0] >= grid_size[0]
            or next_pos[1] < 0
            or next_pos[1] >= grid_size[1]
        ):
            return {
                "positions_visited": positions_visited,
                "visit_path": visit_path,
                "loop": False,
            }

        if lab_map[next_pos[0]][next_pos[1]] == "#":
            current_direction = (current_direction + 1) % 4
            continue

        else:
            positions_visited.add(next_pos)
            if next_pos not in visit_path:
                visit_path[next_pos] = (current_pos, current_direction)
            elif visit_path[next_pos] == (current_pos, current_direction):
                return {
                    "positions_visited": positions_visited,
                    "visit_path": visit_path,
                    "loop": True,
                }
            current_pos = next_pos


part1_patrol = run_patrol(lab_map, start_pos, 0)
positions_visited = part1_patrol["positions_visited"]
visit_path = part1_patrol["visit_path"]
answer1 = len(positions_visited)

answer2 = 0
copy_lab_map = json.dumps(lab_map)
for i, j in positions_visited:
    candidate_map = json.loads(copy_lab_map)
    candidate_map[i][j] = "#"
    result = run_patrol(candidate_map, start_pos, 0)
    if result["loop"] is True:
        answer2 += 1

utils.print_day(6, answer1, answer2)

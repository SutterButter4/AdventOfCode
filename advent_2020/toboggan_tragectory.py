from typing import Tuple, Dict


def toboggan_tragectory(input_data_location) -> int:
    topology, width, height = parse_input(input_data_location)

    return traverse(topology, width, height, 1, 1) * traverse(topology, width, height, 3, 1) * traverse(topology, width, height, 5, 1) * traverse(topology, width, height, 7, 1) * traverse(topology, width, height, 1, 2)


def traverse(topology: Dict[Tuple[int, int], bool], width: int, height: int, deltax: int, deltay: int) -> int:
    num_trees, x, y = 0, 0, 0

    while y < height:
        if topology[(x, y)]:
            num_trees += 1

        (x, y) = ((x + deltax) % width, y + deltay)

    return num_trees


def get_index(x, y, width) -> int:
    return y * width + (x % width)


def parse_input(input_data_location) -> Tuple[Dict[Tuple[int, int], bool], int, int]:
    with open(input_data_location) as file:
        text = file.read()
        lines = text.split("\n")

        topology = {}

        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                topology[x, y] = (line[x] == "#")

        return topology, len(lines[0]), len(lines)

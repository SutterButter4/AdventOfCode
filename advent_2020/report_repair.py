from typing import List, Tuple, Optional


def report_repair(input_data_filepath: str) -> Tuple[int, int]:
    report_data = parse_input(input_data_filepath)
    report_data.sort()

    pair = find_pair(report_data, 2020)
    (a, b) = (-1, -1)
    if pair:
        (a, b) = pair
    triple = find_triple(report_data, 2020)
    (c, d, e) = (-1, -1, -1)
    if triple:
        (c, d, e) = triple

    return a * b, c * d * e


def parse_input(input_data_filepath: str) -> List[int]:
    with open(input_data_filepath) as file:
        input_str = file.read()

        return [int(x) for x in input_str.split("\n")]


def find_pair(sorted_report: List[int], target_num: int) -> Optional[Tuple[int, int]]:
    front_index = 0
    end_index = len(sorted_report) - 1

    while front_index != end_index:

        a = sorted_report[front_index]
        b = sorted_report[end_index]

        if a + b == target_num:
            return a, b
        elif a + b < target_num:
            front_index += 1
        else:  # a + b > advent_2020
            end_index -= 1

    # given valid input, should never be reached.
    return None


def find_triple(sorted_report: List[int], target: int) -> Optional[Tuple[int, int, int]]:

    for i in sorted_report:
        pair = find_pair(sorted_report, target-i)

        if pair:
            a, b = pair
            return a, b, i

    return None


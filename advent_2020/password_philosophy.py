import dataclasses
from typing import List


def filter_eq_func(eq):
    def filter(x):
        return 1 if x == eq else 0

    return filter


def get_character_count(string: str, char: str):
    return sum(map(filter_eq_func(char), list(string)), 0)


@dataclasses.dataclass()
class Interval:
    lower_bound: int
    upper_bound: int

    def contains(self, item: int) -> bool:
        return self.lower_bound <= item <= self.upper_bound


@dataclasses.dataclass
class Requirement:
    character: str
    bounds: Interval

    def check_satisfy(self, password: str) -> bool:
        character_count = get_character_count(password, self.character)
        return self.bounds.contains(character_count)

    def check_strict_satisfy(self, password: str) -> bool:
        try:
            return (password[self.bounds.lower_bound - 1] == self.character) != (password[self.bounds.upper_bound - 1] == self.character)
        except IndexError:
            return False


@dataclasses.dataclass
class Entry:
    password: str
    requirement: Requirement

    def check_valid(self) -> bool:
        return self.requirement.check_satisfy(self.password)

    def check_strict_valid(self) -> bool:
        return self.requirement.check_strict_satisfy(self.password)


def password_philosophy(input_data_filepath: str) -> int:
    entries = parse_input(input_data_filepath)
    return sum(map(lambda entry: 1 if entry.check_valid() else 0, entries))


def password_philosophy_strict(input_data_filepath: str) -> int:
    entries = parse_input(input_data_filepath)
    return sum(map(lambda entry: 1 if entry.check_strict_valid() else 0, entries))


def parse_input(input_data_filepath: str) -> List[Entry]:
    with open(input_data_filepath) as file:
        return list(map(parse_entry, file.read().split("\n")))


def parse_entry(entry: str) -> Entry:
    (requirement_str, password_str) = entry.split(":")

    (interval_str, character_str) = requirement_str.split(" ")
    (lower_bound_str, upper_bound_str) = interval_str.split("-")

    password = password_str.strip()

    return Entry(password=password, requirement=Requirement(bounds=Interval(int(lower_bound_str), int(upper_bound_str)),
                                                            character=character_str))

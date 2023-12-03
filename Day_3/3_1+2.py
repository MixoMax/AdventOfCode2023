#Advent of Code 2023 Day 3 Part 1 + 2

import os
from string import digits
from typing import Generator
from math import prod

os.chdir(os.path.dirname(os.path.abspath(__file__)))
 
digits = set(digits)
 

 
def parse_data(data: str) -> tuple[set[complex], list[tuple[int, list[complex]]]]:
    symbols = set()
    number_output: list[tuple[int, list[complex]]] = []
    for y, row in enumerate(data.splitlines()):
        num = ""
        num_locs = list()
        for x, val in enumerate(row):
            if val in digits:
                num += val
                num_locs.append(complex(x, y))
            elif num:
                number_output.append((int(num), num_locs.copy()))
                num = ""
                num_locs = list()
            if val not in digits and val != ".":
                symbols.add(complex(x, y))
        if num:
            number_output.append((int(num), num_locs.copy()))
    return symbols, number_output
 
 
ADJACENT_DIRECTIONS = (
    complex(-1, -1),
    complex(-1, 0),
    complex(-1, 1),
    complex(0, -1),
    complex(0, 1),
    complex(1, -1),
    complex(1, 0),
    complex(1, 1),
)
 
 
def adjacent_locations(
    location: complex, adjacent_directions=ADJACENT_DIRECTIONS
) -> Generator[complex, None, None]:
    for adjacent in adjacent_directions:
        yield location + adjacent
 
 
def has_adjacent_symbol(locations: list[complex], symbols: set[complex]) -> bool:
    for location in locations:
        for adj in adjacent_locations(location):
            if adj in symbols:
                return True
    return False
 
 
def part_a(input_data: str) -> int:
    total = 0
    symbols, numbers = parse_data(input_data)
    for number, positions in numbers:
        if has_adjacent_symbol(positions, symbols):
            total += number
    return total
 
 
def part_b(input_data: str) -> int:
    gear_ratio = 0
    symbols, numbers = parse_data(input_data)
    for symbol in symbols:
        adjacent_numbers = []
        adj_locs = set(adjacent_locations(symbol))
        for num, positions in numbers:
            if set(positions).intersection(adj_locs):
                adjacent_numbers.append(num)
        if len(adjacent_numbers) == 2:
            gear_ratio += prod(adjacent_numbers)
    return gear_ratio


with open("./data.txt", "r") as f:
    input_str = f.read()

print("part a:", part_a(input_str))
print("part b:", part_b(input_str))
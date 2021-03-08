#!/usr/bin/python3
"""
Solution for the first part for the day 9
"""

from advent_of_code.year2020.day09.common import (
    read_file,
    get_previous_numbers,
    get_sums,
)


def is_valid(preamble: list = None, number: int = 0) -> bool:
    """
    Check if provided number exists in the given list
    """
    return number in preamble


def solve_the_task(filename="", preamble_size: int = 25) -> int:
    """
    Complete solution for the provided task
    """
    numbers = read_file(filename)
    init_pos = preamble_size
    while init_pos < len(numbers):
        preamble = get_previous_numbers(
            data=numbers, preamble=preamble_size, pos=init_pos
        )
        preamble_combinations = get_sums(preamble)
        if not is_valid(preamble_combinations, numbers[init_pos]):
            return numbers[init_pos]
        init_pos += 1
    return -1


if __name__ == "__main__":
    res = solve_the_task(filename="input.txt")
    print(f"First incorrect value is: {res}")

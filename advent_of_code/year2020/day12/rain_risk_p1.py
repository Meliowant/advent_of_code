#!/usr/bin/env python3
"""
Solution for the first part of the task on day 12
"""

from advent_of_code.year2020.day12.common import read_instructions, Ferry


def solve_the_task(filename: str = None) -> int:
    """
    Main logic for the solution
    """
    instructions = read_instructions(filename)
    my_ferry = Ferry()
    for instruction in instructions:
        my_ferry.execute(instruction)
    man_dist = my_ferry.manhattan_distance()
    print(f"Manhattan distance for ferry in the final point is '{man_dist}'")
    return man_dist


if __name__ == "__main__":
    solve_the_task(filename="aoc_input.txt")

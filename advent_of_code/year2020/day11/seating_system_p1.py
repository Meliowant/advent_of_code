#!/bin/env python3
"""
Solution for the first part of the task on day 11
"""

from advent_of_code.year2020.day11.common import (
    read_seats, verify_seat, map_to_str
)


def solve_the_task(filename: str = None):
    """
    Main function to solve the first part of the task on day 11
    """
    seats_map = read_seats(filename)
    has_changed = True
    loops = 0
    while has_changed:
        print(f"Staring loop '{loops}'")
        loops += 1
        has_changed = False
        new_seats_map = []
        for row_idx, row in enumerate(seats_map):
            new_seats_map.append([])
            for col_idx, _ in enumerate(row):
                updated_seat = verify_seat(seats_map, (row_idx, col_idx))
                new_seats_map[row_idx].append(updated_seat)
                if not has_changed and \
                        updated_seat != seats_map[row_idx][col_idx]:
                    has_changed = True
        seats_map = new_seats_map

    seats = map_to_str(seats_map).count("#")
    print(f"'{seats}' seats are occupied after all")
    return seats


if __name__ == "__main__":
    solve_the_task(filename="aoc_input.txt")

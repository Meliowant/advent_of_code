#!/usr/bin/env python3
"""
Solution for the second part for task on day 11
"""

from advent_of_code.year2020.day11.common import (
    read_seats,
    toggle_seat,
    map_to_str,
)


def seats_in_direction(
    seats_map: list = None, position: tuple = None, direction: tuple = None
) -> int:
    """
    Get amount of seats in requested direction.

    Keywords:
        seats_map - a list of lists with the seats;
        position - a tuple that contains the initial position;
        direction - a tuple with direction where the seats will be checked
            first argument - go to the west (if negative) or the east
                (if positive)
            second argument - go to the north (if negative) or south
                (if positive)

    Returns:
        an integer value of visible seats
    """
    row, col = position
    row_shift, col_shift = direction
    min_col = 0
    min_row = 0
    max_row = len(seats_map) - 1
    max_col = len(seats_map[0]) - 1
    col += col_shift
    row += row_shift
    while min_row <= row <= max_row and min_col <= col <= max_col:
        if seats_map[row][col] == "#":
            return 1
        if seats_map[row][col] == "L":
            return 0
        col += col_shift
        row += row_shift
    return 0


def get_occupied_seats(seats_map: list = None, position: tuple = None) -> int:
    """
    Calculate amount of occupied seats in the visible range for the given
        position.

    Keywords:
        seats_map - a list of lists with the seats configuration.
        position - a tuple (row, column) for initial seat.

    Returns:
        Amount of occupied seats among the nearest visible seats.
    """
    north_dir = seats_in_direction(seats_map, position, (-1, 0))
    ne_dir = seats_in_direction(seats_map, position, (-1, 1))
    east_dir = seats_in_direction(seats_map, position, (0, 1))
    se_dir = seats_in_direction(seats_map, position, (1, 1))
    south_dir = seats_in_direction(seats_map, position, (1, 0))
    sw_dir = seats_in_direction(seats_map, position, (1, -1))
    west_dir = seats_in_direction(seats_map, position, (0, -1))
    nw_dir = seats_in_direction(seats_map, position, (-1, -1))

    return sum(
        [
            north_dir,
            ne_dir,
            east_dir,
            se_dir,
            south_dir,
            sw_dir,
            west_dir,
            nw_dir,
        ]
    )


def seat_must_be_toggled(seat: str = None, occupied_seats: int = None) -> bool:
    """
    Check if the seat must be switched from free to occupied and vice-versa.
    """
    if seat == "L" and occupied_seats == 0:
        return True
    if seat == "#" and occupied_seats > 4:
        return True
    return False


def verify_seat(seats: list = None, seat: tuple = None) -> str:
    """
    Get the seat's new state after examining all visible seats
    """
    occupied_seats = get_occupied_seats(seats, seat)
    seat_row, seat_col = seat
    seat_state = seats[seat_row][seat_col]
    if seat_must_be_toggled(seat_state, occupied_seats):
        seat_state = toggle_seat(seat_state)
    return seat_state


def solve_the_task(filename: str) -> int:
    """
    Solution for the second task on day 11
    """
    seats_map = read_seats(filename)
    has_changed = True
    loops = 0
    while has_changed:
        loops += 1
        print(f"Working on '{loops}' map.")
        has_changed = False
        new_seats_map = []
        for row_idx, row in enumerate(seats_map):
            new_seats_map.append([])
            for col_idx, seat in enumerate(row):
                updated_seat = (
                    seat
                    if seat == "."
                    else verify_seat(seats_map, (row_idx, col_idx))
                )
                new_seats_map[row_idx].append(updated_seat)
                if (
                    not has_changed
                    and updated_seat != seats_map[row_idx][col_idx]
                ):
                    has_changed = True
        seats_map = new_seats_map

    seats = map_to_str(seats_map).count("#")
    print(f"'{seats}' seats are occupied after all")
    return seats


if __name__ == "__main__":
    solve_the_task(filename="aoc_input.txt")

#!/bin/env python3
"""
A set of functions that will be used in both part of solution for day 11.
"""


from pathlib import Path


def read_seats(filename: Path = None) -> list:
    """
    Read a content of file and create a list of lists with the seats.
    The seats are marked as:
        . - floor;
        L - empty seat;
        # - occupied seat.

    Expected keywords:
        filename - file with the seats.
    """
    if not isinstance(filename, Path):
        filename = Path(filename)

    seats = []

    with filename.open() as _:
        line = _.readline()
        while line:
            seats.append(list(x for x in line.strip()))
            line = _.readline()

    return seats


def is_seat(seat: str = None) -> bool:
    """
    Check if provided seat is really seat.

    Keyword arguments:
        seat - seat label (str).

    Returns:
        True - if seat is either 'L' or '#';
        False - otherwise
    """
    return seat in ["L", "#"] if seat else False


def toggle_seat(seat: str = None) -> str:
    """
    Toggles seat from free to occupied and vice versa.


    Keyword arguments:
        seat - seat label (str)

    Returns:
        "#" - if seat value is "L",
        "L" - if seat's value is "#",
        raises ValueError if seat has other value
    """
    seats = ["L", "#"]
    try:
        seats.remove(seat)
    except ValueError as err:
        raise ValueError(f"Unknown seat value: {seat}") from err
    return seats[0]


def get_occupied_seats(seats_map: list = None, position: tuple = None) -> int:
    """
    Calculate amount of occupied adjacent seats (up, down, left, right, diags)

    Expected keywords:
        seats_map - a complete set of seats (list of lists)
        position - a tuple with the position of the seat, for which amount of
          adjacent seats will be calculated

    Returns:
        On success - amount of adjacent occupied seats for given seat;
        On failure - raises ValueError
    """
    adjacent_seats = []
    row, col = position
    rows = len(seats_map)
    cols = len(seats_map[0])
    str_map = map_to_str(seats_map)

    for s_row, s_col in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        new_row = row + s_row
        new_col = col + s_col

        if 0 <= new_row < rows and 0 <= new_col < cols:
            seat_pos = new_row * cols + new_col
            exp_seat = str_map[seat_pos]
            adjacent_seats.append(exp_seat if is_seat(exp_seat) else None)

    adjacent_seats_amount = adjacent_seats.count("#")

    return adjacent_seats_amount


def map_to_str(seats_map: list = None) -> str:
    """
    Convert a map into a string
    """
    return "".join(["".join(x) for x in seats_map])


def verify_seat(seats: list = None, seat: tuple = None) -> str:
    """
    Apply occupation rules for a seat
    """
    seat_row, seat_col = seat
    seat_state = seats[seat_row][seat_col]
    occupied_seats = get_occupied_seats(seats, seat)
    if seat_must_be_toggled(seat_state, occupied_seats):
        seat_state = toggle_seat(seat_state)

    return seat_state


def seat_must_be_toggled(seat: str = None, occupied_seats: int = None) -> bool:
    """
    Helper to hide toggling logic
    """
    if seat == "L" and occupied_seats == 0:
        return True

    if seat == "#" and occupied_seats > 3:
        return True

    return False

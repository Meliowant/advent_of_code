#!/usr/bin/env python3
"""
Test suite for the second solution on day 11.
"""

import pytest
from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day11.seating_system_p2 import (
    get_occupied_seats,
    seats_in_direction,
    verify_seat,
    solve_the_task,
    seat_must_be_toggled,
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "All neighboring seats around are occupied",
            "seats_map": [["#", "#", "#"], ["#", "L", "#"], ["#", "#", "#"]],
            "position": (1, 1),
            "expected_seats": 8,
        },
        {
            "test_name": "All distant seats around are occupied",
            "seats_map": [
                ["#", "#", "#", "#", "#"],
                ["#", "L", "L", "L", "#"],
                ["#", "L", "L", "L", "#"],
                ["#", "L", "L", "L", "#"],
                ["#", "#", "#", "#", "#"],
            ],
            "position": (2, 2),
            "expected_seats": 0,
        },
        {
            "test_name": (
                "All distant visible seats are occupied, non-visible free"
            ),
            "seats_map": [
                ["#", "L", "#", "L", "#"],
                ["L", ".", ".", ".", "L"],
                ["#", ".", "L", ".", "#"],
                ["L", ".", ".", ".", "L"],
                ["#", "L", "#", "L", "#"],
            ],
            "position": (2, 2),
            "expected_seats": 8,
        },
        {
            "test_name": "Top-right corner. All distant seats are occupied",
            "seats_map": [["L", ".", "#"], [".", ".", "L"], ["#", "L", "#"]],
            "position": (0, 0),
            "expected_seats": 3,
        },
        {
            "test_name": "All seats around are occupied",
            "seats_map": [["#", "#", "#"], ["#", "L", "#"], ["#", "#", "#"]],
            "position": (1, 1),
            "expected_seats": 8,
        },
        {
            "test_name": "AOC Reference example 1",
            "seats_map": [
                [".", ".", ".", ".", ".", ".", ".", "#", "."],
                [".", ".", ".", "#", ".", ".", ".", ".", "."],
                [".", "#", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", "#", "L", ".", ".", ".", ".", "#"],
                [".", ".", ".", ".", "#", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                ["#", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "#", ".", ".", ".", ".", "."],
            ],
            "position": (4, 3),
            "expected_seats": 8,
        },
        {
            "test_name": "AOC Reference example 2",
            "seats_map": [
                [
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                ],
                [
                    ".",
                    "L",
                    ".",
                    "L",
                    ".",
                    "#",
                    ".",
                    "#",
                    ".",
                    "#",
                    ".",
                    "#",
                    ".",
                ],
                [
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                    ".",
                ],
            ],
            "position": (1, 1),
            "expected_seats": 0,
        },
        {
            "test_name": "AOC Reference example 3",
            "seats_map": [
                [".", "#", "#", ".", "#", "#", "."],
                ["#", ".", "#", ".", "#", ".", "#"],
                ["#", "#", ".", ".", ".", "#", "#"],
                [".", ".", ".", "L", ".", ".", "."],
                ["#", "#", ".", ".", ".", "#", "#"],
                ["#", ".", "#", ".", "#", ".", "#"],
                [".", "#", "#", ".", "#", "#", "."],
            ],
            "position": (3, 3),
            "expected_seats": 0,
        },
    ],
    ids=format_name,
)
def test_get_occupied_seats(opts):
    """
    Test updated method for calculating adjacent seats in visible directions.
    """
    got_seats = get_occupied_seats(
        seats_map=opts["seats_map"], position=opts["position"]
    )
    assert got_seats == opts["expected_seats"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No seats in direction",
            "map": [["L", "L", "L"], ["L", "L", "L"], ["L", "L", "L"]],
            "position": (1, 1),
            "direction": (1, 0),
            "expected_seats": 0,
        },
        {
            "test_name": "One seat on west",
            "map": [["L", "L", "L"], ["L", "L", "#"], ["L", "L", "L"]],
            "position": (1, 1),
            "direction": (0, 1),
            "expected_seats": 1,
        },
        {
            "test_name": "One seat on west, in second line",
            "map": [["L", "L", "L", "L"], ["L", ".", ".", "#"]],
            "position": (1, 1),
            "direction": (0, 1),
            "expected_seats": 1,
        },
        {
            "test_name": "One seat on west, in first line, second is hidden",
            "map": [["L", "L", "L", "L"], ["L", "L", "#", "#"]],
            "position": (1, 1),
            "direction": (0, 1),
            "expected_seats": 1,
        },
        {
            "test_name": "Seat is top-left, go right",
            "map": [["L", ".", "L", "#"], ["#", "L", "#", "#"]],
            "position": (0, 0),
            "direction": (0, 1),
            "expected_seats": 0,
        },
        {
            "test_name": "Seat us top-left, go top, no seats",
            "map": [["L", "L", "L", "L"], ["L", "L", "#", "#"]],
            "position": (0, 0),
            "direction": (-1, 0),
            "expected_seats": 0,
        },
        {
            "test_name": "Seat is top-left, do bottom, 1 seat visible",
            "map": [["L", "L", "L", "L"], ["#", "L", "#", "#"]],
            "position": (0, 0),
            "direction": (1, 0),
            "expected_seats": 1,
        },
        {
            "test_name": "Seat is top-left, go left, no seats are visible",
            "map": [["L", "L", "L", "L"], ["L", "L", "#", "#"]],
            "position": (0, 0),
            "direction": (0, -1),
            "expected_seats": 0,
        },
    ],
    ids=format_name,
)
def test_seats_in_direction(opts):
    """
    Check if seats_in_direction_works_correctly
    """
    got_seats = seats_in_direction(
        seats_map=opts["map"],
        position=opts["position"],
        direction=opts["direction"],
    )
    assert got_seats == opts["expected_seats"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Seat is free, no seats around",
            "seats": [["L", "L", "L"], ["L", "L", "L"], ["L", "L", "L"]],
            "seat": (1, 1),
            "expected_seat": "#",
        },
        {
            "test_name": "Seat is free, 1 seat around",
            "seats": [["L", "L", "L"], ["L", "L", "#"], ["L", "L", "L"]],
            "seat": (1, 1),
            "expected_seat": "L",
        },
        {
            "test_name": "Seat is free, 4 seats around",
            "seats": [
                ["L", "#", "L"],
                ["L", "L", "L"],
                ["#", "L", "#"],
                ["L", "L", "L"],
                ["L", "#", "L"],
            ],
            "seat": (2, 1),
            "expected_seat": "L",
        },
        {
            "test_name": "Seat is occupied, 3 seats around",
            "seats": [
                ["L", "L", "#", "L", "L"],
                ["L", "L", "L", "L", "L"],
                ["L", "L", "#", "L", "L"],
                ["L", "L", "L", "L", "L"],
                ["L", "L", "#", "L", "#"],
            ],
            "seat": (2, 2),
            "expected_seat": "#",
        },
        {
            "test_name": "Seat is occupied, 4 seats around",
            "seats": [
                ["#", "L", "#", "L", "L"],
                ["L", "L", "L", "L", "L"],
                ["L", "L", "#", "L", "L"],
                ["L", "L", "L", "L", "L"],
                ["L", "L", "#", "L", "#"],
            ],
            "seat": (2, 2),
            "expected_seat": "#",
        },
        {
            "test_name": "Seat is occupied, 5 seats around",
            "seats": [
                ["#", "L", "#", "L", "#"],
                ["L", ".", ".", ".", "L"],
                ["L", ".", "#", ".", "L"],
                ["L", ".", ".", ".", "L"],
                ["L", "L", "#", "L", "#"],
            ],
            "seat": (2, 2),
            "expected_seat": "L",
        },
    ],
    ids=format_name,
)
def test_verify_seat(opts):
    """
    Check verify_seat functionality
    """
    got_seat = verify_seat(opts["seats"], opts["seat"])
    assert got_seat == opts["expected_seat"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Seat is free and toggles to occupied",
            "seat": "L",
            "occupied_seats": 0,
            "expected_toggled_value": True,
        },
        {
            "test_name": "Seat is free, 1 visible seat, seat remains free",
            "seat": "L",
            "occupied_seats": 1,
            "expected_toggled_value": False,
        },
        {
            "test_name": (
                "Seat is occupied, 4 visible seats, seat remains occupied"
            ),
            "seat": "#",
            "occupied_seats": 4,
            "expected_toggled_value": False,
        },
        {
            "test_name": (
                "Seat is occupied, 5 visible seats, seat becomes free"
            ),
            "seat": "#",
            "occupied_seats": 5,
            "expected_toggled_value": True,
        },
        {
            "test_name": "Seat if free and toggles to occupied",
            "seat": "L",
            "occupied_seats": 0,
            "expected_toggled_value": True,
        },
    ],
    ids=format_name,
)
def test_seat_must_be_toggled(opts):
    """
    Check seat_must_be_toggled functionality
    """
    got_toggled_value = seat_must_be_toggled(
        opts["seat"], opts["occupied_seats"]
    )
    assert got_toggled_value == opts["expected_toggled_value"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "AOC reference file",
            "filename": "aoc_example_1.txt",
            "expected_result": 26,
        }
    ],
    ids=format_name,
)
def test_solve_the_task(opts):
    """
    Check solve_the_task functionality
    """
    got_result = solve_the_task(opts["filename"])
    assert got_result == opts["expected_result"]

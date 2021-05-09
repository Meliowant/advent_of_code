#!/bin/env python3
"""
Test suite for common functions that will be used in the solution for this day
"""

import pytest
from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day11.common import (
    read_seats,
    is_seat,
    toggle_seat,
    get_occupied_seats,
    map_to_str,
    verify_seat,
    seat_must_be_toggled,
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Single floor seat",
            "input": "one_floor.txt",
            "expected_seats": [["."]],
        },
        {
            "test_name": "Single free seat",
            "input": "one_empty_seat.txt",
            "expected_seats": [["L"]],
        },
        {
            "test_name": "Single occupied seat",
            "input": "one_occupied_seat.txt",
            "expected_seats": [["#"]],
        },
        {
            "test_name": "AOC's first example",
            "input": "aoc_example_1.txt",
            "expected_seats": [
                ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
                ["L", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
                ["L", ".", "L", ".", "L", ".", ".", "L", ".", "."],
                ["L", "L", "L", "L", ".", "L", "L", ".", "L", "L"],
                ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
                ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
                [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
                ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
                ["L", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
                ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
            ],
        },
    ],
    ids=format_name,
)
def test_read_seats(opts):
    """
    Test if file with the sets map was read correctly
    """
    got_seats = read_seats(opts["input"])
    assert got_seats == opts["expected_seats"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Value is free seat",
            "value": "L",
            "expected": True,
        },
        {
            "test_name": "Value is occupied seat",
            "value": "#",
            "expected": True,
        },
        {
            "test_name": "Value is floor",
            "value": ".",
            "expected": False,
        },
        {
            "test_name": "Value is empty",
            "value": "",
            "expected": False,
        },
        {
            "test_name": "Value is missing",
            "value": None,
            "expected": False,
        },
    ],
    ids=format_name,
)
def test_is_seat(opts):
    """
    Check seat detection
    """
    got_is_seat = is_seat(opts["value"])
    assert got_is_seat == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {"test_name": "Seat is free", "value": "L", "expected": "#"},
        {"test_name": "Seat is occupied", "value": "#", "expected": "L"},
        pytest.param(
            {"test_name": "Seat is not seat", "value": ".", "expected": ""},
            marks=pytest.mark.xfail(raises=ValueError),
        ),
    ],
    ids=format_name,
)
def test_toggle_seat(opts):
    """
    Check if free seat becomes occupied from free, and vice versa
    """
    toggled_seat = toggle_seat(opts["value"])
    assert toggled_seat == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "top-left",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (0, 0),
            "expected_seats": 3,
        },
        {
            "test_name": "top-center",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (0, 1),
            "expected_seats": 5,
        },
        {
            "test_name": "top-right",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (0, 2),
            "expected_seats": 3,
        },
        {
            "test_name": "middle-left",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (1, 0),
            "expected_seats": 5,
        },
        {
            "test_name": "middle-center",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (1, 1),
            "expected_seats": 8,
        },
        {
            "test_name": "middle-right",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (1, 2),
            "expected_seats": 5,
        },
        {
            "test_name": "bottom-left",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (2, 0),
            "expected_seats": 3,
        },
        {
            "test_name": "bottom-middle",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (2, 1),
            "expected_seats": 5,
        },
        {
            "test_name": "bottom-right",
            "seats_map": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
            "position": (2, 2),
            "expected_seats": 3,
        },
        {
            "test_name": "bottom-right. Sole around free",
            "seats_map": [["#", "#", "#"], ["#", "L", "L"], ["#", "L", "#"]],
            "position": (2, 2),
            "expected_seats": 0,
        },
        {
            "test_name": "bottom-right. Sole arounf floor",
            "seats_map": [["#", "#", "#"], ["#", ".", "."], ["#", ".", "#"]],
            "position": (2, 2),
            "expected_seats": 0,
        },
    ],
    ids=format_name,
)
def test_get_occupied_seats(opts):
    """
    Test calculation for amount of occupied adjacent seats (up, down, left,
    right and diagonal)
    """
    seats = get_occupied_seats(opts["seats_map"], position=opts["position"])
    assert seats == opts["expected_seats"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Single entry",
            "map": [["L"]],
            "expected": "L",
        },
        {
            "test_name": "Multiple entries",
            "map": [["L", "L"]],
            "expected": "LL",
        },
        {
            "test_name": "Multiple items in multiple entries",
            "map": [["L", "L"], ["#", "L"]],
            "expected": "LL#L",
        },
    ],
    ids=format_name,
)
def test_map_to_str(opts):
    """
    Test converting map to string
    """
    got_map = map_to_str(opts["map"])
    assert got_map == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Seat must be toggled from free to occupied",
            "seat": "L",
            "occupied_seats": 0,
            "exp_toggled": True,
        },
        {
            "test_name": "Seat remains free. One adjacent occupied",
            "seat": "L",
            "occupied_seats": 1,
            "exp_toggled": False,
        },
        {
            "test_name": "Seat remains occupied, not enough occupied",
            "seat": "#",
            "occupied_seats": 3,
            "exp_toggled": False,
        },
        {
            "test_name": "Seat must be toggled from occupied to free",
            "seat": "#",
            "occupied_seats": 4,
            "exp_toggled": True,
        },
    ],
    ids=format_name,
)
def test_seat_must_be_toggled(opts):
    """
    Check if seat_must be toggled
    """
    got_toggled = seat_must_be_toggled(opts["seat"], opts["occupied_seats"])
    assert got_toggled is opts["exp_toggled"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Seat was free and becomes occupied",
            "seats": [["L", "L", "L"], ["L", "L", "L"], ["L", "L", "L"]],
            "seat": (1, 1),
            "expected_seat": "#",
        },
        {
            "test_name": "Seat was occupied and becomes free",
            "seats": [["L", "L", "L"], ["#", "#", "#"], ["#", "#", "L"]],
            "seat": (1, 1),
            "expected_seat": "L",
        },
        {
            "test_name": "Seat was and remains free (not enough occupied)",
            "seats": [["#", "#", "#"], ["L", "L", "L"], ["L", "L", "L"]],
            "seat": (1, 1),
            "expected_seat": "L",
        },
        {
            "test_name": "Seat was and remains occupied",
            "seats": [["#", "#", "#"], ["L", "#", "L"], ["L", "L", "L"]],
            "seat": (1, 1),
            "expected_seat": "#",
        },
    ],
    ids=format_name,
)
def test_verify_seat(opts):
    """
    Check if seat will be updated
    """
    got_seat = verify_seat(seats=opts["seats"], seat=opts["seat"])
    assert got_seat == opts["expected_seat"]

#!/bin/env python3
"""
Suite for testing first part of solution for seating system.
"""

import pytest
from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day11.seating_system_p1 import solve_the_task


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "AOC example",
            "filename": "aoc_example_1.txt",
            "exp_seats": 37
        }
    ],
    ids=format_name
)
def test_solve_the_task(opts):
    """
    Check the sole method that returns amount of occupied seats for the given
    seats map
    """
    got_seats = solve_the_task(opts["filename"])
    assert got_seats == opts["exp_seats"]

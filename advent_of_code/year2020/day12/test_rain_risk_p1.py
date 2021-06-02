#!/usr/bin/env python3
"""
Test solution for the first part of the task on day 12
"""

import pytest
from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day12.rain_risk_p1 import solve_the_task


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "AOC reference example",
            "filename": "aoc_example_1.txt",
            "expected_distance": 25,
        }
    ],
    ids=format_name,
)
def test_solve_the_task(opts):
    """
    Check solution's logic
    """
    got_distance = solve_the_task(opts["filename"])
    assert got_distance == opts["expected_distance"]

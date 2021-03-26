"""
Test suite for solution of the first part on the day 10
"""
import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day10.adapter_array_p1 import (
    get_adapters_and_stats,
    solve_the_task,
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Check first example from Advent of Code",
            "file_name": "test_input_aoc_example1.txt",
            "expected_adapters": [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19],
            "expected_stats": {"1": 7, "3": 5},
        },
    ],
    ids=format_name,
)
def test_get_adapters_and_stats(opts):
    """
    Check the whole solution's logic
    """
    adapters, stats = get_adapters_and_stats(opts["file_name"])
    assert adapters == opts["expected_adapters"]
    assert stats == opts["expected_stats"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Check first example from Advent of Code",
            "file_name": "test_input_aoc_example1.txt",
            "expected_mult": 35,
        },
        {
            "test_name": "Check second example from Advent of Code",
            "file_name": "test_input_aoc_example2.txt",
            "expected_mult": 220,
        },
    ],
    ids=format_name,
)
def test_solve_the_task(opts):
    """
    Check solve_the_task main function
    """
    got = solve_the_task(opts["file_name"])
    assert got == opts["expected_mult"]

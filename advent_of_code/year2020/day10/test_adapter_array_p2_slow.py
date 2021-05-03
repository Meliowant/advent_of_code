"""
Set of tests for the second part of the day 10th task.
"""
import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day10.adapter_array_p2_slow import (
    list_all_combinations,
    solve_the_task,
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "One combination, with two elements",
            "adapters": [0],
            "input_joltage": 1,
            "expected_combinations": [[0, 1]],
        },
        {
            "test_name": "Two combinations",
            "adapters": [0, 1],
            "input_joltage": 2,
            "expected_combinations": [[0, 1, 2], [0, 2]],
        },
        {
            "test_name": "No combinations",
            "adapters": [0, 1],
            "input_joltage": 5,
            "expected_combinations": [],
        },
    ],
    ids=format_name,
)
def test_list_all_combinations(opts):
    """
    Check if we list correctly all possible combinations
    """
    got_combinations = sorted(
        list_all_combinations(
            adapters=opts["adapters"], target_joltage=opts["input_joltage"]
        )
    )
    assert got_combinations == sorted(opts["expected_combinations"])


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "First AOC reference example",
            "file_name": "test_input_aoc_example1.txt",
            "expected_combinations": 8,
        },
        {
            "test_name": "Second AOC reference example",
            "file_name": "test_input_aoc_example2.txt",
            "expected_combinations": 19208,
        },
    ],
    ids=format_name,
)
def test_solve_the_task(opts):
    """
    Test entrance logic for the second solution on day 10.
    """
    calculated_combinations = solve_the_task(opts["file_name"])
    assert calculated_combinations == opts["expected_combinations"]

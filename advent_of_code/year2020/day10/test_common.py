"""
Set of common calls to solve tasks for day 10
"""

import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day10.common import (
    read_data,
    get_devices_joltage,
    get_tried_out_adapters,
    pick_adapter,
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Read empty file",
            "filename": "input_empty.txt",
            "expected": [],
        },
        {
            "test_name": "Read non-existing file",
            "filename": "non-existing-file.txt",
            "expected": [],
        },
        {
            "test_name": "Read file with numbers only",
            "filename": "input_numbers.txt",
            "expected": [1, 2, 3, 4, 5],
        },
        {
            "test_name": "Read file with letters only",
            "filename": "input_letters.txt",
            "expected": [],
        },
    ],
    ids=format_name,
)
def test_read_data(opts):
    """
    Check if data was read correctly from the file
    """
    got_data = read_data(file_name=opts["filename"])
    assert got_data == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "List of adapters is missing",
            "adapters": None,
            "expected": 3,
        },
        {
            "test_name": "List of adapters is empty",
            "adapters": [],
            "expected": 3,
        },
        {
            "test_name": "List of adapters is OK",
            "adapters": [1, 2, 3],
            "expected": 6,
        },
    ],
    ids=format_name,
)
def test_get_devices_joltage(opts):
    """
    Detect device's joltage
    """
    got_devices_joltage = get_devices_joltage(adapters=opts["adapters"])
    assert got_devices_joltage == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Empty list of adapters",
            "adapters": [],
            "init_joltage": 5,
            "expected": ([], []),
        },
        {
            "test_name": "No supported adapters",
            "adapters": [1, 2, 3],
            "init_joltage": 8,
            "expected": ([], []),
        },
        {
            "test_name": "Joltage is zero, has one supported adapter",
            "adapters": [1, 4, 5, 6],
            "init_joltage": 0,
            "expected": ([1], [4, 5, 6]),
        },
        {
            "test_name": "One supported adapter, joltage is not counted",
            "adapters": [3, 6, 2, 9, 7, 10],
            "init_joltage": 2,
            "expected": ([3], [6, 9, 7, 10]),
        },
        {
            "test_name": "Two supported adapters, joltage is not counted",
            "adapters": [3, 6, 2, 9, 5, 10],
            "init_joltage": 1,
            "expected": ([3, 2], [6, 9, 5, 10]),
        },
    ],
    ids=format_name,
)
def test_get_tried_out_adapters(opts):
    """
    Check get_tried_out adapters.
    """
    got_adapters = get_tried_out_adapters(
        adapters=opts["adapters"], init_joltage=opts["init_joltage"]
    )
    assert got_adapters == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No suitable adapters",
            "adapters": [1, 2, 3],
            "input_joltage": 5,
            "expected": (None, None),
        },
    ],
    ids=format_name,
)
def test_pick_adapter(opts):
    """
    Test pick_adapter functionality
    """
    # TODO Add cases for checking pick_adapter
    got_adapter = pick_adapter(
        adapters=opts["adapters"], input_joltage=opts["input_joltage"]
    )
    assert got_adapter == opts["expected"]

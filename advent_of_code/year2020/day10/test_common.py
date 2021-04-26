"""
Set of common calls to solve tasks for day 10
 """

import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day10.common import (
    read_data,
    get_devices_joltage,
    get_compatible_adapter,
    get_compatible_adapters,
    get_joltage_diff,
    JoltageStats,
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
            "expected": (-1, []),
        },
        {
            "test_name": "No supported adapters",
            "adapters": [1, 2, 3],
            "init_joltage": 8,
            "expected": (-1, []),
        },
        {
            "test_name": "Joltage is zero, has one supported adapter",
            "adapters": [1, 4, 5, 6],
            "init_joltage": 0,
            "expected": (1, [4, 5, 6]),
        },
        {
            "test_name": "One supported adapter, joltage is not counted",
            "adapters": [3, 6, 2, 9, 7, 10],
            "init_joltage": 2,
            "expected": (3, [6, 7, 9, 10]),
        },
        {
            "test_name": "One supported adapter, joltage is not counted",
            "adapters": [13, 16, 12, 19, 17, 10, 5],
            "init_joltage": 2,
            "expected": (5, [10, 12, 13, 16, 17, 19]),
        },
        {
            "test_name": "Two supported adapters, joltage is not counted",
            "adapters": [3, 6, 2, 9, 5, 10],
            "init_joltage": 1,
            "expected": (2, [3, 5, 6, 9, 10]),
        },
        {
            "test_name": "Two supported adapters, joltage in reversed order",
            "adapters": [10, 5, 9, 3, 6, 2],
            "init_joltage": 1,
            "expected": (2, [3, 5, 6, 9, 10]),
        },
    ],
    ids=format_name,
)
def test_get_compatible_adapter(opts):
    """
    Check get_compatible_adapter
    """
    got_adapters = get_compatible_adapter(
        adapters=opts["adapters"], init_joltage=opts["init_joltage"]
    )
    assert got_adapters == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Ascending list",
            "adapters": [2, 3, 4, 5, 6, 7],
            "joltage": 1,
            "supported_list": [2, 3, 4],
        },
        {
            "test_name": "Descending list",
            "adapters": [7, 6, 5, 4, 3, 2],
            "joltage": 1,
            "supported_list": [2, 3, 4],
        },
        {
            "test_name": "List with ignored values",
            "adapters": [1, 2, 3, 4, 5, 6, 7],
            "joltage": 1,
            "supported_list": [2, 3, 4],
        },
        {
            "test_name": "Empty list",
            "adapters": [],
            "joltage": 1,
            "supported_list": [],
        },
        {
            "test_name": "Ascending list",
            "adapters": [2, 3, 4, 5, 6, 7],
            "joltage": 1,
            "supported_list": [2, 3, 4],
        },
    ],
    ids=format_name,
)
def test_get_compatible_adapters(opts):
    """
    Check get_compatible_adapters.
    """
    supported = get_compatible_adapters(
        opts["adapters"], input_joltage=opts["joltage"]
    )
    assert supported == opts["supported_list"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "In and out diff by 1",
            "in": 1,
            "out": 2,
            "expected": 1,
        },
        {
            "test_name": "In and out diff by 3",
            "in": 1,
            "out": 4,
            "expected": 3,
        },
        {
            "test_name": "In joltage is missing",
            "in": None,
            "out": 4,
            "expected": -1,
        },
        {
            "test_name": "Out joltage is missing",
            "in": 1,
            "out": None,
            "expected": -1,
        },
    ],
    ids=format_name,
)
def test_get_joltage_diff(opts):
    """
    Test get_joltage_diff
    """
    got = get_joltage_diff(in_joltage=opts["in"], out_joltage=opts["out"])
    assert got == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No items collected",
            "in": [],
            "expected_dict": {},
        },
        {
            "test_name": "Single item collected",
            "in": [1],
            "expected_dict": {"1": 1},
        },
        {
            "test_name": "Two items with same joltage collected",
            "in": [1, 1],
            "expected_dict": {"1": 2},
        },
        {
            "test_name": "Two items with different joltage collected",
            "in": [1, 3],
            "expected_dict": {"1": 1, "3": 1},
        },
    ],
    ids=format_name,
)
def test_joltage_stats(opts):
    """
    Test collection and reporting for JoltageStats storage
    """
    stats = JoltageStats()
    for itm in opts["in"]:
        stats.collect(itm)
    got = stats.report()
    assert got == opts["expected_dict"]

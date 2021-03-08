"""
Test suite for common functions, that are used for solution on day 9
"""
import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day09.common import (
    read_file,
    get_previous_numbers,
    get_sums,
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "File exists",
            "filename": "test_expected_input.txt",
            "exp_data": [1, 2, 3],
        },
        {
            "test_name": "File is empty",
            "filename": "test_empty_input.txt",
            "exp_data": [],
        },
        {
            "test_name": "File contains only letters",
            "filename": "test_letters_input.txt",
            "exp_data": [],
        },
        {
            "test_name": "File contains numbers and letters",
            "filename": "test_letters_and_numbers_input.txt",
            "exp_data": [1, 22],
        },
        {
            "test_name": "File doesn't exist",
            "filename": "no_such_file.txt",
            "exp_data": [],
        },
    ],
    ids=format_name,
)
def test_read_file(opts):
    """
    Test reading file's content
    """
    got_data = read_file(filename=opts["filename"])
    assert got_data == opts["exp_data"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Positive. ",
            "input_sequence": [1, 2, 3, 4, 5],
            "position": 3,
            "preambule_size": 2,
            "expected_sequence": [2, 3],
        },
        {
            "test_name": (
                "Negative. Position is out of input sequence. Lower bound"
            ),
            "input_sequence": [1, 2, 3],
            "position": -1,
            "preambule_size": 1,
            "expected_sequence": [],
        },
        {
            "test_name": (
                "Negative. Position is out of input sequence. Upper bound"
            ),
            "input_sequence": [1, 2, 3],
            "position": 3,
            "preambule_size": 1,
            "expected_sequence": [],
        },
        {
            "test_name": "Negative. Input sequence is empty.",
            "input_sequence": [],
            "position": 0,
            "preambule_size": 2,
            "expected_sequence": [],
        },
        {
            "test_name": (
                "Negative. Preambule size is bigger than input sequence."
            ),
            "input_sequence": [1, 2, 3],
            "position": 1,
            "preambule_size": 4,
            "expected_sequence": [],
        },
    ],
    ids=format_name,
)
def test_get_previous_numbers(opts):
    """
    Test extracting preamble
    """
    got_sequence = get_previous_numbers(
        data=opts["input_sequence"],
        preamble=opts["preambule_size"],
        pos=opts["position"],
    )
    assert got_sequence == opts["expected_sequence"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "All unique numbers. Ascending order.",
            "in_seq": [1, 2, 3],
            "exp_seq": [3, 4, 5],
        },
        {
            "test_name": "All unique numbers. Descending order.",
            "in_seq": [3, 2, 1],
            "exp_seq": [3, 4, 5],
        },
        {"test_name": "All same numbers", "in_seq": [1, 1, 1], "exp_seq": []},
        {
            "test_name": "Two numbers that repeat",
            "in_seq": [1, 2, 1, 2, 1, 2],
            "exp_seq": [3],
        },
    ],
    ids=format_name,
)
def test_get_sums(opts):
    """
    Test rendering sums from the preamble.
    1. Remove all duplicate input values (only unique values can be summed);
    2. Remove all duplicate result values
    """
    got_seq = get_sums(opts["in_seq"])
    assert got_seq == opts["exp_seq"]

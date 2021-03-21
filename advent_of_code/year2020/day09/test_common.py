"""
Test suite for common functions, that are used for solution on day 9
"""
import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day09.common import (
    read_file,
    read_file_until_number,
    get_sums,
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "File exists",
            "filename": "test_expected_input.txt",
            "preamble_size": 2,
            "exp_data": [1, 2, 3],
        },
        {
            "test_name": "File is empty",
            "filename": "test_empty_input.txt",
            "preamble_size": 2,
            "exp_data": [],
        },
        {
            "test_name": "File contains only letters",
            "filename": "test_letters_input.txt",
            "preamble_size": 2,
            "exp_data": [],
        },
        {
            "test_name": "File contains numbers and letters",
            "filename": "test_letters_and_numbers_input.txt",
            "preamble_size": 1,
            "exp_data": [1, 22],
        },
        {
            "test_name": "File doesn't exist",
            "filename": "no_such_file.txt",
            "preamble_size": 2,
            "exp_data": [],
        },
    ],
    ids=format_name,
)
def test_read_file(opts):
    """
    Test reading file's content
    """
    got_data_as_list = []
    for _ in read_file(
        filename=opts["filename"], preamble_size=opts["preamble_size"]
    ):
        got_data_as_list.extend(_)

    assert got_data_as_list == opts["exp_data"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "File doesn't contain requested number",
            "filename": "test_expected_input.txt",
            "target_number": 4,
            "exp": [1, 2, 3],
        },
        {
            "test_name": "File contains requested number",
            "filename": "test_expected_input.txt",
            "target_number": 3,
            "exp": [1, 2],
        },
    ],
    ids=format_name,
)
def test_read_file_until_number(opts):
    """
    Test for read_file_until_number.
    """
    got_data = read_file_until_number(
        filename=opts["filename"], target_number=opts["target_number"]
    )
    assert got_data == opts["exp"]


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

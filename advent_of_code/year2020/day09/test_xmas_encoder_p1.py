"""
Test first part of solution for day 9.
"""
import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day09.xmas_encoder_p1 import solve_the_task


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "All numbers are valid",
            "input_file": "solve_example_valid.txt",
            "preamble_size": 2,
            "exp_value": -1,
        },
        {
            "test_name": "Has invalid sequence",
            "input_file": "solve_example_invalid.txt",
            "preamble_size": 2,
            "exp_value": 8,
        },
    ],
    ids=format_name,
)
def test_solve_the_task(opts):
    """
    Check complete solution
    """
    invalid_number = solve_the_task(
        filename=opts["input_file"], preamble_size=opts["preamble_size"]
    )
    assert invalid_number == opts["exp_value"]

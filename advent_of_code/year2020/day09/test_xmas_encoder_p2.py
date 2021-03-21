"""
Solution for the second task on day 09
"""

import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day09.xmas_encoder_p2 import get_contiguous_set


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Whole set equals to the target nummber",
            "set": [1, 2, 3],
            "target": 6,
            "expected_set": [1, 2, 3],
        },
        {
            "test_name": (
                "Neither the whole set (nor its subpart) is equal to the "
                "target number"
            ),
            "set": [1, 2, 3],
            "target": 4,
            "expected_set": None,
        },
        {
            "test_name": "Contiguous set resides in the begining",
            "set": [1, 2, 3, 4],
            "target": 6,
            "expected_set": [1, 2, 3],
        },
        {
            "test_name": "Contiguous set resides in the middle",
            "set": [1, 2, 3, 4, 5],
            "target": 9,
            "expected_set": [2, 3, 4],
        },
        {
            "test_name": "Contiguous set resides in the end",
            "set": [1, 2, 3, 4, 5],
            "target": 12,
            "expected_set": [3, 4, 5],
        },
        {
            "test_name": "Reference input",
            "set": [
                35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576,
            ],
            "target": 127,
            "expected_set": [15, 25, 47, 40],
        },
    ],
    ids=format_name,
)
def test_get_contiguous_set(opts):
    """
    Test if contiguous set, whose items are equal to the target number, exists
    in the given set.
    """
    got_set = get_contiguous_set(data=opts["set"], target_number=opts["target"])
    assert got_set == opts["expected_set"]

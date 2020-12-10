#!/usr/bin/python3
import pytest
from tree_pass_2 import next_pos, is_tree


@pytest.mark.parametrize(
    opts,[
        {
            "test_name": "Initial position",

        },
        {
            "test_name": "In the middle",
        },
        {
            "test_name": "Last X position, first line"
        },
        {
            "test_name": "Last X position, two lines passed"
        },
        {
            "test_name": "Next coordination must rewind the line"
        },

    ]
)
def test_next_pos():
    new_pos = next_pos(index=0, lines_to_skip=2, line="")
    assert new_pos == 2


@pytest.mark.parametrize(
    'opt',
    [
        {
            'test_name': "positive",
            "line": "#",
            "is_tree": True,
        },
        {
            "test_name": "negative",
            "line": ".",
            "is_tree": False,
        }
    ]
)
def test_is_tree(opt):
    test_value = is_tree(opt["line"], 0)
    assert test_value == opt["is_tree"]


def test_slopes():
    """
        Check the slope's correct movement
    """

    pass

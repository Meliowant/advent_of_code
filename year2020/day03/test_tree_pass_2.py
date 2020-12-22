#!/usr/bin/python3
import pytest
from tree_pass_2 import next_pos, is_tree, next_line


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "",
            "x_pos": 0,
            "step": 2,
            "line": "..X.",
            "exp_position": 2,
        },
        {
            "test_name": "",
            "x_pos": 2,
            "step": 2,
            "line": "..X.",
            "exp_position": 0,
        },
        {
            "test_name": "",
            "x_pos": 1,
            "step": 2,
            "line": "..X.",
            "exp_position": 3,
        },
    ],
)
def test_next_pos(opts):
    new_pos = next_pos(
        x_pos=opts["x_pos"], step=opts["step"], line=opts["line"]
    )
    assert new_pos == opts["exp_position"]


@pytest.mark.parametrize(
    "opt",
    [
        {
            "test_name": "positive",
            "line": "#",
            "is_tree": True,
        },
        {
            "test_name": "negative",
            "line": ".",
            "is_tree": False,
        },
    ],
)
def test_is_tree(opt):
    test_value = is_tree(opt["line"], 0)
    assert test_value == opt["is_tree"]

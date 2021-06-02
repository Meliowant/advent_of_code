#!/usr/bin/env python3
"""
Test suite for checking solution for the second task on day 12
"""

import pytest
from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day12.common import NavigationInstruction
from advent_of_code.year2020.day12.rain_risk_p2 import FerryX, solve_the_task


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Default constructor",
            "args": None,
            "expected_x_pos": 0,
            "expected_y_pos": 0,
            "expected_facing": "E",
            "expected_wp_x_pos": 10,
            "expected_wp_y_pos": -1,
        },
        {
            "test_name": "Custom constructor",
            "args": {"facing": "N", "wp_x_pos": 5, "wp_y_pos": 5},
            "expected_x_pos": 0,
            "expected_y_pos": 0,
            "expected_facing": "N",
            "expected_wp_x_pos": 5,
            "expected_wp_y_pos": 5,
        },
    ],
    ids=format_name,
)
def test_ferryx_creation(opts):
    """
    Check that an instance of FerryX was created
    """
    if opts["args"]:
        my_ferry = FerryX(**opts["args"])
    else:
        my_ferry = FerryX()

    assert my_ferry.x_pos == opts["expected_x_pos"]
    assert my_ferry.y_pos == opts["expected_y_pos"]
    assert my_ferry.facing == opts["expected_facing"]
    assert my_ferry.wp_x_pos == opts["expected_wp_x_pos"]
    assert my_ferry.wp_y_pos == opts["expected_wp_y_pos"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Default constructor",
            "args": None,
            "expected_repr": (
                "<FerryX(x_pos='0', y_pos='0', facing='E', "
                "wp_x_pos='10', wp_y_pos='-1')>"
            ),
        },
        {
            "test_name": "Custom constructor",
            "args": {"facing": "N", "wp_x_pos": 5, "wp_y_pos": 5},
            "expected_repr": (
                "<FerryX(x_pos='0', y_pos='0', facing='N', "
                "wp_x_pos='5', wp_y_pos='5')>"
            ),
        },
    ],
    ids=format_name,
)
def test_ferryx_repr(opts):
    """
    Test re-defined __repr__()
    """
    if opts["args"]:
        my_ferry = FerryX(**opts["args"])
    else:
        my_ferry = FerryX()

    assert my_ferry.__repr__() == opts["expected_repr"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No movement",
            "instructions": [],
            "expected_ferry_pos": (0, 0),
            "expected_wp_pos": (10, -1),
        },
        {
            "test_name": "Single move shipment",
            "instructions": [NavigationInstruction(action="F", value=10)],
            "expected_ferry_pos": (100, -10),
            "expected_wp_pos": (10, -1),
        },
        {
            "test_name": "Single move way point to N3",
            "instructions": [NavigationInstruction(action="N", value=3)],
            "expected_ferry_pos": (0, 0),
            "expected_wp_pos": (10, -4),
        },
        {
            "test_name": "Single move way point to S3",
            "instructions": [NavigationInstruction(action="S", value=3)],
            "expected_ferry_pos": (0, 0),
            "expected_wp_pos": (10, 2),
        },
        {
            "test_name": "Single move way point to E3",
            "instructions": [NavigationInstruction(action="E", value=3)],
            "expected_ferry_pos": (0, 0),
            "expected_wp_pos": (13, -1),
        },
        {
            "test_name": "Single move way point to W3",
            "instructions": [NavigationInstruction(action="W", value=3)],
            "expected_ferry_pos": (0, 0),
            "expected_wp_pos": (7, -1),
        },
    ],
    ids=format_name,
)
def test_ferry_move(opts):
    """
    Test ferry's and waypoint's movement
    """
    my_ferry = FerryX()
    for instruction in opts["instructions"]:
        my_ferry.move(instruction)
    assert (my_ferry.x_pos, my_ferry.y_pos) == opts["expected_ferry_pos"]
    assert (my_ferry.wp_x_pos, my_ferry.wp_y_pos) == opts["expected_wp_pos"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Rotate waypoint around the ship with L90",
            "instruction": NavigationInstruction(action="L", value=90),
            "expected_facing": (-1, -10),
        },
        {
            "test_name": "Rotate waypoint around the ship with R270",
            "instruction": NavigationInstruction(action="R", value=270),
            "expected_facing": (-1, -10),
        },
        {
            "test_name": "Rotate waypoint around the ship with L180",
            "instruction": NavigationInstruction(action="L", value=180),
            "expected_facing": (-10, 1),
        },
        {
            "test_name": "Rotate waypoint around the ship with R180",
            "instruction": NavigationInstruction(action="R", value=180),
            "expected_facing": (-10, 1),
        },
        {
            "test_name": "Rotate waypoint around the ship with L270",
            "instruction": NavigationInstruction(action="L", value=270),
            "expected_facing": (1, 10),
        },
        {
            "test_name": "Rotate waypoint around the ship with R90",
            "instruction": NavigationInstruction(action="R", value=90),
            "expected_facing": (1, 10),
        },
        pytest.param(
            {
                "test_name": "Rotate waypoint with custom value",
                "instruction": NavigationInstruction(action="R", value=100),
                "expected_facing": (-1, -10),
            },
            marks=pytest.mark.xfail(raises=NotImplementedError),
        ),
    ],
    ids=format_name,
)
def test_ferryx_rotate_old_fashion(opts):
    """
    Test rotation basic logic for FerryX
    """
    my_ferry = FerryX()
    my_ferry.rotate(opts["instruction"])
    assert (my_ferry.wp_x_pos, my_ferry.wp_y_pos) == opts["expected_facing"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Rotate waypoint around the ship with L90",
            "instruction": NavigationInstruction(action="L", value=90),
            "expected_facing": (-1, -10),
        },
        {
            "test_name": "Rotate waypoint around the ship with R270",
            "instruction": NavigationInstruction(action="R", value=270),
            "expected_facing": (-1, -10),
        },
        {
            "test_name": "Rotate waypoint around the ship with L180",
            "instruction": NavigationInstruction(action="L", value=180),
            "expected_facing": (-10, 1),
        },
        {
            "test_name": "Rotate waypoint around the ship with R180",
            "instruction": NavigationInstruction(action="R", value=180),
            "expected_facing": (-10, 1),
        },
        {
            "test_name": "Rotate waypoint around the ship with L270",
            "instruction": NavigationInstruction(action="L", value=270),
            "expected_facing": (1, 10),
        },
        {
            "test_name": "Rotate waypoint around the ship with R90",
            "instruction": NavigationInstruction(action="R", value=90),
            "expected_facing": (1, 10),
        },
    ],
    ids=format_name,
)
def test_ferryx_rotate(opts):
    """
    Test rotation advanced logic for FerryX
    """
    my_ferry = FerryX()
    my_ferry.clever_rotate(opts["instruction"])
    assert (my_ferry.wp_x_pos, my_ferry.wp_y_pos) == opts["expected_facing"]


def test_solve_the_task():
    """
    Test main solution.
    """
    got_distance = solve_the_task("aoc_example_1.txt")
    assert got_distance == 286

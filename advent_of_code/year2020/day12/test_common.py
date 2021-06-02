#!/usr/bin/env python3

"""
Test suite for checking common fuctionality for solutions on day 12.
"""

import pytest
from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day12.common import (
    NavigationInstruction, read_instructions, Ferry
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "A file with the single instruction",
            "filename": "single_instruction.txt",
            "expected_instructions": [
                NavigationInstruction(action="N", value=10)
            ]
        },
        {
            "test_name": "An empty file",
            "filename": "empty_file.txt",
            "expected_instructions": []
        },
        {
            "test_name": "A file with no instructions",
            "filename": "no_instructions.txt",
            "expected_instructions": []
        },
        {
            "test_name": "A file with mix of proper and incorrect instruction",
            "filename": "mix_of_instructions.txt",
            "expected_instructions": [
                NavigationInstruction(action="N", value=10),
                NavigationInstruction(action="E", value=10),
            ]
        },
    ],
    ids=format_name
)
def test_read_instructions(opts):
    """
    Check if instructions were read.
    """
    got_instructions = read_instructions(opts["filename"])
    assert got_instructions == opts["expected_instructions"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Ferry creates with default arguments",
            "facing": None,
            "expected": "<Ferry(x_pos='0', y_pos='0', facing='E', angle='0')>"
        },
        {
            "test_name": "Ferry creates with custom argument",
            "facing": "blah",
            "expected": (
                "<Ferry(x_pos='0', y_pos='0', facing='blah', angle='0')>"
            )
        },
    ],
    ids=format_name
)
def test_ferry_creation(opts):
    """
    Check if Ferry creates correctly
    """
    my_ferry = Ferry(opts["facing"]) if opts["facing"] else Ferry()
    assert my_ferry.__repr__() == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Ferry doesn't rotate",
            "angle": NavigationInstruction(action="R", value=0),
            "expected_facing": "E"
        },
        {
            "test_name": "Ferry rotates 90 degrees",
            "angle": NavigationInstruction(action="R", value=90),
            "expected_facing": "S"
        },
        {
            "test_name": "Ferry rotates 90 degrees",
            "angle": NavigationInstruction(action="L", value=90),
            "expected_facing": "N"
        },
        {
            "test_name": "Ferry rotates 90 degrees ccw",
            "angle": NavigationInstruction(action="R", value=-90),
            "expected_facing": "N"
        },
        {
            "test_name": "Ferry rotates 180 degrees",
            "angle": NavigationInstruction(action="R", value=180),
            "expected_facing": "W"
        },
        {
            "test_name": "Ferry rotates 180 degrees",
            "angle": NavigationInstruction(action="L", value=180),
            "expected_facing": "W"
        },
        {
            "test_name": "Ferry rotates 270 degrees",
            "angle": NavigationInstruction(action="R", value=270),
            "expected_facing": "N"
        },
        {
            "test_name": "Ferry rotates 270 degrees",
            "angle": NavigationInstruction(action="L", value=270),
            "expected_facing": "S"
        },

    ],
    ids=format_name
)
def test_ferry_rotation(opts):
    """
    Check if ferry rotates correctly
    """
    my_ferry = Ferry()
    my_ferry.rotate(opts["angle"])
    assert my_ferry.facing == opts["expected_facing"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Ferry doesn't move",
            "direction": NavigationInstruction(action="N", value=0),
            "expected_position": (0, 0)
        },
        {
            "test_name": "Ferry moves north by 1 unit",
            "direction": NavigationInstruction(action="N", value=1),
            "expected_position": (0, -1)
        },
        {
            "test_name": "Ferry moves south by 1 unit",
            "direction": NavigationInstruction(action="S", value=1),
            "expected_position": (0, 1)
        },
        {
            "test_name": "Ferry moves east by 1 unit",
            "direction": NavigationInstruction(action="E", value=1),
            "expected_position": (1, 0)
        },
        {
            "test_name": "Ferry moves west by 1 unit",
            "direction": NavigationInstruction(action="W", value=1),
            "expected_position": (-1, 0)
        },
        {
            "test_name": "Ferry moves in default direcction by 1 unit",
            "direction": NavigationInstruction(action="F", value=1),
            "expected_position": (1, 0)
        },

    ],
    ids=format_name
)
def test_ferry_movement(opts):
    """
    Check if ferry moves correctly
    """
    my_ferry = Ferry()
    my_ferry.move(opts["direction"])
    assert (my_ferry.x_pos, my_ferry.y_pos) == opts["expected_position"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No commands",
            "instructions": [],
            "expected_position": (0, 0),
            "expected_facing": "E",
        },
        {
            "test_name": "Move 1 unit west and 1 unit east",
            "instructions": [
                NavigationInstruction(action="W", value=1),
                NavigationInstruction(action="E", value=1),
            ],
            "expected_position": (0, 0),
            "expected_facing": "E",
        },
        {
            "test_name": "Move to north west by 1 unit and rotate to north",
            "instructions": [
                NavigationInstruction(action="W", value=1),
                NavigationInstruction(action="N", value=1),
                NavigationInstruction(action="R", value=270),
            ],
            "expected_position": (-1, -1),
            "expected_facing": "N",
        },
        {
            "test_name": "Pyramid movement",
            "instructions": [
                NavigationInstruction(action="F", value=1),  # (1, 0) >
                NavigationInstruction(action="R", value=90),  # v
                NavigationInstruction(action="F", value=1),  # (1, 1) v
                NavigationInstruction(action="R", value=-90),  # >
                NavigationInstruction(action="F", value=1),  # (2, 1) >
                NavigationInstruction(action="R", value=90),  # v
                NavigationInstruction(action="F", value=1),  # (2, 2) v
                NavigationInstruction(action="R", value=-90),  # >
                NavigationInstruction(action="F", value=2),  # (4, 2) >
                NavigationInstruction(action="R", value=-90),  # ^
                NavigationInstruction(action="F", value=1),  # (4, 1) ^
                NavigationInstruction(action="R", value=90),  # >
                NavigationInstruction(action="F", value=1),  # (5, 1) >
                NavigationInstruction(action="R", value=-90),  # ^
                NavigationInstruction(action="F", value=1),  # (5, 0) ^
                NavigationInstruction(action="R", value=90),  # >
                NavigationInstruction(action="F", value=1),  # (6, 0) >
                NavigationInstruction(action="R", value=-90),  # ^
            ],
            "expected_position": (6, 0),
            "expected_facing": "N",
        },

    ],
    ids=format_name
)
def test_ferry_execute(opts):
    """
    Check if ferry correctly executes given commands
    """
    my_ferry = Ferry()
    for instr in opts["instructions"]:
        my_ferry.execute(instr)
    assert (my_ferry.x_pos, my_ferry.y_pos) == opts["expected_position"]
    assert my_ferry.facing == opts["expected_facing"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No commands",
            "instructions": [],
            "expected_distance": 0,
        },
        {
            "test_name": "Move 1 unit west and 1 unit east",
            "instructions": [
                NavigationInstruction(action="W", value=1),
                NavigationInstruction(action="E", value=1),
            ],
            "expected_distance": 0,
        },
        {
            "test_name": "Move to north west by 1 unit and rotate to north",
            "instructions": [
                NavigationInstruction(action="W", value=1),
                NavigationInstruction(action="N", value=1),
                NavigationInstruction(action="R", value=270),
            ],
            "expected_distance": 2,
        },
        {
            "test_name": "Pyramid movement",
            "instructions": [
                NavigationInstruction(action="F", value=1),  # (1, 0) >
                NavigationInstruction(action="R", value=90),  # v
                NavigationInstruction(action="F", value=1),  # (1, 1) v
                NavigationInstruction(action="R", value=-90),  # >
                NavigationInstruction(action="F", value=1),  # (2, 1) >
                NavigationInstruction(action="R", value=90),  # v
                NavigationInstruction(action="F", value=1),  # (2, 2) v
                NavigationInstruction(action="R", value=-90),  # >
                NavigationInstruction(action="F", value=2),  # (4, 2) >
                NavigationInstruction(action="R", value=-90),  # ^
                NavigationInstruction(action="F", value=1),  # (4, 1) ^
                NavigationInstruction(action="R", value=90),  # >
                NavigationInstruction(action="F", value=1),  # (5, 1) >
                NavigationInstruction(action="R", value=-90),  # ^
                NavigationInstruction(action="F", value=1),  # (5, 0) ^
                NavigationInstruction(action="R", value=90),  # >
                NavigationInstruction(action="F", value=1),  # (6, 0) >
                NavigationInstruction(action="R", value=-90),  # ^
            ],
            "expected_distance": 6,
        },

    ],
    ids=format_name
)
def test_ferry_manhattan_distance(opts):
    """
    Test Manhattan distance calculation after ferry made a set of movements
    """
    my_ferry = Ferry()
    for instr in opts["instructions"]:
        my_ferry.execute(instr)
    got_distance = my_ferry.manhattan_distance()
    assert got_distance == opts["expected_distance"]

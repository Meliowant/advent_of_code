#!/usr/bin/env python3
import pytest

from advent_of_code.year2025.day01.solution_01 import SafeDial

def test_safedial_init():
    """Check if wheel contains all values"""
    sd = SafeDial(10)
    assert sd.size == 10

@pytest.mark.parametrize(
    "dial_size", [
        1, 5, 15
    ]
)
def test_current_position(dial_size):
    """Check position for the dial"""
    sd = SafeDial(dial_size)
    assert sd.position == 0


@pytest.mark.parametrize("init_pos", [1, 2, 4, 5, 7])
def test_safedial_init_pos(init_pos):
    """Check if user-defined initial position is OK"""
    sd = SafeDial(10, init_pos)
    assert sd.position == init_pos

@pytest.mark.parametrize(
    "dial_size, init_pos, shift, new_pos",
    [
        (10, 9, 1, 8),
        (10, 5, 5, 0),
        (10, 9, 11, 8),
        (10, 0, 1, 9),
        (100, 19, 19, 0),
        (100, 5, 10, 95)
    ]
)
def test_rotate_left(dial_size, init_pos, shift, new_pos):
    """Check if rotation left works as expected"""
    sd = SafeDial(dial_size, init_pos)
    sd.rotate_left(shift)
    assert sd.position == new_pos

@pytest.mark.parametrize(
    "dial_size, init_pos, shift, new_pos",
    [
        (10, 9, 1, 0),
        (10, 5, 5, 0),
        (10, 9, 10, 9),
        (100, 11, 8, 19),
        (100, 99, 1, 0),
    ]
)
def test_rotate_right(dial_size, init_pos, shift, new_pos):
    """Check if rotation left works as expected"""
    sd = SafeDial(dial_size, init_pos)
    sd.rotate_right(shift)
    assert sd.position == new_pos

@pytest.mark.parametrize(
        "dial_size, rot_str, exp_val", [
            (10, ("R5", ), 5),
            (2, ("R1", "L1", ), 0),
            (2, ("L1", "R1", ), 0),
            (100, ("L1", ), 99),
        ],
        ids=[
            "10-(R5)-5",
            "2-(R1-L1)-0",
            "2-(L1-R1)-0",
            "100-(L1)-0",
            ]
)
def test_rotation(dial_size, rot_str, exp_val):
    """ Test rotation algorithm """
    sd = SafeDial(dial_size)
    for r in rot_str:
        sd.rotate(r)
    assert sd.position == exp_val


def test_acceptance():
    """
    Example, provided by Advent of Code.
    Safe dial's size is 99. Initial value - 0.
    Turns are:
    - L68
    - L30
    - R48
    - L5
    - R60
    - L55
    - L1
    - L99
    - R14
    - L82
    """

    turns = [
            "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"
    ]
    sd = SafeDial(100, 50)
    positions = []
    for turn in turns:
        sd.rotate(turn)
        if sd.position == 0:
            positions.append(sd.position)
    assert len(positions) == 3, positions

#!/usr/bin/env python3
import pytest

from advent_of_code.year2025.day01.solution_01 import locker_wheel

def test_locker_wheel():
    """Check if wheel contains all values"""
    assert locker_wheel[0] == 0
    assert locker_wheel[-1] == 99


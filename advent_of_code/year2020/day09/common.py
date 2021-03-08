#!/usr/bin/python3
"""
Common functions for day 9 solution.
"""


import pathlib


def read_file(filename: str = None) -> list:
    """
    Read all numbers from the file. Each number resides a single line.
    Lines that don't contain number are ignored.
    """
    retval = []
    input_data = pathlib.Path(filename)
    if not input_data.exists():
        return retval
    with input_data.open() as data:
        for line in data:
            try:
                num = int(line)
                retval.append(num)
            except (TypeError, ValueError):  # Skip such line
                pass
    return retval


def get_previous_numbers(
    data: list = None, preamble: int = 25, pos: int = 0
) -> list:
    """
    Extract a list of numbers from the incoming data.
    """
    retval = []

    if not data:
        return retval
    if preamble < 1:
        return retval
    if pos < 0 or pos > len(data) - 1:
        return retval
    if pos - preamble < 0:
        return retval

    startpos = pos - preamble
    retval = data[startpos:pos]
    return retval


def get_sums(data: list = None) -> list:
    """
    Calculate sums of all numbers from th incoming data:w
    """
    retval = []
    unique_data = []
    data.sort()

    for val in data:
        if val not in unique_data:
            unique_data.append(val)

    for idx, value in enumerate(unique_data):
        idx2 = idx + 1
        while idx2 < len(unique_data):
            retval.append(value + unique_data[idx2])
            idx2 += 1

    # Sort-out unique values
    unique_data = []
    for val in retval:
        if val not in unique_data:
            unique_data.append(val)
    return unique_data

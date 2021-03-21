#!/usr/bin/python3
"""
Common functions for day 9 solution.
"""


import pathlib


def read_file(filename: str = None, preamble_size: int = 25) -> list:
    """
    Read all numbers from the file. Each number resides a single line.
    Lines that don't contain number are ignored.
    """
    retval = []
    read_items = 0
    input_data = pathlib.Path(filename)
    if not input_data.exists():
        return retval
    with input_data.open() as data:
        for line in data:
            try:
                num = int(line)
                retval.append(num)
                read_items += 1
                if read_items > preamble_size:
                    list_size = preamble_size + 1
                    retval = retval[-list_size:]  # Only useful items
                    yield retval
            except (TypeError, ValueError):  # Skip such line
                pass
    return retval


def read_file_until_number(filename=None, target_number=None):
    """
    Read the content of the file before the <number> will appear
    """
    input_file = pathlib.Path(filename)
    retval = []
    if not input_file.exists():
        return retval
    with input_file.open() as data:
        for line in data:
            try:
                num = int(line)
                if num == target_number:
                    return retval
                retval.append(num)
            except (TypeError, ValueError):
                pass
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

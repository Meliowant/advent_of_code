"""
Set of common functions for this day's solution.
"""

import pathlib


def read_data(file_name: str = ""):
    """
    Read the content of the given file. Return it as a list.
    """
    output = []
    datafile = pathlib.Path(file_name)
    if not datafile.exists():
        return output
    with datafile.open("r") as data:
        line = data.readline()
        while line:
            try:
                num = int(line)
                output.append(num)
            except (TypeError, ValueError):
                pass
            line = data.readline()
    return output


def get_devices_joltage(adapters: list = None):
    """
    Get device's joltage
    """
    return max(adapters) + 3 if adapters else 3


def get_tried_out_adapters(
    adapters: list = None, init_joltage: int = None
) -> (list, list):
    """
    Extract all compatible adapters from the provided list.

    Keyword arguments:
        adapters -- list of available adapters
        init_joltage -- input joltage that will be utilized by adapter

    Returns:
        A tuple of two lists:
            The first list is a list of supported adapters;
            The second list is a list of remained adapters.
    """
    used_adapters = []
    remained_adapters = []
    for adapter in adapters:
        if adapter <= init_joltage:
            continue
        if adapter < init_joltage + 3:
            target_adapters = used_adapters
        else:
            target_adapters = remained_adapters
        target_adapters.append(adapter)
    return (used_adapters, remained_adapters)


def pick_adapter(
    adapters: list = None, input_joltage: int = None
) -> (int, int):
    """
    Pick the most suitable adapter.

    Keyword arguments:
        adapters -- list of adapters that can operate with the input joltage
        input_joltage -- joltage value for the adapter

    Returns:
        A tuple of int values:
            - Output joltage value for the picked adapter
            - Difference between input and output joltage value
    """
    picked_adapter = min(adapters)
    diff = picked_adapter - input_joltage
    return (picked_adapter, diff)

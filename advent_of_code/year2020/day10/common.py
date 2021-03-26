"""
Set of common functions for this day's solution.
"""

import pathlib


class JoltageStats():
    """
    Single source for collecting joltage differences
    """
    def __init__(self):
        self.joltage_diffs = {}

    def collect(self, in_joltage: int) -> None:
        """
        Summarize joltages statistics
        """
        diff = str(in_joltage)  # This is key
        if diff not in self.joltage_diffs.keys():
            self.joltage_diffs[diff] = 1
        else:
            self.joltage_diffs[diff] += 1

    def report(self):
        """
        Return joltage difference sumamry
        """
        return self.joltage_diffs


def read_data(file_name: str = "") -> list:
    """
    Read the content of the given file. Return it as a list.

    Keyword arguments:
        file_name -- name on a file with the source.:w
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


def get_devices_joltage(adapters: list = None) -> int:
    """
    Get device's joltage

    Keyword arguments:
        adapters - list of integers, that represent adapters' output joltage

    Returns:
        Target device's input joltage.
    """
    return max(adapters) + 3 if adapters else 3


def get_compatible_adapter(
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
    comp_adapters = []
    incomp_adapters = []
    min_joltage = init_joltage + 1
    max_joltage = init_joltage + 3
    for adapter in sorted(adapters):
        if adapter <= init_joltage:
            continue
        if min_joltage <= adapter <= max_joltage:
            target_adapters = comp_adapters
        else:
            target_adapters = incomp_adapters
        target_adapters.append(adapter)
    comp_adapters.sort()
    compatible_adapter = comp_adapters.pop(0) if comp_adapters else -1

    remained_adapters = comp_adapters + incomp_adapters
    return (compatible_adapter, remained_adapters)


def get_joltage_diff(in_joltage: int = None, out_joltage: int = None) -> int:
    """
    Calculate difference between joltage values

    Keyword arguments:
        in_joltage - input joltage value
        out_joltage - output joltage value

    Returns:
        On success - difference between joltage values;
        On failure - -1.
    """
    try:
        in_joltage = int(in_joltage)
        out_joltage = int(out_joltage)
    except (TypeError, ValueError):
        return -1
    return out_joltage - in_joltage

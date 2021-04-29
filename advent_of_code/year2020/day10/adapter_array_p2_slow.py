"""
Solution for the second part of the day 10.
"""
from advent_of_code.year2020.day10.common import (
    read_data,
    get_devices_joltage,
    get_compatible_adapters,
)


def calculate_combinations(
    adapters: list = [], init: int = None, final: int = None
):
    """
    Calculate combinations. This is my second approach, that is not straight-
    forward. Here I calculate next
    """
    pass


def list_all_combinations(
    adapters: list = None, target_joltage: int = None
) -> list:
    """
    Create a list of combinations for all the adapters, that can be joined
    together, from the source (starts with 0) to the target device. Each
    adapter can be connected to the source (output outlet, or other adapter),
    whose output joltage is not bigger than 3 joltages.

    Keyword arguments:
        adapters - a list of adapters' input joltage.
        target_joltage - input joltage for target device.
    """
    combinations = []
    check_combinations = [[0]]
    adapters.append(target_joltage)
    counter = 0

    while check_combinations:
        combination = check_combinations.pop(0)
        last_adapter = combination[-1]
        comp_adapters = get_compatible_adapters(
            adapters=adapters, input_joltage=last_adapter
        )
        if not comp_adapters and combination[-1] == target_joltage:
            if combination not in combinations:
                combinations.append(combination)
            continue

        for adapter in sorted(comp_adapters):
            new_combination = combination.copy()
            new_combination.append(adapter)
            check_combinations.append(new_combination)

        remained = len(check_combinations)
        if remained % 1000000 == 0:
            max_len = max([len(x) for x in check_combinations])
            cur_max = (
                max([len(x) for x in combinations]) if combinations else 0
            )
            print(
                f"Combinations processed: {counter}, "
                f"remains: {remained} "
                f"maxlen: {max_len} "
                f"curmax: {cur_max}"
            )

        counter += 1

    return combinations


def solve_the_task(file_name: str = None) -> int:
    """
    Calculate total amount of possible combinations for given adapters.

    Keyword arguments:
        file_name - file that contains a list of adapters. Each line contains
        adapter's input joltage

    Returns:
        On success - integer number of possible combinations for given adapters
        On failure - 0
    """
    adapters = read_data(file_name)
    target_joltage = get_devices_joltage(adapters)
    combinations = list_all_combinations(
        adapters=adapters, target_joltage=target_joltage
    )
    total_combinations = len(combinations)
    return total_combinations


def solve_the_task_short(adapters: list = [], target_joltage: int = None):
    pass


if __name__ == "__main__":
    COMBINATIONS = solve_the_task(file_name="test_input.txt")
    print(f"Adapters can be joined in '{COMBINATIONS}' combinations.")

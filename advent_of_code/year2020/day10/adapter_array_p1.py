"""
Solution for the first part of day's 10 task
"""


from advent_of_code.year2020.day10.common import (
    JoltageStats,
    read_data,
    get_devices_joltage,
    get_compatible_adapter,
    get_joltage_diff,
)


def get_adapters_and_stats(file_name: str) -> (list, dict):
    """
    Get a list of used adapters and their joltage differences
    """
    out_joltage = 0
    used_adapters = [out_joltage]
    jolt_stats = JoltageStats()

    adapters = read_data(file_name=file_name)
    exp_out_joltage = get_devices_joltage(adapters)

    while out_joltage < exp_out_joltage and len(adapters) > 0:
        adapter, adapters = get_compatible_adapter(adapters, out_joltage)
        used_adapters.append(adapter)
        joltage_diff = get_joltage_diff(out_joltage, adapter)
        out_joltage = adapter
        jolt_stats.collect(joltage_diff)

    final_diff = get_joltage_diff(used_adapters[-1], exp_out_joltage)
    jolt_stats.collect(final_diff)
    return used_adapters, jolt_stats.report()


def solve_the_task(file_name: str = None) -> (list, dict):
    """
    Main function to pick a list of existing adapters from the file, and
    return a list of used adapters, and joltage differences between them.
    """
    _, stats = get_adapters_and_stats(file_name)
    one_jolt_diffs = stats.get("1", 0)
    three_jol_diffs = stats.get("3", 0)
    return one_jolt_diffs * three_jol_diffs


if __name__ == "__main__":
    result = solve_the_task(file_name="test_input.txt")
    print(f"Multiplied joltage value: {result}")

#!/usr/bin/python3

"""
This is solution for the second task on day 9 from Advent of Code
"""

from advent_of_code.year2020.day09.common import read_file_until_number


def get_contiguous_set(data: list = None, target_number: int = None) -> list:
    """
    Get a list of contiguous numbers sum of which equals to target_number.
    """
    output = []
    for idx in range(len(data)):
        internal_idx = idx
        output = []
        while internal_idx < len(data):
            output.append(data[internal_idx])
            if sum(output) >= target_number:
                break
            internal_idx += 1

        if sum(output) == target_number:
            break

    output = output if sum(output) == target_number else None
    return output


def solve_the_task(filename: str = None, target_number: int = None) -> int:
    """
    Find an XMAS encryption weakness number
    """
    encryption_weakness = -1
    data = read_file_until_number(
        filename=filename, target_number=target_number
    )
    print(f"Totally read {len(data)} numbers")
    print(f"Obtained data: {data}")
    contiguous_set = get_contiguous_set(data, target_number)
    print(f"Set of data: {contiguous_set}")
    if contiguous_set:
        encryption_weakness = min(contiguous_set) + max(contiguous_set)
    return encryption_weakness


if __name__ == "__main__":
    weak_num = solve_the_task(filename="input.txt", target_number=27911108)
    print(f"XMAS encryption number is: '{weak_num}'")

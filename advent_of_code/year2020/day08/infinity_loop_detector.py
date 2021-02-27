#!/usr/bin/python3

from collections import namedtuple
from advent_of_code.year2020.day08.common import (
    Instruction,
    read_file,
    instruction_index,
    run_emulation,
)


def solve_task(filename=""):
    instructions = read_file(filename)
    trace, acc_value = run_emulation(instructions)
    return trace, acc_value


if __name__ == "__main__":
    res = solve_task(filename="input_data.txt")
    print(f"Accumulator's value prior loop was '{res[1]}'.")

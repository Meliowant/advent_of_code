#!/usr/bin/python3

from collections import namedtuple
from advent_of_code.year2020.day08.common import (
    Instruction,
    read_file,
    instruction_index,
)


def run_emulation(instructions=[]):
    rv = []
    accumulator_value = 0
    current_step = 0
    step_counter = 1
    while True and 0 <= current_step < len(instructions):
        # import pdb;pdb.set_trace()
        instr = instructions[current_step]
        instr_idx = instruction_index(instr, rv)
        if instr_idx < 0:
            rv.append([instr, [step_counter]])
        else:
            rv[instr_idx][1].append(step_counter)
            return rv, accumulator_value  # Instructions called more than once

        next_step = instr.arg if instr.cmd == "jmp" else 1
        accumulator_value += instr.arg if instr.cmd == "acc" else 0
        current_step = current_step + next_step
        step_counter += 1
    return rv, accumulator_value


def solve_task(filename=""):
    instructions = read_file(filename)
    trace, acc_value = run_emulation(instructions)
    return trace, acc_value


if __name__ == "__main__":
    res = solve_task(filename="input_data.txt")
    print(f"Accumulator's value prior loop was '{res[1]}'.")

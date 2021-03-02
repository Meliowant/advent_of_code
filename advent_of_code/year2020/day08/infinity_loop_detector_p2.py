#!/usr/bin/python3

from advent_of_code.year2020.day08.common import (
    Instruction,
    read_file,
    instruction_index,
)


def run_emulation(instructions=None):
    """
    Run emulation for the second part. It is similar to the emulation
    of the first part, but I added here a variable to track if code
    was executed till its end.
    """
    rv = []
    accumulator_value = 0
    current_step = 0
    step_counter = 1
    completed = False
    while 0 <= current_step < len(instructions):
        # import pdb;pdb.set_trace()
        instr = instructions[current_step]
        instr_idx = instruction_index(instr, rv)
        if instr_idx < 0:
            rv.append([instr, [step_counter]])
        else:
            rv[instr_idx][1].append(step_counter)
            return (
                rv,
                accumulator_value,
                completed,
            )  # Instructions called more than once

        next_step = instr.arg if instr.cmd == "jmp" else 1
        accumulator_value += instr.arg if instr.cmd == "acc" else 0
        current_step = current_step + next_step
        step_counter += 1

    completed = True
    return rv, accumulator_value, completed


def solve_task(filename=""):
    """
    Main method to complete the task.
    """
    instructions = read_file(filename)
    completed = True
    trace = []
    acc_value = 0
    for idx, instruction in enumerate(instructions):
        completed = False
        cloned_instructions = instructions.copy()
        if instruction.cmd == "nop":
            new_code = "jmp"
        elif instruction.cmd == "jmp":
            new_code = "nop"
        else:
            continue

        cloned_instructions[idx] = Instruction(
            cmd=new_code, pos=idx, arg=instructions[idx].arg
        )
        trace, acc_value, completed = run_emulation(cloned_instructions)
        if completed:
            break
    return trace, acc_value, completed


if __name__ == "__main__":
    res = solve_task(filename="input_data.txt")
    print(f"Accumulator's value prior loop was '{res[1]}'.")

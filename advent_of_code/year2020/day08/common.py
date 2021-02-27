from collections import namedtuple
import re
import os

Instruction = namedtuple("Instruction", ["cmd", "pos", "arg"])
instr_struct = re.compile("([a-zA-Z]+) ([+-][0-9]+)")


def read_file(fname=""):
    rv = []
    counter = 0
    if not(os.path.exists(fname)):
        return rv
    with open(fname, "r") as data:
        for line in data:
            m = instr_struct.search(line)
            if m:
                instr = Instruction(
                    cmd=m.groups()[0], pos=counter, arg=int(m.groups()[1])
                )
                rv.append(instr)
                counter += 1
    return rv


def instruction_index(instr: Instruction, instructions: list) -> int:
    for idx, item in enumerate(instructions):
        if item[0] == instr:
            return idx
    return -1


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

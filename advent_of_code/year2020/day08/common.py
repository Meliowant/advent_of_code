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




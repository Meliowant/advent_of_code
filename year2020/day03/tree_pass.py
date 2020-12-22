#!/usr/bin/python3


def next_pos(cur_pos, shift, line):
    new_pos = (cur_pos + shift) % (len(line))
    return new_pos


def is_tree(line, pos):
    return line[pos] == "#"


trees = 0
steps = 0
# Read the file
with open("demo.txt", "r") as data:
    line = data.readline()
    line = line.strip("\n")
    line = data.readline()
    line = line.strip("\n")
    pos = 0
    steps += 1
    while line != "":
        pos = next_pos(pos, 3, line)
        if is_tree(line, pos):
            trees += 1
        line = data.readline()
        line = line.strip("\n")
        steps += 1

print(f"Found {trees} trees, making {steps} steps.")

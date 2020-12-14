#!/usr/bin/python3

def next_pos(x_pos, step, line):
    new_x_pos = (x_pos + step) % len(line)
    return new_x_pos


def next_line(fd, stop_on_line):
    for i in range(stop_on_line):
        line = fd.readline()
        line = line.strip('\n')
    return line


def is_tree(line, pos):
    return line[pos] == "#"


def trace_path(filename, stop_on_line:int=1, shift:int=1) -> (int, int):
    trees = 0
    steps = 0
    # Read the file
    with open(filename, "r") as data:
        line = data.readline()
        line = line.strip("\n")
        pos = 0
        steps += 1
        if is_tree(line, pos):
            trees += 1

        line = next_line(data, stop_on_line)
        while line != '':
            pos = next_pos(pos, shift, line)
            if is_tree(line, pos):
                trees += 1
            line = next_line(data, stop_on_line)
            steps += 1

    return trees, steps


def solve_the_task(filename="demo.txt"):
    # 1 down, 1 right
    trees, steps = trace_path(filename, stop_on_line=1, shift=1)
    print(f"Found {trees} trees, making {steps} steps.")
    # 1 down, 3 right
    trees, steps = trace_path(filename, stop_on_line=1, shift=3)
    print(f"Found {trees} trees, making {steps} steps.")
    # 1 down, 5 right
    trees, steps = trace_path(filename, stop_on_line=1, shift=5)
    print(f"Found {trees} trees, making {steps} steps.")
    # 1 down, 7 right
    trees, steps = trace_path(filename, stop_on_line=1, shift=7)
    print(f"Found {trees} trees, making {steps} steps.")
    # 2 down, 1 right
    trees, steps = trace_path(filename, stop_on_line=2, shift=1)
    print(f"Found {trees} trees, making {steps} steps.")


if __name__ == "__main__":
    solve_the_task(filename="demo.txt")

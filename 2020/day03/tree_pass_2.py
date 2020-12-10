#!/usr/bin/python3

def next_pos(x_pos, y_pos):
    new_x_pos = x_pos + 2
    if new_x_pos > 7:
        new_x_pos = 1
        new_y_pos = y_pos + 1
    else:
        new_y_pos = y_pos
    return (new_x_pos, new_y_pos)


def is_tree(line, pos):
    return line[pos] == "#"


def solve_the_task(input_file="demo.txt"):
    trees = 0
    steps = 0
    # Read the file
    with open(input_file, "r") as data:
        line = data.readline()
        line = data.readline()
        line = line.strip('\n')
        pos = 0
        steps += 1
        while line != '':
            pos = next_pos(pos, 3, line)
            if is_tree(line, pos):
                trees += 1
            line = data.readline()
            line = line.strip('\n')
            steps += 1

    print(f"Found {trees} trees, making {steps} steps.")


if __name__ == "__main__":
    solve_the_task(filename="demo.txt")

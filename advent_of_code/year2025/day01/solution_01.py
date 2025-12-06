#!/usr/bin/env python3
"""
Solution for day 1, task 1.
"""
import argparse

class SafeDial:
    """ This is safe dial class to pick correct password to enter throuh
    the secret entrance at the North Pole
    """
    def __init__(self, size: int, init_position: int = 0):
        self.size = size
        self._position = init_position

    @property
    def position(self):
        return self._position

    @position.setter
    def set_position(self, value):
        self._position = value

    def rotate_left(self, shift):
        self._position = self._position - shift
        if self._position < 0:
            self._position = self.size + self._position

    def rotate_right(self, shift):
        self._position = self._position + shift
        if self._position >= self.size:
            self._position = self._position - self.size

    def rotate(self, value):
        """Take decision where to turn the dial, and update the position
           accordingly"""

        direction, step = value[:1], int(value[1:])
        step = step % self.size
        if direction == "R":
            self.rotate_right(step)
        elif direction == "L":
            self.rotate_left(step)

def solve_task_01(input_file):
    """Code to run first solution for day 1"""

    sd = SafeDial(100, 50)
    zero_tick_counter = 0
    positions = []

    with open(input_file, "rt") as fd:
        line = fd.readline().strip()

        while line:
            sd.rotate(line)
            positions.append(sd.position)
            line = fd.readline().strip()

    print(
        f"Dial was at 0 position {positions.count(0)} times "
        "for {len(positions)} turns."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-f", "--file", help="File to read input from", required=True
    )
    args = parser.parse_args()
    solve_task_01(args.file)

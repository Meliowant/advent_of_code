#!/usr/bin/env python3
"""
Solution for the second task on day 12
"""

import math
from advent_of_code.year2020.day12.common import read_instructions, Ferry


class FerryX(Ferry):
    """
    An updated version of Ferry class
    """

    def __init__(
        self, facing: str = "E", wp_x_pos: int = 10, wp_y_pos: int = 1
    ) -> "FerryX":
        """
        Extend existing Ferry with waypoint coordinates
        """
        self.x_pos = 0
        self.y_pos = 0
        self.wp_x_pos = wp_x_pos
        self.wp_y_pos = wp_y_pos
        hipo_value = math.sqrt(self.wp_x_pos ** 2 + self.wp_y_pos ** 2)
        self.facing = round(
            math.degrees(math.asin(self.wp_y_pos / hipo_value))
        )

    def __repr__(self):
        return (
            f"<FerryX(x_pos='{self.x_pos}', y_pos='{self.y_pos}', "
            f"facing='{self.facing}', "
            f"wp_x_pos='{self.wp_x_pos}', wp_y_pos='{self.wp_y_pos}')>"
        )

    def move(self, instruction):
        if instruction.action == "F":
            self.x_pos += self.wp_x_pos * instruction.value
            self.y_pos += self.wp_y_pos * instruction.value
        else:
            value = instruction.value
            if instruction.action in ["S", "W"]:
                value = -value

            if instruction.action in ["N", "S"]:
                self.wp_y_pos += value
            else:
                self.wp_x_pos += value

    def legacy_rotate(self, instruction):
        """
        Waypoint rotation logic for angles 90, 180, 270 left or right
        """
        act = instruction.action
        val = instruction.value
        if (act, val) in [("L", 90), ("R", 270)]:
            self.wp_x_pos, self.wp_y_pos = -self.wp_y_pos, self.wp_x_pos
        elif val == 180:
            self.wp_x_pos, self.wp_y_pos = -self.wp_x_pos, -self.wp_y_pos
        elif (act, val) in [("L", 270), ("R", 90)]:
            self.wp_x_pos, self.wp_y_pos = self.wp_y_pos, -self.wp_x_pos
        else:
            raise NotImplementedError("Random rotation is not implemented")

    def rotate(self, instruction):
        """
        Allow ferry's rotation on any degree
        """
        hipo_value = math.sqrt(self.wp_x_pos ** 2 + self.wp_y_pos ** 2)
        degrees = round(
            math.degrees(math.acos(self.wp_x_pos / hipo_value))
        )
        if self.wp_y_pos < 0:
            degrees = 360 - degrees

        degrees += (-1 if instruction.action == "R" else 1) * instruction.value

        self.wp_x_pos = round(hipo_value * math.cos(math.radians(degrees)))
        self.wp_y_pos = round(hipo_value * math.sin(math.radians(degrees)))
        self.facing = round(
            math.degrees(math.asin(self.wp_y_pos / hipo_value))
        )


def solve_the_task(filename: str) -> int:
    """
    Main function for solving the task
    """
    instructions = read_instructions(filename)
    my_ferry = FerryX()
    for instruction in instructions:
        my_ferry.execute(instruction)
    man_dist = my_ferry.manhattan_distance()
    print(f"Manhattan distance for ferry in the final point is '{man_dist}'")
    return man_dist


if __name__ == "__main__":
    solve_the_task(filename="aoc_input.txt")

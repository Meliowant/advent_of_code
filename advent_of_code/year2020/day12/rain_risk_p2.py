#!/usr/bin/env python3
"""
Solution for the second task on day 12
"""

from advent_of_code.year2020.day12.common import read_instructions, Ferry


class FerryX(Ferry):
    """
    An updated version of Ferry class
    """

    def __init__(
        self, facing: str = "E", wp_x_pos: int = 10, wp_y_pos: int = -1
    ) -> "FerryX":
        """
        Extend existing Ferry with waypoint coordinates
        """
        super().__init__(facing)
        self.wp_x_pos = wp_x_pos
        self.wp_y_pos = wp_y_pos

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
            if instruction.action in ["N", "W"]:
                value = -value

            if instruction.action in ["N", "S"]:
                self.wp_y_pos += value
            else:
                self.wp_x_pos += value

    def rotate(self, instruction):
        act = instruction.action
        val = instruction.value
        if (act, val) in [("L", 90), ("R", 270)]:
            self.wp_x_pos, self.wp_y_pos = self.wp_y_pos, -self.wp_x_pos
        elif val == 180:
            self.wp_x_pos, self.wp_y_pos = -self.wp_x_pos, -self.wp_y_pos
        elif (act, val) in [("L", 270), ("R", 90)]:
            self.wp_x_pos, self.wp_y_pos = -self.wp_y_pos, self.wp_x_pos
        else:
            raise NotImplementedError("Random rotation is not implemented")


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

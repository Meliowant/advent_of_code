#!/usr/bin/env python3

"""
A set of common functions that will be used by both solutions for the day 12.
"""

from collections import namedtuple
import re
import pathlib

NavigationInstruction = namedtuple(
    "NavigationInstruction", ["action", "value"]
)


def read_instructions(filename: str = None) -> list:
    """
    Read instructions from the given file
    """
    retval = []
    f_name = pathlib.Path(filename)
    instr_re = r"^(?P<action>[a-zA-Z])(?P<value>-?[0-9]+)$"
    with f_name.open("r") as f:
        line = f.readline()
        while line:
            parsed_line = re.match(instr_re, line)
            if parsed_line:
                retval.append(
                    NavigationInstruction(
                        action=parsed_line.groupdict().get("action"),
                        value=int(parsed_line.groupdict().get("value"))
                    )
                )
            line = f.readline()
    return retval


class Ferry:
    def __init__(self, facing: str = None):
        """
        Create new ferry in its initial point
        """
        self.x_pos = 0
        self.y_pos = 0
        self.facing = "E" if not facing else facing
        self.angle = 0

    def __repr__(self):
        """
        Get representation
        """
        return (
            f"<Ferry(x_pos='{self.x_pos}', y_pos='{self.y_pos}', "
            f"facing='{self.facing}', angle='{self.angle}')>"
        )

    def rotate(self, instruction):
        """
        Rotate ferry
        """
        degs_to_facing = [(0, "E"), (90, "S"), (180, "W"), (270, "N")]
        value = -instruction.value \
            if instruction.action == "L" \
            else instruction.value
        self.angle += value
        self.angle = abs(self.angle % 360)
        deviations = {abs(df[0]-self.angle): df[1] for df in degs_to_facing}
        self.facing = deviations[min(deviations.keys())]
        return self.facing

    def move(self, instruction):
        """
        Move ferry towards safe port
        """
        direction = instruction.action
        units = instruction.value

        target_units = -units\
            if direction in ["N", "W"] or \
            direction == "F" and self.facing in ["N", "W"]\
            else units

        if direction in ["N", "S"] or (
            direction == "F" and self.facing in ["N", "S"]
        ):
            self.y_pos += target_units
        else:
            self.x_pos += target_units

        return self.x_pos, self.y_pos

    def execute(self, instruction):
        """
        Wraper for instruction execution
        """
        if instruction.action in ["R", "L"]:
            self.rotate(instruction)
        else:
            self.move(instruction)

    def manhattan_distance(self):
        """
        Calculate manhattan distance between ferry's x and y coordinates
        """
        return abs(self.x_pos) + abs(self.y_pos)

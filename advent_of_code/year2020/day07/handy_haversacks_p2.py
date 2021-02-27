#!/usr/bin/python3
from advent_of_code.year2020.day07.conftest import (
    read_bags_from_file,
    build_dependencies_down,
    calculate_bags,
)


def solve_the_task(filename=None, target_color=None):
    collected_bags, collected_rules = read_bags_from_file(filename)
    # print(collected_bags)
    bags_dependencies = build_dependencies_down(collected_bags, target_color)
    # print(bags_dependencies)
    total_bags = calculate_bags(bags_dependencies)
    return total_bags


if __name__ == "__main__":
    target_color = "shiny gold"
    bags = solve_the_task(filename="input_data.txt", target_color=target_color)
    print(f"{target_color} resides in {bags} bags.")

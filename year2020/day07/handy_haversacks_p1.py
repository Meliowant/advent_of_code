#!/usr/bin/python3
from year2020.day07.conftest import read_bags_from_file, build_dependencies_up


def solve_the_task(filename=None, target_color=None):
    bags, rules_count = read_bags_from_file(filename)

    bags_dependencies = build_dependencies_up(bags, target_color)
    outer_bags = set()
    for bag_list in bags_dependencies:
        for bag in bag_list:
            outer_bags.add(bag)

    return len(outer_bags) - 1  # Except of the bag itself


if __name__ == "__main__":
    target_color = "shiny gold"
    bags = solve_the_task(filename="input_data.txt", target_color=target_color)
    print(f"{target_color} resides in {bags} bags.")

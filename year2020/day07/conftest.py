#!/usr/bin/python3
import re
from collections import namedtuple


Bag = namedtuple("Bag", ["amount", "colour"])


def read_bags_from_file(filename=None):
    collected_bags = {}
    collected_rules = 0
    with open(filename, "r") as f:
        for line in f:
            collected_rules += 1
            line = line.strip()
            bags_from_file = extract_bags(line)
            collected_bags = update_bags(collected_bags, bags_from_file)

    return collected_bags, collected_rules


def extract_bags(line):
    bags_outer_exp = r"(?P<outer>.+) bags contain (?P<inner>.+)"
    bags_inner_exp = r"(?P<amount>\d+) (?P<colour>\D+) bag"
    bags = {}

    outer = re.search(bags_outer_exp, line)

    if outer is not None:
        outer_bag = outer.groupdict().get("outer")
        bags[outer_bag] = {}
        inner = re.findall(bags_inner_exp, outer.groupdict().get("inner"))
        if inner is not None:
            for itm in inner:
                bag = Bag(*itm)
                bags[outer_bag][bag.colour] = int(bag.amount)

    return bags


def update_bags(existing={}, incoming={}):
    for outer, inner in incoming.items():
        if outer not in existing.keys():
            existing[outer] = inner
        else:
            existing[outer].update(inner)
    return existing


def build_dependencies_up(source={}, target=""):
    outer_bags = []
    added_more = True
    for outer, inner in source.items():
        if target in inner.keys():
            outer_bags.append([target, outer])

    while added_more:
        added_more = False
        new_outer = []
        for bag_list in outer_bags:
            last_bag = bag_list[-1]
            last_bag_found = False

            for outer_bag, inner_bags in source.items():
                if last_bag in inner_bags.keys():
                    last_bag_found = True
                    new_list = list(bag_list)
                    new_list.append(outer_bag)
                    new_outer.append(new_list)
                    added_more = True

            if last_bag_found is False:
                new_outer.append(bag_list)

        if new_outer:
            outer_bags = list(new_outer)

    return outer_bags

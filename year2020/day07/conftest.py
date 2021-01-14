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


def build_dependencies_down(source={}, target=""):
    rv = []
    empty_bag = Bag(amount=1, colour="")

    for outer, inners in source.items():
        if outer == target:
            init = [Bag(amount=1, colour=outer)]
            rv.append(init)

    # Detect sub-children
    has_more_children = True
    while has_more_children:
        has_more_children = False
        new_rv = []
        for unique_edge_set in rv:
            last_bag = unique_edge_set[-1]

            if last_bag == empty_bag:
                new_rv.append(unique_edge_set)
                continue

            children_bags = source.get(last_bag.colour, {})
            if len(children_bags) == 0:
                unique_edge_set.append(empty_bag)
                new_rv.append(unique_edge_set)
                continue

            for colour, amount in children_bags.items():
                has_more_children = True
                new_bag_set = unique_edge_set.copy()
                new_bag_set.append(Bag(colour=colour, amount=amount))
                new_rv.append(new_bag_set)

        rv = new_rv.copy() if len(new_rv) > 0 else rv

    new_rv = []
    for unique_edge_set in rv:
        if empty_bag in unique_edge_set:
            empty_bag_idx = unique_edge_set.index(empty_bag)
            unique_edge_set.pop(empty_bag_idx)
        new_rv.append(unique_edge_set)

    return new_rv


def calculate_bags(data=[]):
    """
    Return sum of all bags
    """
    total = 0
    bags = data.copy()
    processed_bags = []
    while len(bags) > 0:
        bags.sort()
        new_bags = []
        processing_bags = []
        for bag_idx in range(len(bags)):
            if bags[bag_idx] in processed_bags:
                continue
            processed_bags.append(bags[bag_idx])
            new_bags.append(bags[bag_idx])
            bag_idx = bag_idx + bags.count(bags[bag_idx])

        for bag_line in new_bags:
            lowest_bags = 1
            bags_amount = [x.amount for x in bag_line]
            for amount in bags_amount:
                lowest_bags *= amount
            total += lowest_bags
            if len(bag_line[:-1]) > 0 and bag_line[:-1] not in processing_bags:
                processing_bags.append(bag_line[:-1])

        bags = processing_bags
    return total - 1  # Exclude the root one

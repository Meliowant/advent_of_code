import pytest

from year2020.conftest import format_name
from year2020.day07.conftest import (
    read_bags_from_file,
    extract_bags,
    update_bags,
    build_dependencies_up,
    build_dependencies_down,
    calculate_bags,
    Bag,
)


def test_read_bags_from_file():
    _, rules = read_bags_from_file(filename="test_data_p1.txt")
    assert rules == 9


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "One bag with 1 bag colour inside",
            "input": "bright white bags contain 1 shiny gold bag.",
            "exp_output": {"bright white": {"shiny gold": 1}},
        },
        {
            "test_name": "One bag with 2 bag colours inside",
            "input": "muted yellow bags contain 2 shiny gold bags, "
            "9 faded blue bags.",
            "exp_output": {"muted yellow": {"shiny gold": 2, "faded blue": 9}},
        },
        {
            "test_name": "One bag with no bags inside",
            "input": "faded blue bags contain no other bags.",
            "exp_output": {"faded blue": {}},
        },
    ],
    ids=format_name,
)
def test_extract_bags(opts):
    bags = extract_bags(opts["input"])
    assert bags == opts["exp_output"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Update registered bags with brand new bags",
            "existing": {"faded blue": {"dark olive": 1}},
            "new": {"vibrant plum": {"faded blue": 5}},
            "expected": {
                "faded blue": {"dark olive": 1},
                "vibrant plum": {"faded blue": 5},
            },
        },
        {
            "test_name": "Update registered bags with existing bag, same "
            "colour other amount",
            "existing": {"faded blue": {"dark olive": 1}},
            "new": {"faded blue": {"dark olive": 5}},
            "expected": {"faded blue": {"dark olive": 5}},
        },
        {
            "test_name": "Update registered bags with existing bag, "
            "other colour",
            "existing": {"faded blue": {"dark olive": 1}},
            "new": {"faded blue": {"dotted black": 5}},
            "expected": {"faded blue": {"dark olive": 1, "dotted black": 5}},
        },
    ],
    ids=format_name,
)
def test_update_bags(opts):
    bags = update_bags(existing=opts["existing"], incoming=opts["new"])
    assert bags == opts["expected"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "One bag in other",
            "incoming": {
                "faded blue": {"dark olive": 1},
                "dark olive": {"dotted black": 1},
            },
            "target": "dotted black",
            "expected": [["dotted black", "dark olive", "faded blue"]],
        },
        {
            "test_name": "One bag in two others",
            "incoming": {
                "muted yellow": {"dotted black": 1},
                "faded blue": {"dark olive": 1},
                "dark olive": {"dotted black": 1},
            },
            "target": "dotted black",
            "expected": [
                ["dotted black", "dark olive", "faded blue"],
                ["dotted black", "muted yellow"],
            ],
        },
        {
            "test_name": "One bag in three others",
            "incoming": {
                "muted yellow": {"dotted black": 1},
                "faded blue": {"dotted black": 1},
                "dark olive": {"faded blue": 2},
                "mulled red": {"faded blue": 1},
                "faded green": {"mulled red": 1},
                "dotted green": {"mulled red": 1},
            },
            "target": "dotted black",
            "expected": [
                ["dotted black", "muted yellow"],
                ["dotted black", "faded blue", "dark olive"],
                ["dotted black", "faded blue", "mulled red", "faded green"],
                ["dotted black", "faded blue", "mulled red", "dotted green"],
            ],
        },
    ],
    ids=format_name,
)
def test_build_dependencies_up(opts):
    dependencies = build_dependencies_up(
        source=opts["incoming"], target=opts["target"]
    )
    assert sorted(dependencies) == sorted(opts["expected"])


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No bags inside",
            "source": {
                "muted yellow": {},
            },
            "target": "muted yellow",
            "expected": [[Bag(1, "muted yellow")]],
        },
        {
            "test_name": "One bag inside, w/o descendants",
            "source": {"muted yellow": {"dotted black": 1}},
            "target": "muted yellow",
            "expected": [[Bag(1, "muted yellow"), Bag(1, "dotted black")]],
        },
        {
            "test_name": "Two bags inside, only second one has descendant",
            "source": {
                "muted yellow": {"faded blue": 1, "dark olive": 1},
                "faded blue": {"dotted black": 1},
                "dark olive": {},
                "dotted black": {},
            },
            "target": "muted yellow",
            "expected": [
                [
                    Bag(1, "muted yellow"),
                    Bag(1, "faded blue"),
                    Bag(1, "dotted black"),
                ],
                [
                    Bag(1, "muted yellow"),
                    Bag(1, "dark olive"),
                ],
            ],
        },
        {
            "test_name": "Two bags inside, both have single descendant",
            "source": {
                "muted yellow": {"faded blue": 2, "dark olive": 3},
                "faded blue": {"chopped green": 3},
                "chopped green": {},
                "dark olive": {"light red": 5},
                "light red": {},
            },
            "target": "muted yellow",
            "expected": [
                [
                    Bag(1, "muted yellow"),
                    Bag(2, "faded blue"),
                    Bag(3, "chopped green"),
                ],
                [
                    Bag(1, "muted yellow"),
                    Bag(3, "dark olive"),
                    Bag(5, "light red"),
                ],
            ],
        },
        {
            "test_name": "Two bags inside, both have few different and one "
            "same descendants",
            "source": {
                "muted yellow": {"faded blue": 2, "dark olive": 3},
                "faded blue": {"chopped green": 3},
                "chopped green": {"dark olive": 4},
                "dark olive": {"light red": 5},
                "light red": {},
            },
            "target": "muted yellow",
            "expected": [
                [
                    Bag(1, "muted yellow"),
                    Bag(2, "faded blue"),
                    Bag(3, "chopped green"),
                    Bag(4, "dark olive"),
                    Bag(5, "light red"),
                ],
                [
                    Bag(1, "muted yellow"),
                    Bag(3, "dark olive"),
                    Bag(5, "light red"),
                ],
            ],
        },
    ],
    ids=format_name,
)
def test_build_dependencies_down(opts):
    dependencies = build_dependencies_down(
        source=opts["source"], target=opts["target"]
    )
    assert sorted(dependencies) == sorted(opts["expected"])


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No children",
            "source": [[Bag(1, "muted yellow")]],
            "expected": 0,
        },
        {
            "test_name": "One bag inside",
            "source": [[Bag(1, "muted yellow"), Bag(1, "dark olive")]],
            "expected": 1,
        },
        {
            "test_name": "Two same bags inside",
            "source": [[Bag(1, "muted yellow"), Bag(2, "dark olive")]],
            "expected": 2,
        },
        {
            "test_name": "Two different bags inside",
            "source": [
                [Bag(1, "muted yellow"), Bag(1, "dark olive")],
                [Bag(1, "muted yellow"), Bag(1, "dark blue")],
            ],
            "expected": 2,
        },
        {
            "test_name": "Two different bags inside, each has multiple bags",
            "source": [
                [
                    Bag(1, "muted yellow"),
                    Bag(1, "dark olive"),
                    Bag(2, "dark red"),
                ],
                [
                    Bag(1, "muted yellow"),
                    Bag(2, "dark blue"),
                    Bag(3, "dark green"),
                ],
            ],
            "expected": 11,
        },
        {
            "test_name": "Two different bags inside, first has child, other - not",
            "source": [
                [Bag(1, "muted yellow"), Bag(1, "dark olive")],
                [
                    Bag(1, "muted yellow"),
                    Bag(1, "dark blue"),
                    Bag(1, "dark green"),
                ],
            ],
            "expected": 3,
        },
    ],
    ids=format_name,
)
def test_calculate_children(opts):
    children_count = calculate_bags(opts["source"])
    assert children_count == opts["expected"]

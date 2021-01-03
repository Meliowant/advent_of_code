import pytest

from year2020.conftest import format_name
from year2020.day07.handy_haversacks_p1 import (
    extract_bags, update_bags, build_dependencies, solve_the_task
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "One bag with 1 bag colour inside",
            "input": "bright white bags contain 1 shiny gold bag.",
            "exp_output": {"bright white": {"shiny gold": 1}}
        },
        {
            "test_name": "One bag with 2 bag colours inside",
            "input":
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "exp_output": {"muted yellow": {"shiny gold": 2, "faded blue": 9}}
        },
        {
            "test_name": "One bag with no bags inside",
            "input": "faded blue bags contain no other bags.",
            "exp_output": {"faded blue": {}}
        }
    ],
    ids=format_name
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
            "expected": {
                "faded blue": {"dark olive": 5},
            },
        },
        {
            "test_name": "Update registered bags with existing bag, "
                         "other colour",
            "existing": {"faded blue": {"dark olive": 1}},
            "new": {"faded blue": {"dotted black": 5}},
            "expected": {
                "faded blue": {"dark olive": 1, "dotted black": 5},
            },
        },
    ],
    ids=format_name
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
                "dark olive": {"dotted black": 1}
            },
            "target": "dotted black",
            "expected": [["dotted black", "dark olive", "faded blue"]],
        },
        {
            "test_name": "One bag in two others",
            "incoming": {
                "muted yellow": {"dotted black": 1},
                "faded blue": {"dark olive": 1},
                "dark olive": {"dotted black": 1}
            },
            "target": "dotted black",
            "expected": [
                ["dotted black", "dark olive", "faded blue"],
                ["dotted black", "muted yellow"]
            ]
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
            ]
        },


    ],
    ids=format_name
)
def test_build_dependencies(opts):
    dependencies = build_dependencies(
        source=opts["incoming"], target=opts["target"]
    )
    assert sorted(dependencies) == sorted(opts["expected"])


def test_solve_the_task():
    assert solve_the_task(
        filename="test_data.txt", target_color="shiny gold"
    ) == 4

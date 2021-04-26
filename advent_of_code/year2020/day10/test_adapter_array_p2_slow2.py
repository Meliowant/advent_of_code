#!/usr/bin/python3
"""
Tests for test_adapter_array_p2_slow2.py

This code is intermediary between test_adapter_array_p2_slow.py and
test_adapter_array_p2.py its main purpose is to keep tests for
adapter_array_p2_slow.py that is another (memory-consuming) version for
solution of the second task on day 10.
"""
from collections import namedtuple
import pytest

from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day10.adapter_array_p2_slow2 import JoltageAdapter


ExpAdapter = namedtuple(
    "ExpAdapter",
    ["value", "previous", "processed", "successful", "next_adapters"],
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "First adapter",
            "value": 0,
            "prev": None,
            "exp": ExpAdapter(
                value=0,
                previous=None,
                processed=False,
                successful=False,
                next_adapters=[],
            ),
        },
        {
            "test_name": "Second adapter",
            "value": 1,
            "prev": JoltageAdapter(value=0),
            "exp": ExpAdapter(
                value=1,
                previous=JoltageAdapter(value=0),
                processed=False,
                successful=False,
                next_adapters=[],
            ),
        },
        {
            "test_name": "Adapter with next_adapters",
            "value": 1,
            "prev": JoltageAdapter(value=0),
            "next_adapters": [2, 3, 4],
            "exp": ExpAdapter(
                value=1,
                previous=JoltageAdapter(value=0),
                processed=False,
                successful=False,
                next_adapters=[
                    JoltageAdapter(value=2, previous=JoltageAdapter(value=1)),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=1)),
                    JoltageAdapter(value=4, previous=JoltageAdapter(value=1)),
                ],
            ),
        },
    ],
    ids=format_name,
)
def test_adapter_creation(opts):
    """
    Check if adapter was created.
    """
    js_inst = JoltageAdapter(value=opts["value"], previous=opts["prev"])
    for adapter in opts.get("next_adapters", []):
        JoltageAdapter(value=adapter, previous=js_inst)
    for attr in ["value", "previous", "processed", "successful"]:
        got = js_inst.__getattribute__(attr)
        expected = opts["exp"].__getattribute__(attr)
        assert got == expected

    if not opts.get("next_adapters"):
        return

    for next_adapter in js_inst.next_adapters:
        assert next_adapter in opts["exp"].next_adapters


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Adapters are equal",
            "ad1": JoltageAdapter(value=1, previous=None),
            "ad2": JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
            "areEqual": True,
        },
        {
            "test_name": "Adapters are not equal",
            "ad1": JoltageAdapter(value=1, previous=None),
            "ad2": JoltageAdapter(value=2, previous=JoltageAdapter(value=0)),
            "areEqual": False,
        },
    ],
    ids=format_name,
)
def test_eq(opts):
    """
    __eq__ was redefined, so we check if it works correctly here
    """
    ret_val = opts["ad1"] == opts["ad2"]
    assert ret_val is opts["areEqual"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "One next adapter",
            "init_adapter": 0,
            "adapters": [1, 4, 5],
            "exp_adapters": [1],
        },
        {
            "test_name": "Two next adapters",
            "init_adapter": 0,
            "adapters": [1, 2, 4, 5],
            "exp_adapters": [1, 2],
        },
        {
            "test_name": "Three (max) next adapter",
            "init_adapter": 0,
            "adapters": [1, 2, 3, 4, 5],
            "exp_adapters": [1, 2, 3],
        },
        {
            "test_name": "No next adapter",
            "init_adapter": 0,
            "adapters": [4, 5],
            "exp_adapters": [],
        },
        {
            "test_name": "This adapter is in the middle of adapters list",
            "init_adapter": 3,
            "adapters": [1, 3, 4, 5],
            "exp_adapters": [4, 5],
        },
        {
            "test_name": "This adapter is in the end of the adapters list",
            "init_adapter": 5,
            "adapters": [1, 4, 5],
            "exp_adapters": [],
        },
        {
            "test_name": "This adapter is in the end of the adapters list",
            "init_adapter": 5,
            "adapters": [7, 4, 5, 10, 6],
            "exp_adapters": [6, 7],
        },
    ],
    ids=format_name,
)
def test_possible_adapters(opts):
    """
    Check extraction of possible adapters
    """
    adapter = JoltageAdapter(value=opts["init_adapter"])
    got_adapters = adapter.possible_adapters(adapters=opts["adapters"])
    assert opts["exp_adapters"] == got_adapters


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": (
                "Single item between start and stop, target not in adapters"
            ),
            "adapters": [1],
            "target": 2,
            "exp": [
                JoltageAdapter(value=0),
                JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
                JoltageAdapter(value=2, previous=JoltageAdapter(value=1)),
            ],
        },
        {
            "test_name": (
                "Single item between start and stop, target in adapters"
            ),
            "adapters": [1, 2],
            "target": 2,
            "exp": [
                JoltageAdapter(value=0),
                JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
                JoltageAdapter(value=2, previous=JoltageAdapter(value=1)),
            ],
        },
        {
            "test_name": (
                "Two items between start and stop, target not in adapters"
            ),
            "adapters": [1, 2],
            "target": 3,
            "exp": [
                JoltageAdapter(value=0),
                JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
                JoltageAdapter(value=2, previous=JoltageAdapter(value=1)),
                JoltageAdapter(value=3, previous=JoltageAdapter(value=2)),
            ],
        },
        {
            "test_name": (
                "Three item between start and stop, target not in adapters"
            ),
            "adapters": [1, 2, 3],
            "target": 4,
            "exp": [
                JoltageAdapter(value=0),
                JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
                JoltageAdapter(value=2, previous=JoltageAdapter(value=1)),
                JoltageAdapter(value=3, previous=JoltageAdapter(value=2)),
                JoltageAdapter(value=4, previous=JoltageAdapter(value=3)),
            ],
        },
        {
            "test_name": (
                "Single item between start and stop (max distance), "
                "target not in adapters"
            ),
            "adapters": [3],
            "target": 4,
            "exp": [
                JoltageAdapter(value=0),
                JoltageAdapter(value=3, previous=JoltageAdapter(value=0)),
                JoltageAdapter(value=4, previous=JoltageAdapter(value=3)),
            ],
        },
        {
            "test_name": (
                "Multiple items between start and stop (unsorted list), "
                "target not in adapters"
            ),
            "adapters": [3, 10, 5, 13, 8],
            "target": 16,
            "exp": [
                JoltageAdapter(value=0),
                JoltageAdapter(value=3, previous=JoltageAdapter(value=0)),
                JoltageAdapter(value=5, previous=JoltageAdapter(value=3)),
                JoltageAdapter(value=8, previous=JoltageAdapter(value=5)),
                JoltageAdapter(value=10, previous=JoltageAdapter(value=8)),
                JoltageAdapter(value=13, previous=JoltageAdapter(value=10)),
                JoltageAdapter(value=16, previous=JoltageAdapter(value=13)),
            ],
        },
    ],
    ids=format_name,
)
def test_longest_path(opts):
    """
    Check if we can create a longest path for all the possible adapters
    """
    adapter = JoltageAdapter(value=0)
    adapter.longest_path = opts["adapters"], opts["target"]
    assert adapter.longest_path == opts["exp"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Top adapter is the previous one",
            "adapters_chain": [1, 2, 3, 4, 5],
            "search_for": 4,
            "search_from": 1,
            "exp": JoltageAdapter(value=4),
        }
    ],
    ids=format_name,
)
def test_find_adapter_in_longest_path(opts):
    """
    Check if we can find adapters in the chain of the nearest adapters.
    """
    init_adapter = JoltageAdapter(value=0)
    init_adapter.longest_path = (
        opts["adapters_chain"],
        opts["adapters_chain"][-1],
    )
    adapter = init_adapter
    while adapter.value != opts["search_from"]:
        adapter = adapter.next_nearest

    found_adapter = adapter.find_adapter_in_longest_path(
        adapter=opts["search_for"]
    )
    assert found_adapter == opts["exp"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Connected to source",
            "adapters": [1],
            "expected_tree": [
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
                ]
            ],
        },
        {
            "test_name": "Connected via intermediate adapter",
            "adapters": [1, 2],
            "expected_tree": [
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
                    JoltageAdapter(value=2, previous=JoltageAdapter(value=1)),
                ],
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=2, previous=JoltageAdapter(value=0)),
                ],
            ],
        },
        {
            "test_name": "Connected via two intermediate adapters",
            "adapters": [1, 2, 3],
            "expected_tree": [
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
                    JoltageAdapter(value=2, previous=JoltageAdapter(value=1)),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=2)),
                ],
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=1, previous=JoltageAdapter(value=0)),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=1)),
                ],
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=2, previous=JoltageAdapter(value=0)),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=2)),
                ],
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=0)),
                ],
            ],
        },
        {
            "test_name": (
                "Connected via two intermediate adapters (longer chain)"
            ),
            "adapters": [3, 6, 7, 8, 10],
            "expected_tree": [
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=0)),
                    JoltageAdapter(value=6, previous=JoltageAdapter(value=3)),
                    JoltageAdapter(value=7, previous=JoltageAdapter(value=6)),
                    JoltageAdapter(value=8, previous=JoltageAdapter(value=7)),
                    JoltageAdapter(value=10, previous=JoltageAdapter(value=8)),
                ],
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=0)),
                    JoltageAdapter(value=6, previous=JoltageAdapter(value=3)),
                    JoltageAdapter(value=7, previous=JoltageAdapter(value=6)),
                    JoltageAdapter(value=10, previous=JoltageAdapter(value=7)),
                ],
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=0)),
                    JoltageAdapter(value=6, previous=JoltageAdapter(value=3)),
                    JoltageAdapter(value=8, previous=JoltageAdapter(value=6)),
                    JoltageAdapter(value=10, previous=JoltageAdapter(value=8)),
                ],
            ],
        },
        {
            "test_name": (
                "Connected via multiple intermediate adapters (single chain)"
            ),
            "adapters": [3, 6, 7, 10, 12],
            "expected_tree": [
                [
                    JoltageAdapter(value=0),
                    JoltageAdapter(value=3, previous=JoltageAdapter(value=0)),
                    JoltageAdapter(value=6, previous=JoltageAdapter(value=3)),
                    JoltageAdapter(value=7, previous=JoltageAdapter(value=6)),
                    JoltageAdapter(value=10, previous=JoltageAdapter(value=7)),
                    JoltageAdapter(
                        value=12, previous=JoltageAdapter(value=10)
                    ),
                ],
            ],
        },
    ],
    ids=format_name,
)
def test_build_adapters_tree(opts):
    """
    Check if our tree was built correctly.
    """
    init_adapter = JoltageAdapter(value=0)
    init_adapter.longest_path = (opts["adapters"], opts["adapters"][-1])
    init_adapter.adapters_tree = opts["adapters"]
    tree = init_adapter.adapters_tree
    assert sorted(tree) == sorted(opts["expected_tree"])

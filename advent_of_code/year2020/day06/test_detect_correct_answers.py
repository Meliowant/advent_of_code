from year2020.conftest import format_name
import pytest

from detect_yes_answers import (
    extract_groups_unique_answers,
    extract_answers,
    solve_the_task,
)


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "No repetitive answers",
            "data": ["abc", "def"],
            "unique_answers": 6,
        },
        {
            "test_name": "One repetitive answer",
            "data": ["abc", "ade"],
            "unique_answers": 5,
        },
        {
            "test_name": "Multiple groups same answer",
            "data": ["a", "a", "a", "a"],
            "unique_answers": 1,
        },
    ],
    ids=format_name,
)
def test_extract_groups_unique_answers(opts):
    res = extract_groups_unique_answers(opts["data"])
    assert len(res) == opts["unique_answers"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Single group, all answers unique",
            "data": [["ab", "cd"]],
            "total_answers": 4,
        },
        {
            "test_name": "Multiple groups, all answers unique",
            "data": [["ab", "cd"], ["ef", "gh"]],
            "total_answers": 8,
        },
        {
            "test_name": "Multiple groups, all answers same",
            "data": [["ab"], ["ab"]],
            "total_answers": 4,
        },
    ],
    ids=format_name,
)
def test_extract_answers(opts):
    res = extract_answers(opts["data"])
    assert res == opts["total_answers"]


def test_overall():
    res = solve_the_task("test.txt")
    assert res == 11

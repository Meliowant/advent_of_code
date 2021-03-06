import pytest

from year2020.day07.handy_haversacks_p2 import solve_the_task
from year2020.conftest import format_name


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Downstep rules for the target bag from "
            "the first example",
            "filename": "test_data_p1.txt",
            "target": "shiny gold",
            "expected_bags": 32,
        },
        {
            "test_name": "Brand new rules for the target bag",
            "filename": "test_data_p2.txt",
            "target": "shiny gold",
            "expected_bags": 126,
        },
        {
            "test_name": "Reddit sample for the target bag",
            "filename": "test_data_p3.txt",
            "target": "shiny gold",
            "expected_bags": 14,
        },
    ],
    ids=format_name,
)
def test_solve_the_task(opts):
    estimated_bags = solve_the_task(
        filename=opts["filename"], target_color=opts["target"]
    )
    assert estimated_bags == opts["expected_bags"]

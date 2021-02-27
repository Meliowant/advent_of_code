import pytest
from advent_of.code.year2020.conftest import format_name
from advent_of.code.year2020.day08.infinity_loop_detector import solve_task

@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Filename is provided",
            "filename": "example1.txt",
        },
        {
            "test_name": "Filename is absent",
            "filename": "",
        }
    ],
    ids=format_name
)
def test_solve_task(opts):
    got_trace, got_acc = solve_task(opts["filename"])
    assert isinstance(got_trace, list)
    assert isinstance(got_acc, int)

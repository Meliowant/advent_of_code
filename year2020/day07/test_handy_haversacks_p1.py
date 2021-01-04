import pytest

from year2020.conftest import format_name
from year2020.day07.handy_haversacks_p1 import solve_the_task


def test_solve_the_task():
    assert (
        solve_the_task(filename="test_data_p1.txt", target_color="shiny gold")
        == 4
    )

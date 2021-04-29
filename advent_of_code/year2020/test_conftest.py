import pytest

from advent_of_code.year2020.conftest import narrow_list, format_name


@pytest.mark.parametrize(
    "opts",
    [{"test_name": "Empty list", "data": [], "exp": []}],
    ids=format_name,
)
def test_narrow_list(opts):
    """
    Check if list of different hierarchy depths narrows correctly.
    """
    got = narrow_list(opts["data"])
    assert got == opts["exp"]

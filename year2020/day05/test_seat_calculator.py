import pytest

from .seat_calculator import locate_seatrow
from conftest import format_name


@pytest.mask.parametrize(
    "opts",
    [
        {
            "test_name": "Single position",
            "rows": "F",
            "low_value": "F",
            "high_value": "B",
            "exp_result": 0
        }
    ],
    ids=format_name
)
def test_locate_seatrow(opts):
    res = locate_seatrow(
        data=opts["rows"],
        low=opts["low_value"],
        high=opts["high_value"]
    )
    assert res == opts["exp_result"]

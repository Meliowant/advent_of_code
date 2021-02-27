import pytest

from .seat_calculator2 import (
    locate_seat,
    calculate_seat_id,
    extract_seat_params,
    detect_my_seat,
)
from year2020.conftest import format_name


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Single position 0",
            "rows": "F",
            "low_value": "F",
            "high_value": "B",
            "exp_result": 0,
        },
        {
            "test_name": "Single position 1",
            "rows": "B",
            "low_value": "F",
            "high_value": "B",
            "exp_result": 1,
        },
        {
            "test_name": "Reference example for row: 44",
            "rows": "FBFBBFF",
            "low_value": "F",
            "high_value": "B",
            "exp_result": 44,
        },
        {
            "test_name": "Reference example for seat: 5",
            "rows": "RLR",
            "low_value": "L",
            "high_value": "R",
            "exp_result": 5,
        },
    ],
    ids=format_name,
)
def test_locate_seat(opts):
    res = locate_seat(
        data=opts["rows"], low=opts["low_value"], high=opts["high_value"]
    )
    assert res == opts["exp_result"]


@pytest.mark.parametrize(
    "opts",
    [
        {"test_name": "unreal seat", "row": 0, "seat": 0, "result": 0},
        {"test_name": "real seat", "row": 1, "seat": 1, "result": 9},
    ],
    ids=format_name,
)
def test_calculate_seat_id(opts):
    res = calculate_seat_id(row=opts["row"], seat=opts["seat"])
    assert res == opts["result"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Reference boarding pass with ID 567",
            "pass": "BFFFBBFRRR",
            "seat_id": (70, 7, 567),
        },
        {
            "test_name": "Reference boarding pass with ID 119",
            "pass": "FFFBBBFRRR",
            "seat_id": (14, 7, 119),
        },
        {
            "test_name": "Reference boarding pass with ID 820",
            "pass": "BBFFBBFRLL",
            "seat_id": (102, 4, 820),
        },
    ],
    ids=format_name,
)
def test_extract_seat_params(opts):
    res = extract_seat_params(data=opts["pass"])
    assert res == opts["seat_id"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "My seat is missing",
            "seats": [1, 2, 4, 5],
            "my_seat": 3,
        },
        {
            "test_name": "My seat is missing",
            "seats": [5, 4, 2, 1],
            "my_seat": 3,
        },
        {
            "test_name": "My seat is missing",
            "seats": [4, 5, 7, 8],
            "my_seat": 6,
        },
    ],
)
def test_detect_my_seat(opts):
    res = detect_my_seat(opts["seats"])
    assert res == opts["my_seat"]

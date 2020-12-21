import pytest

from valid_passport_counter import (
    extract_passports, extract_passport_values, is_valid_passport
)

def format_name(param):
    return param.get("test_name").replace(" ", "_")

def test_extract_passports():
    assert len(list(extract_passports("demo.txt"))) == 2
    assert ["a b c", "a b"] == list(extract_passports("demo.txt"))


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Single value",
            "input": "a:b",
            "output": {"a": "b"}
        },
        {
            "test_name": "Multiple values",
            "input": "a:b c:d",
            "output": {"a": "b", "c": "d"}
        },
        {
            "test_name": "No values",
            "input": "",
            "output": {}
        }
    ],
    ids=format_name
)
def test_extract_passport_values(opts):
    res = extract_passport_values(opts["input"])
    assert len(res.keys()) == len(opts["output"])
    for k, v in opts["output"].items():
        assert res[k] == v


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Valid passport",
            "passport": {"a": "b", "c": "d"},
            "mandatory": ["a"],
            "optional": ["c"],
            "is_valid": True,
        },
        {
            "test_name": "Valid passport, mandatory fields only",
            "passport": {"a": "b", "c": "d"},
            "mandatory": ["a", "c"],
            "optional": [],
            "is_valid": True,
        },
        {
            "test_name": "Valid passport, optional fields are missing",
            "passport": {"a": "b", "c": "d"},
            "mandatory": ["a", "c"],
            "optional": ["d", "e"],
            "is_valid": True,
        },
        {
            "test_name": "Invalid passport, no mandatory fields",
            "passport": {"a": "b", "c": "d"},
            "mandatory": ["b"],
            "optional": [],
            "is_valid": False,
        },
        {
            "test_name": "Unknown fields in passport",
            "passport": {"a": "b", "c": "d"},
            "mandatory": ["a"],
            "optional": [],
            "is_valid": False,
        }
    ],
    ids=format_name
)
def test_is_valid_passport(opts):
    is_valid = is_valid_passport(
        passport=opts["passport"],
        mandatory=opts["mandatory"],
        optional=opts["optional"]
    )
    assert is_valid is opts["is_valid"]

import pytest

from valid_passport_counter_2 import (
    extract_passports,
    extract_passport_values,
    is_valid_passport,
    is_valid_field,
)


def format_name(param):
    return param.get("test_name").replace(" ", "_")


def test_extract_passports():
    assert len(list(extract_passports("demo.txt"))) == 2
    assert ["a b c", "a b"] == list(extract_passports("demo.txt"))


@pytest.mark.parametrize(
    "opts",
    [
        {"test_name": "Single value", "input": "a:b", "output": {"a": "b"}},
        {
            "test_name": "Multiple values",
            "input": "a:b c:d",
            "output": {"a": "b", "c": "d"},
        },
        {"test_name": "No values", "input": "", "output": {}},
    ],
    ids=format_name,
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
        },
    ],
    ids=format_name,
)
def test_is_valid_passport(opts):
    is_valid = is_valid_passport(
        passport=opts["passport"],
        mandatory=opts["mandatory"],
        optional=opts["optional"],
    )
    assert is_valid is opts["is_valid"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Valid BYR: 1920 <= year <= 2002",
            "value": "1920",
            "is_valid": True,
        },
        {
            "test_name": "Invalid BYR: not 4 digits",
            "value": "192",
            "is_valid": False,
        },
        {
            "test_name": "Invalid BYR: year out of range - too low",
            "value": "1919",
            "is_valid": False,
        },
        {
            "test_name": "Invalid BYR: year out of range - too high",
            "value": "2003",
            "is_valid": False,
        },
    ],
    ids=format_name,
)
def test_is_valid_key_byr(opts):
    assert is_valid_field("byr", opts["value"]) is opts["is_valid"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Valid IYR: 2010 <= year <= 2020",
            "value": "2010",
            "is_valid": True,
        },
        {
            "test_name": "Invalid IYR: not 4 digits",
            "value": "192",
            "is_valid": False,
        },
        {
            "test_name": "Invalid IYR: year out of range - too low",
            "value": "2009",
            "is_valid": False,
        },
        {
            "test_name": "Invalid BYR: year out of range - too high",
            "value": "2021",
            "is_valid": False,
        },
    ],
    ids=format_name,
)
def test_is_valid_key_iyr(opts):
    assert is_valid_field("iyr", opts["value"]) is opts["is_valid"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Valid EYR: 2020 <= year <= 2030",
            "value": "2020",
            "is_valid": True,
        },
        {
            "test_name": "Invalid EYR: not 4 digits",
            "value": "192",
            "is_valid": False,
        },
        {
            "test_name": "Invalid EYR: year out of range - too low",
            "value": "2019",
            "is_valid": False,
        },
        {
            "test_name": "Invalid EYR: year out of range - too high",
            "value": "2031",
            "is_valid": False,
        },
    ],
    ids=format_name,
)
def test_is_valid_key_eyr(opts):
    assert is_valid_field("eyr", opts["value"]) is opts["is_valid"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Valid HGT: 150 <= height <= 193 (cms) 150cm",
            "value": "150cm",
            "is_valid": True,
        },
        {
            "test_name": "Valid HGT: 150 <= height <= 193 (cms) 193cm",
            "value": "193cm",
            "is_valid": True,
        },
        {
            "test_name": "Valid HGT: 59 <= height <= 76 (in) 59in",
            "value": "59in",
            "is_valid": True,
        },
        {
            "test_name": "Valid HGT: 59 <= height <= 76 (in) 76in",
            "value": "76in",
            "is_valid": True,
        },
        {
            "test_name": "Invalid HGT: 150 <= height <= 193 (cms) 149cm",
            "value": "149cm",
            "is_valid": False,
        },
        {
            "test_name": "Invalid HGT: 150 <= height <= 193 (cms) 194cm",
            "value": "194cm",
            "is_valid": False,
        },
        {
            "test_name": "Invalid HGT: 59 <= height <= 76 (in) 58in",
            "value": "50in",
            "is_valid": False,
        },
        {
            "test_name": "Invalid HGT: 59 <= height <= 76 (in) 77in",
            "value": "77in",
            "is_valid": False,
        },
        {
            "test_name": "Invalid HGT: bad units",
            "value": "194ms",
            "is_valid": False,
        },
        {
            "test_name": "Invalid HGT: no units",
            "value": "193",
            "is_valid": False,
        },
        {
            "test_name": "Invalid HGT: units only",
            "value": "in",
            "is_valid": False,
        },
    ],
    ids=format_name,
)
def test_is_valid_key_hgt(opts):
    assert is_valid_field("hgt", opts["value"]) is opts["is_valid"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Valid hair color: #000000",
            "value": "#000000",
            "is_valid": True,
        },
        {
            "test_name": "Valid hair color: #ffffff",
            "value": "#ffffff",
            "is_valid": True,
        },
        {
            "test_name": "Invalid hair color: #fffffg",
            "value": "#fffffg",
            "is_valid": False,
        },
        {
            "test_name": "Invalid hair color: #fffg",
            "value": "#fffg",
            "is_valid": False,
        },
        {
            "test_name": "Invalid hair color: #fffffg",
            "value": "fffffg",
            "is_valid": False,
        },
    ],
    ids=format_name,
)
def test_is_valid_key_hcl(opts):
    assert is_valid_field("hcl", opts["value"]) is opts["is_valid"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Eye color: amb",
            "value": "amb",
        },
        {
            "test_name": "Eye color: blu",
            "value": "blu",
        },
        {
            "test_name": "Eye color: brn",
            "value": "brn",
        },
        {
            "test_name": "Eye color: gry",
            "value": "gry",
        },
        {
            "test_name": "Eye color: grn",
            "value": "grn",
        },
        {
            "test_name": "Eye color: hzl",
            "value": "hzl",
        },
        {
            "test_name": "Eye color: oth",
            "value": "oth",
        },
    ],
    ids=format_name,
)
def test_is_valid_key_ecl_valid(opts):
    assert is_valid_field("ecl", opts["value"]) is True


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Eye color: am",
            "value": "am",
        },
        {
            "test_name": "Eye color: b",
            "value": "b",
        },
        {
            "test_name": "Eye color: <empty>",
            "value": "",
        },
        {
            "test_name": "Eye color: xxx",
            "value": "xxx",
        },
        {
            "test_name": "Eye color: green",
            "value": "green",
        },
    ],
    ids=format_name,
)
def test_is_valid_key_hcl_invalid(opts):
    assert is_valid_field("ecl", opts["value"]) is False


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Valid PID: 111111111",
            "value": "111111111",
            "is_valid": True,
        },
        {
            "test_name": "Valid PID: 000000001",
            "value": "000000001",
            "is_valid": True,
        },
        {"test_name": "Invalid PID: <empty>", "value": "", "is_valid": False},
        {
            "test_name": "Invalid PID: no digits",
            "value": "abcdefghi",
            "is_valid": False,
        },
        {
            "test_name": "Invalid PID: too many digits",
            "value": "1234567890",
            "is_valid": False,
        },
        {
            "test_name": "Invalid PID: not enogh digits",
            "value": "12345678",
            "is_valid": False,
        },
    ],
    ids=format_name,
)
def test_is_valid_key_pid(opts):
    assert is_valid_field("pid", opts["value"]) is opts["is_valid"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Valid cid: <empty>",
            "value": "",
        },
        {
            "test_name": "Valid cid: whatever",
            "value": "whatever is here",
        },
    ],
    ids=format_name,
)
def test_valid_key_cid_always_valid(opts):
    assert is_valid_field("cid", opts["value"]) is True

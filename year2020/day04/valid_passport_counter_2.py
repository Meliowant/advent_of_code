#!/usr/bin/python3
import re


def extract_passports(passport_file: str = ""):
    with open(passport_file, "r") as f:
        passport = []
        for line in f:
            line = line.strip("\n")
            if len(line) == 0:
                yield " ".join(passport)
                passport = []
            else:
                passport.append(line)

    if len(passport) > 0:
        yield " ".join(passport)


def extract_passport_values(passport):
    """
    Convert extracted passport into the dictionary of keys and values.
    """
    rv = {}
    fields = passport.split(" ")
    for field in fields:
        if ":" in field:
            field_key, field_value = field.split(":")
            rv[field_key] = field_value
    return rv


def is_valid_passport(
    passport: dict = {}, mandatory: list = [], optional: list = []
):
    if len(passport.keys()) < len(mandatory) or len(mandatory) + len(
        optional
    ) < len(passport.keys()):
        return False
    pass_copy = dict(passport)
    for k in mandatory:
        if k not in passport.keys():
            return False
        else:
            pass_copy.pop(k)

    for k in optional:
        if k in passport.keys():
            pass_copy.pop(k)

    return len(pass_copy) == 0


def validate_fields(passport: dict = {}):
    valid_fields = []
    for k, v in passport.items():
        valid_fields.append(is_valid_field(k, v))
    return all(valid_fields)


def is_valid_field(field: str = "", value: str = ""):
    is_valid = False
    if field == "byr":
        is_valid = byr_is_valid(value)
    elif field == "iyr":
        is_valid = iyr_is_valid(value)
    elif field == "eyr":
        is_valid = eyr_is_valid(value)
    elif field == "hgt":
        is_valid = hgt_is_valid(value)
    elif field == "hcl":
        is_valid = hcl_is_valid(value)
    elif field == "ecl":
        is_valid = ecl_is_valid(value)
    elif field == "pid":
        is_valid = pid_is_valid(value)
    elif field == "cid":
        is_valid = True
    return is_valid


def byr_is_valid(value: str):
    expr = r"^[0-9]{4}$"
    if not re.match(expr, value):
        return False
    return 1920 <= int(value) <= 2002


def iyr_is_valid(value: str):
    expr = r"^[0-9]{4}$"
    if not re.match(expr, value):
        return False
    return 2010 <= int(value) <= 2020


def eyr_is_valid(value: str):
    expr = r"^[0-9]{4}$"
    if not re.match(expr, value):
        return False
    return 2020 <= int(value) <= 2030


def hgt_is_valid(value: str):
    expr = r"^(?P<height>[0-9]{2,3})(?P<units>(in|cm))$"
    matched = re.match(expr, value)
    if not matched:
        return False
    min_value = 150 if matched.groupdict().get("units") == "cm" else 59
    max_value = 193 if matched.groupdict().get("units") == "cm" else 76
    return min_value <= int(matched.groupdict().get("height")) <= max_value


def hcl_is_valid(value: str):
    expr = r"^\#([0-9a-f]{6})$"
    matched = re.match(expr, value)
    return matched is not None


def ecl_is_valid(value: str):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid_is_valid(value: str):
    expr = r"^[0-9]{9}$"
    return re.match(expr, value) is not None


def solve_the_task():
    passport_records = extract_passports(passport_file="passports.txt")
    valid_passports = 0
    passports = 0
    for passport_records in passport_records:
        passports += 1
        passport = extract_passport_values(passport_records)
        valid_pass = is_valid_passport(
            passport,
            mandatory=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
            optional=["cid"],
        )
        if valid_pass and validate_fields(passport):
            valid_passports += 1
    print(
        f"You have {valid_passports} of {passports} valid passports in the file."
    )


if __name__ == "__main__":
    solve_the_task()

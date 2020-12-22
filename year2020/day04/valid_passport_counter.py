#!/usr/bin/python3


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


def is_valid_passport(passport: dict = {}, mandatory: dict = {}, optional: dict = {}):
    if len(passport.keys()) < len(mandatory) or len(mandatory) + len(optional) < len(
        passport.keys()
    ):
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


def solve_the_task():
    passport_records = extract_passports(passport_file="passports.txt")
    valid_passports = 0
    passports = 0
    for passport in passport_records:
        passports += 1
        if is_valid_passport(
            extract_passport_values(passport),
            mandatory=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
            optional=["cid"],
        ):
            valid_passports += 1
    print(f"You have {valid_passports} of {passports} valid passports in the file.")


if __name__ == "__main__":
    solve_the_task()

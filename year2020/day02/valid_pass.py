#!/usr/bin/python3

import re

passline = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<char>.): (?P<phrase>.*)")
total = 0
with open("input.txt", "r") as f:
    line = f.readline()
    valid_passwords = 0
    while line != "":
        total += 1
        matched = re.match(passline, line)
        passwd = matched.groupdict().get("phrase")
        minv = matched.groupdict().get("min")
        maxv = matched.groupdict().get("max")
        charv = matched.groupdict().get("char")

        if matched:
            times = passwd.count(charv)
            if int(minv) <= times <= int(maxv):
                valid_passwords += 1
                print(f"Password {passwd} in line {total} is valid")
            else:
                print(
                    f"Password {passwd} should have {minv}-{maxv} of '{charv}', but has {times}"
                )
        line = f.readline()

print(f"Found {valid_passwords} valid of {total} total passwords.")

#!/usr/bin/python3

import re

passline = re.compile(r'(?P<first>\d+)-(?P<second>\d+) (?P<char>.): (?P<phrase>.*)')
total = 0
with open("input.txt", "r") as f:
    line = f.readline()
    valid_passwords = 0
    while line != "":
        total += 1
        matched = re.match(passline, line)
        passwd = matched.groupdict().get("phrase")
        first = int(matched.groupdict().get("first"))
        second = int(matched.groupdict().get("second"))
        charv = matched.groupdict().get("char")

        if matched:
            times = passwd.count(charv)
            if int(passwd[first-1] == charv) ^ int(passwd[second-1] == charv):
                valid_passwords += 1
        line = f.readline()

print(f"Found {valid_passwords} valid of {total} total passwords.")


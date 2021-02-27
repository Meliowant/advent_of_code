#!/usr/bin/python3


def locate_seat(data="", low="", high=""):
    rv = 0
    for itm in data:
        rv = rv << 1
        rv = rv ^ (0 if itm == low else 1)
    return rv


def calculate_seat_id(row=0, seat=0):
    return row * 8 + seat


def extract_seat_params(data):
    row_data = locate_seat(data[0:7], low="F", high="B")
    seat_data = locate_seat(data[7:], low="L", high="R")
    seat_id = calculate_seat_id(row_data, seat_data)
    return row_data, seat_data, seat_id


def solve_the_task():
    seat_ids = []
    with open("boarding_passes.txt", "r") as passes:
        for record in passes:
            record = record.strip("\n")
            seat_id = extract_seat_params(record)
            seat_ids.append(seat_id)

    print(f"The highest seat ID is '{max(seat_ids)}'.")


if __name__ == "__main__":
    solve_the_task()

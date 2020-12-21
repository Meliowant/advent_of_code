def locate_seatrow(data="", low="", high=""):
    rv = 0
    for itm in data:
        rv = rv << 1
        rv = rv ^ (0 if itm == low else 1)
    return rv


def solve_the_task():
    pass


if __name__ == '__main__':
    solve_the_task()

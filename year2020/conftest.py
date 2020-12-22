def format_name(param):
    return param.get("test_name").replace(" ", "_")


def read_blocks_data(filename, delimiter="\n"):
    data = []
    if not filename:
        return data

    with open(filename, "r") as data_in:
        item_box = []
        for row in data_in:
            if row == delimiter:
                data.append(item_box)
                item_box = []
            else:
                row = row.split("\n")
                item_box.append(row)

    return data


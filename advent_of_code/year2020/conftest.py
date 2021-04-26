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


def narrow_list(items: list = None) -> list:
    """
    Transform a hierarchical list of lists into a narrow one.
    These heirarchies are expected to be in form:
        [[int, [int, [int]]], [int, [int]]].

    Keyword arguments:
        items - a list of lists that must be transformed into a narrow list
    Returns:
        On success - a narroweed list of items like:
            [[int, int, int], [int, int]]
    """
    top_level = items
    while top_level:  # TODO process list until there are any items
        target = []
        for item in top_level:
            # TODO Detect amount of lists inside the item

            # TODO For each list item create a new list, with the non-list
            # items inside it
            # TODO Append existing list item to the new one.
            pass
        top_level = target
    return top_level

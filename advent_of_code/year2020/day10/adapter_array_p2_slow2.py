"""
Second try to get the faster calculation for the possible adapters combination
"""

from advent_of_code.year2020.day10.common import read_data, get_devices_joltage


class JoltageAdapter:
    """
    Describe a single adapter
    """

    def __init__(self, value: int = None, previous: "JoltageAdapter" = None):
        """
        Constructor for a two-directed list
        """
        self.value = value
        self.previous = previous
        self.processed = False
        self.successful = False
        self.next_adapters = []
        self.next_nearest = None
        self.adapters_counter = 1
        if previous:
            previous.next_adapters.append(self)

    def __eq__(self, other):
        """
        Redefine equality function. We treat two jolt adapters as equal if
        their values are equal
        """
        if not isinstance(other, JoltageAdapter):
            return self.value == other
        return self.value == other.value

    def __ne__(self, other):
        """
        Redefine non-equal function.
        """
        if not other:
            return True
        if isinstance(other, JoltageAdapter):
            return self.value != other.value
        return self.value != other

    def __lt__(self, other):
        """
        Redefince less that to use with sorted()
        """
        if isinstance(other, JoltageAdapter):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other

        try:
            other = int(other)
            return self.value < other
        except TypeError as exc:
            raise TypeError("JoltageAdapter or int is expected") from exc
        except ValueError as exc:
            raise ValueError("JoltageAdapter or int is expected") from exc

    def __repr__(self):
        return f"{self.value}"

    def possible_adapters(self, adapters: list = None) -> list:
        """
        Get a list of possbile adapters. Such adapters must be 1 joltage above
        from the current value at least, and 3 joltages above the at most.

        Known arguments:
            adapters - list of integer values, that are joltage adapters.

        Returns:
            On success - a non-empty list of integer values
            On failure - an empty list
        """
        compatible_adapters = []
        if adapters:
            compatible_adapters = [
                x for x in sorted(adapters) if self.value < x <= self.value + 3
            ]
        return compatible_adapters

    def build_longest_path(self, stuff: (list, int)) -> bool:
        """
        Build the path for joltage adapters that includes the most elements
        from the provided list of adapters.
        This part is similar to the solution we got in the first, but, instead
        of list of ints, we use here a list of objects, that will contain next
        possible adapters.

        Known arguments:
            stuff - a tuple of existing adapters and target device's joltage

        Returns:
            On success - True (if we can reach the list with the existing
            adapters)
            On failure - False (if we cannon reach the list with the existing
            set of adapters)
        """
        adapters, target = stuff
        if target not in adapters:
            adapters.append(target)

        adapters.sort()
        adapter = self
        next_adapters = adapter.possible_adapters(adapters)
        while next_adapters:
            nearest_adapter = JoltageAdapter(
                next_adapters[0], previous=adapter
            )
            adapter.next_nearest = nearest_adapter
            adapter = adapter.next_nearest
            next_adapters = adapter.possible_adapters(adapters)

        return adapter.value == target

    def get_longest_path(self):
        """
        Getter for longest path of adapters
        """
        path = []
        ad = self
        while ad:
            path.append(ad)
            ad = ad.next_nearest

        return path

    longest_path = property(get_longest_path, build_longest_path)

    def find_adapter_in_longest_path(self, adapter: int = None):
        """
        Find Joltage Adapter with `adapter` input voltage in the longest list
        of nearest adapters
        """
        if self.value == adapter:
            return self
        return self.next_nearest.find_adapter_in_longest_path(adapter)

    def build_adapters_tree(self, adapters: list = None) -> list:
        """
        Build a tree of adapters, from the current adapter to the target one.

        Returns:
            A list of JoltageAdapters
        """
        tail = self
        while tail.next_nearest:
            tail = tail.next_nearest

        curr_adapter = tail
        while curr_adapter != self:
            curr_adapter = curr_adapter.previous
            for value in curr_adapter.possible_adapters(adapters):
                adapter = curr_adapter.find_adapter_in_longest_path(value)
                if adapter and adapter not in curr_adapter.next_adapters:
                    curr_adapter.next_adapters.append(adapter)

    def get_adapters_tree(self, depth: int = 0):
        """
        Getter for adapters_tree property. Retrieves a list of nearest adapters
        and returns each possible path to the final adapter as a list Joltage
        adapters.
        """
        final = []
        if not self.next_adapters:
            return [self]
        for adapter in self.next_adapters:
            curr = [self]
            # TODO Doesn't work for 0->1->2->3 and 0->1->3 (check why)
            curr.extend(adapter.get_adapters_tree(depth + 1))
            final.append(curr)
            # if depth > 0:  # TODO make nice list of lists
        return final

    def format_adapters_tree(self):
        """
        Transform a list of inherited lists into a narrow list
        """
        changed = True
        tree = self.get_adapters_tree()
        final_list = []
        while changed:
            # import pdb;pdb.set_trace()
            changed = False
            while tree:
                second_lvl_item = tree.pop(0)
                # for second_lvl_item in tree:
                # tree.remove(second_lvl_item)
                total_items = sum(
                    [1 for itm in second_lvl_item if isinstance(itm, list)]
                )
                if not any([isinstance(x, list) for x in second_lvl_item]):
                    final_list.append(second_lvl_item)
                    continue

                arrays = []
                for _ in range(total_items):
                    # Fill each array where the lists will be put
                    arr = []
                    for itm in second_lvl_item:
                        if isinstance(itm, list):
                            break
                        arr.append(itm)
                    arrays.extend([arr])
                list_start = 0
                for _ in second_lvl_item:
                    if isinstance(_, list):
                        break
                    list_start += 1

                remained_items = second_lvl_item[list_start:]
                for idx, value in enumerate(remained_items):
                    arrays[idx].extend(value)
                for array in arrays:
                    tree.append(array)
                changed = True

        return final_list

    adapters_tree = property(format_adapters_tree, build_adapters_tree)


def solve_the_task(file_name: str = None):
    """
    This is the main processing unit
    """
    adapters = read_data(file_name)
    target_adapter = get_devices_joltage(adapters)
    adapters.append(target_adapter)
    initial = JoltageAdapter(value=0, previous=None)
    initial.longest_path = (adapters, target_adapter)
    initial.adapters_tree = adapters
    return initial.adapters_tree


if __name__ == "__main__":
    total_paths = solve_the_task(file_name="test_input.txt")
    print(f"Total amount of solutions: '{len(total_paths)}'")

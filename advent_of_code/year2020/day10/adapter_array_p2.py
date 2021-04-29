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
        if (
            previous
            and isinstance(previous, JoltageAdapter)
            and self not in previous.next_adapters
        ):
            previous.next_adapters.append(self)
        self.next_adapters = []
        self.next_nearest = None
        self.possible_paths = 0

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
        Redefine less that to use with sorted()
        """
        if not other:
            raise ValueError("Second argument is missing")
        if isinstance(other, JoltageAdapter):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        try:
            other_value = int(other)
            return self.value < other_value
        except TypeError as e:
            raise TypeError(
                "Second argument is expected to be an instance of "
                f"JoltageAdapter or int. Provided type is {type(other)}"
            ) from e

    def __repr__(self):

        if self.next_adapters:
            next_adapters = sorted([x.value for x in self.next_adapters])
            str_next_adapters = ", ".join([str(x) for x in next_adapters])
        else:
            str_next_adapters = ""
        str_next_adapters = f"[{str_next_adapters}]"

        return (
            "<JoltageAdapter("
            f"value='{self.value}', "
            f"previous='{self.previous.value if self.previous else None}', "
            f"next_nearest='{self.next_nearest}', "
            f"possible_paths='{self.possible_paths}', "
            f"next_adapters='{str_next_adapters}')>"
        )

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
            adapter = JoltageAdapter(next_adapters[0], previous=adapter)
            adapter.previous.next_nearest = adapter
            next_adapters = adapter.possible_adapters(adapters)

        return adapter.value == target

    def get_longest_path(self):
        """
        Getter for longest path of adapters
        """
        path = []
        adapter = self
        while adapter:
            path.append(adapter)
            adapter = adapter.next_nearest

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

    def get_paths_amount(self, adapters: list = None):
        """
        Calculate amount of possible paths for given adapters
        """
        assert adapters
        target = self
        while target.next_nearest:
            target = target.next_nearest

        target.possible_paths = 1  # This is final point

        while target.previous:
            target = target.previous
            next_adapters = target.possible_adapters(adapters)
            adapter_paths = []
            for adapter_value in next_adapters:
                next_adapter = target.next_nearest
                while next_adapter:
                    if next_adapter.value == adapter_value:
                        break
                    next_adapter = next_adapter.next_nearest
                if next_adapter.value == adapter_value:
                    adapter_paths.append(next_adapter.possible_paths)

            if target.possible_paths == 0:
                target.possible_paths = sum(adapter_paths)

        retval = self.possible_paths

        return retval


def solve_the_task(file_name: str = None):
    """
    This is the main processing unit
    """
    adapters = read_data(file_name)
    target_adapter = get_devices_joltage(adapters)
    adapters.append(target_adapter)
    initial = JoltageAdapter(value=0, previous=None)
    initial.longest_path = (adapters, target_adapter)
    amount = initial.get_paths_amount(adapters)
    return amount


if __name__ == "__main__":
    total_paths = solve_the_task(file_name="test_input.txt")
    print(f"Total amount of solutions: '{total_paths}'")

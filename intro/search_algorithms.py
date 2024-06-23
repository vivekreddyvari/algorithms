from dataclasses import dataclass
from typing import List

@dataclass
class BinarySearch:
    elements: List
    item: int

    def binary_search(self):
        low = 0
        high = len(self.elements) - 1

        while low <= high:
            mid = (low + high)
            guess = self.elements[mid]
            if guess == self.item:
                return mid
            if guess > self.item:
                high = mid - 1
            else:
                low = mid + 1
        return None


if __name__ == "__main__":
    my_list = [1, 3, 7, 10, 12]

    BINARYSEARCH_test1 = BinarySearch(elements=my_list, item=3)
    BINARYSEARCH_test2 = BinarySearch(elements=my_list, item=13)

    assert BINARYSEARCH_test1.binary_search() == 1, "Element search failed"
    assert BINARYSEARCH_test2.binary_search() is None, "Element search failed"

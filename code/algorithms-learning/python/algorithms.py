from typing import Any


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
def linear_search(array: list[Any], searched_item: Any) -> int:
    for item_index, item in enumerate(array):
        if item == searched_item:
            return item_index

    return -1


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
def binary_search(array: list[Any], searched_item: Any) -> int:
    lowBoundary = 0
    hightBoundary = len(array) - 1

    while lowBoundary <= hightBoundary:
        middle = (lowBoundary + hightBoundary) // 2

        if array[middle] == searched_item:
            return middle
        elif array[middle] < searched_item:
            lowBoundary = middle + 1
        else:
            hightBoundary = middle - 1

    return -1
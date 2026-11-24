from typing import Any


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class CircularQueue:
    def __init__(self, queue_capacity: int):
        if queue_capacity <= 0:
            raise ValueError(f"ERROR: Couldn't initialize a queue due to invalid queue capacity {queue_capacity}")

        self.queue_capacity = queue_capacity
        self.start = 0
        self.size = 0
        self.items = [None] * queue_capacity


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def _isQueueEmpty(self) -> bool:
        return self.size == 0


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def _isQueueFull(self) -> bool:
        return self.size == self.queue_capacity


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def enqueue(self, new_item: Any) -> None:
        if self._isQueueFull():
            raise RuntimeError(f"ERROR: Couldn't enqueue item {new_item} because the queue is full")

        if self.start + self.size >= self.queue_capacity:
            new_item_index = self.start + self.size - self.queue_capacity
        else:
            new_item_index = self.start + self.size

        self.items[new_item_index] = new_item
        self.size += 1


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def dequeue(self) -> Any:
        if self._isQueueEmpty():
            raise RuntimeError(f"ERROR: Couldn't dequeue because the queue is empty")

        removed_item = self.items[self.start]
        self.items[self.start] = None

        if self.start + 1 == self.queue_capacity:
            new_start = 0
        else:
            new_start = self.start + 1

        self.start = new_start
        self.size -= 1
        return removed_item

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def printQueue(self) -> None:
        if self._isQueueEmpty():
            print("The queue is empty")
            return

        print("CircularQueue contents:")

        for i in range(self.size):
            item_index = (self.start + i) % self.queue_capacity
            print(f"{item_index}: {self.items[item_index]}")
        

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def linear_search(array: list[Any], searched_item: Any) -> int:
    for item_index, item in enumerate(array):
        if item == searched_item:
            return item_index

    return -1


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def binary_search(array: list[Any], searched_item: Any) -> int:
    low_boundary = 0
    high_boundary = len(array) - 1

    while low_boundary <= high_boundary:
        middle = (low_boundary + high_boundary) // 2

        if array[middle] == searched_item:
            return middle
        elif array[middle] < searched_item:
            low_boundary = middle + 1
        else:
            high_boundary = middle - 1

    return -1
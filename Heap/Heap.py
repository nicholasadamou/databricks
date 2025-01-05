from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')

class Heap(Generic[T]):
    """
    A min heap data structure.

    :param items: Optional initial list of items to populate the heap.
    :type items: Optional[List[T]]
    """
    def __init__(self, items: Optional[List[T]] = None):
        self._heap: List[T] = []
        if items:
            self.heapify(items)

    def insert(self, item: T) -> None:
        """
        Insert an item into the heap.

        :param item: The item to be inserted into the heap.
        :type item: T
        """
        self._heap.append(item)
        self._sift_up(len(self._heap) - 1)

    def peek(self) -> Optional[T]:
        """
        Get the minimum item from the heap without removing it.

        :return: The minimum item if the heap is not empty, otherwise None.
        :rtype: Optional[T]
        """
        return self._heap[0] if self._heap else None

    def is_empty(self) -> bool:
        """
        Check if the heap is empty.

        :return: True if the heap is empty, otherwise False.
        :rtype: bool
        """
        return not self._heap

    def clear(self) -> None:
        """
        Remove all items from the heap.
        """
        self._heap.clear()

    def pop(self) -> Optional[T]:
        """
        Remove and return the minimum item from the heap.

        :return: The minimum item if the heap is not empty, otherwise None.
        :rtype: Optional[T]
        """
        min_item = self.peek()
        if min_item is not None:
            self._swap(0, len(self._heap) - 1)
            self._heap.pop()
            self._sift_down(0)
        return min_item

    def heapify(self, items: List[T]) -> None:
        """
        Transform a list of items into a heap.

        :param items: The list of items to be transformed into a heap.
        :type items: List[T]
        """
        self._heap = items[:]
        start_index = len(self._heap) // 2 - 1
        for index in range(start_index, -1, -1):
            self._sift_down(index)

    def _sift_up(self, index: int) -> None:
        """
        Sift up the element at the specified index to maintain heap property.

        :param index: The index of the element to sift up.
        :type index: int
        """
        parent_index = (index - 1) // 2
        if index > 0 and self._heap[index] < self._heap[parent_index]:
            self._swap(index, parent_index)
            self._sift_up(parent_index)

    def _sift_down(self, index: int) -> None:
        """
        Sift down the element at the specified index to maintain heap property.

        :param index: The index of the element to sift down.
        :type index: int
        """
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (left_child_index < len(self._heap) and
            self._heap[left_child_index] < self._heap[smallest]):
            smallest = left_child_index

        if (right_child_index < len(self._heap) and
            self._heap[right_child_index] < self._heap[smallest]):
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self._sift_down(smallest)

    def _swap(self, i: int, j: int) -> None:
        """
        Swap the elements at indices i and j in the heap.

        :param i: Index of the first element.
        :type i: int
        :param j: Index of the second element.
        :type j: int
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def __len__(self) -> int:
        """
        Get the number of elements in the heap.

        :return: The number of elements in the heap.
        :rtype: int
        """
        return len(self._heap)

    def __str__(self) -> str:
        """
        Get a string representation of the heap.

        :return: A string representation of the heap.
        :rtype: str
        """
        return f"Heap({self._heap})"

    def __repr__(self) -> str:
        """
        Get a string representation of the heap.

        :return: A string representation of the heap.
        :rtype: str
        """
        return self.__str__()

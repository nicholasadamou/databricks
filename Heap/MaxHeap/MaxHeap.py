from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class MaxHeap(Generic[T]):
    """
    A generic max-heap implementation.

    Attributes:
        _heap (List[T]): The internal list representation of the heap.
    """

    def __init__(self, elements: Optional[List[T]] = None):
        """
        Initialize the heap with optional initial elements.

        :param elements: A list of elements to initialize the heap.
        """
        self._heap = elements or []
        for i in reversed(range(len(self._heap) // 2)):
            self._sift_down(i)

    def insert(self, element: T) -> None:
        """
        Insert an element into the heap.

        :param element: The element to be inserted.
        """
        self._heap.append(element)
        self._sift_up(len(self._heap) - 1)

    def pop(self) -> Optional[T]:
        """
        Remove and return the maximum element from the heap.

        :return: The maximum element, or None if the heap is empty.
        """
        if not self._heap:
            return None
        self._swap(0, len(self._heap) - 1)
        max_element = self._heap.pop()
        self._sift_down(0)
        return max_element

    def peek(self) -> Optional[T]:
        """
        Return the maximum element without removing it.

        :return: The maximum element, or None if the heap is empty.
        """
        return self._heap[0] if self._heap else None

    def clear(self) -> None:
        """
        Remove all elements from the heap.
        """
        self._heap.clear()

    def is_empty(self) -> bool:
        """
        Check if the heap is empty.

        :return: True if the heap is empty, False otherwise.
        """
        return len(self._heap) == 0

    def __len__(self) -> int:
        """
        Return the number of elements in the heap.

        :return: The size of the heap.
        """
        return len(self._heap)

    def _sift_up(self, index: int) -> None:
        """
        Sift up the element at the specified index to maintain heap property.

        :param index: The index of the element to sift up.
        """
        parent_index = (index - 1) // 2
        if index > 0 and self._heap[index] > self._heap[parent_index]:
            self._swap(index, parent_index)
            self._sift_up(parent_index)

    def _sift_down(self, index: int) -> None:
        """
        Sift down the element at the specified index to maintain heap property.

        :param index: The index of the element to sift down.
        """
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (left_child_index < len(self._heap) and
            self._heap[left_child_index] > self._heap[largest]):
            largest = left_child_index

        if (right_child_index < len(self._heap) and
            self._heap[right_child_index] > self._heap[largest]):
            largest = right_child_index

        if largest != index:
            self._swap(index, largest)
            self._sift_down(largest)

    def _swap(self, i: int, j: int) -> None:
        """
        Swap the elements at indices i and j.

        :param i: The first index.
        :param j: The second index.
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

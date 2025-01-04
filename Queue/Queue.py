from typing import Generic, TypeVar, List, Optional, Callable

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self):
        self.queue: List[T] = []

    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        :return: True if the queue is empty, False otherwise
        """
        return len(self.queue) == 0

    def enqueue(self, item: T) -> None:
        """
        Add an item to the queue
        :param item: The item to add
        :return: None
        """
        self.queue.append(item)

    def dequeue(self) -> T:
        """
        Remove an item from the queue
        :return: The item removed
        """
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.queue.pop(0)

    def peek(self) -> T:
        """
        Get the item at the front of the queue
        :return: The item at the front of the queue
        """
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.queue[0]

    def size(self) -> int:
        """
        Get the size of the queue
        :return: The size of the queue
        """
        return len(self.queue)

    def sort(self, key: Optional[Callable[[T], any]] = None, reverse: bool = False) -> None:
        """
        Sort the queue in place.
        :param key: A function that serves as a key for the sort comparison.
        :param reverse: If True, the list elements are sorted as if each comparison were reversed.
        :return: None
        """
        self.queue.sort(key=key, reverse=reverse)

    def get_items(self) -> List[T]:
        """
        Get the list of items in the queue.
        :return: A list of items in the queue.
        """
        return self.queue

    def __str__(self) -> str:
        return str(self.queue)

    def __repr__(self) -> str:
        return str(self.queue)


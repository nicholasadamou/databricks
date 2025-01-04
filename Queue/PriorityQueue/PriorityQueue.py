from typing import Generic, TypeVar, Tuple
from Queue.Queue import Queue

T = TypeVar("T")

class PriorityQueue(Generic[T]):
    def __init__(self):
        self.queue: Queue[Tuple[int, T]] = Queue()

    def enqueue(self, item: T, priority: int) -> None:
        """
        Add an item to the queue with a priority
        :param item: The item to add
        :param priority: The priority of the item
        :return: None
        """
        self.queue.enqueue((priority, item))
        self.queue.sort(key=lambda x: x[0])

    def dequeue(self) -> T:
        """
        Remove an item from the queue
        :return: The item removed
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        return self.queue.dequeue()[1]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        :return: True if the queue is empty, False otherwise
        """
        return self.queue.size() == 0

    def peek(self) -> T:
        """
        Get the item at the front of the queue
        :return: The item at the front of the queue
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")

        return self.queue.peek()[1]

    def size(self) -> int:
        """
        Get the size of the queue
        :return: The size of the queue
        """
        return self.queue.size()

    def __str__(self) -> str:
        return str(self.queue)

    def __repr__(self) -> str:
        return self.__str__()

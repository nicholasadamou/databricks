from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class CircularQueue(Generic[T]):
    def __init__(self, max_size: int):
        self.queue: List[Optional[T]] = [None] * max_size
        self.max_size: int = max_size
        self.front: int = -1
        self.rear: int = -1

    def enqueue(self, item: T) -> None:
        """
        Add an item to the queue
        :param item: The item to add
        :return: None
        """
        if (self.rear + 1) % self.max_size == self.front:
            raise OverflowError("Queue is full")

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size

        self.queue[self.rear] = item

    def dequeue(self) -> T:
        """
        Remove an item from the queue
        :return: The item removed
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size

        return item

    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        :return: True if the queue is empty, False otherwise
        """
        return self.front == -1

    def peek(self) -> T:
        """
        Get the item at the front of the queue
        :return: The item at the front of the queue
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")

        return self.queue[self.front]

    def size(self) -> int:
        """
        Get the size of the queue
        :return: The size of the queue
        """
        if self.is_empty():
            return 0

        if self.rear >= self.front:
            return self.rear - self.front + 1

        return self.max_size - self.front + self.rear + 1

    def __str__(self) -> str:
        return str(self.queue)

    def __repr__(self) -> str:
        return self.__str__()

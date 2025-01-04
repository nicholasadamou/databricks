from typing import TypeVar, Generic, Optional
from LinkedList.DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

T = TypeVar('T')

"""
Why use a Doubly Linked List for a Deque?

A deque is a double-ended queue, which means that we can add and remove items from both the front and rear of the deque.

A doubly linked list is a perfect data structure for a deque because it allows us to easily add and remove items from both
the front and rear of the deque in O(1) time complexity.

Otherwise, if we use a list or a stack to implement a deque, adding and removing items from the front of the deque would
require O(n) time complexity because we would have to shift all the items in the list to the right or left.
"""

class Deque(Generic[T]):
    def __init__(self, items: Optional[list[T]] = None):
        if items is None:
            self.deque = DoublyLinkedList[T]()
            return

        self.deque = DoublyLinkedList[T](items)

    def add_front(self, item: T) -> None:
        """
        Add an item to the front of the deque
        :param item: The item to add
        :return: The deque with the item added
        """
        self.deque.prepend(item)

    def add_rear(self, item: T) -> None:
        """
        Add an item to the rear of the deque
        :param item: The item to add
        :return: The deque with the item added
        """
        self.deque.append(item)

    def remove_front(self) -> T:
        """
        Remove an item from the front of the deque
        :return: The item removed
        """
        if self.is_empty():
            raise IndexError("Remove from empty deque")

        item = self.deque.head.data
        self.deque.remove(0)
        return item

    def remove_rear(self) -> T:
        """
        Remove an item from the rear of the deque
        :return: The item removed
        """
        if self.is_empty():
            raise IndexError("Remove from empty deque")

        item = self.deque.tail.data
        self.deque.remove(self.size() - 1)
        return item

    def is_empty(self) -> bool:
        """
        Check if the deque is empty
        :return: True if the deque is empty, False otherwise
        """
        return len(self.deque) == 0

    def size(self) -> int:
        """
        Get the size of the deque
        :return: The size of the deque
        """
        return len(self.deque)

    def rotate(self, n: int) -> None:
        """
        Rotate the deque n steps to the right
        :param n: The number of steps to rotate
        :return: The deque rotated n steps to the right
        """
        if self.is_empty():
            return

        n = n % self.size()  # Handle rotations greater than size
        if n == 0:
            return

        for _ in range(n):
            item = self.remove_rear()
            self.add_front(item)

    def peek_front(self) -> T:
        """
        Get the item at the front of the deque
        :return: The item at the front of the deque
        """
        if self.is_empty():
            raise IndexError("Peek from empty deque")

        return self.deque.head.data

    def peek_rear(self) -> T:
        """
        Get the item at the rear of the deque
        :return: The item at the rear of the deque
        """
        if self.is_empty():
            raise IndexError("Peek from empty deque")

        return self.deque.tail.data

    def clear(self) -> None:
        """
        Clear the deque
        """
        self.deque.clear()

    def __str__(self) -> str:
        return str(self.deque)

    def __repr__(self) -> str:
        return str(self.deque)

    def __len__(self) -> int:
        return len(self.deque)

    def __getitem__(self, index: int) -> T:
        dummy = self.deque.head

        for _ in range(index):
            dummy = dummy.next

        return dummy.data

    def __setitem__(self, index: int, item: T) -> None:
        dummy = self.deque.head

        for _ in range(index):
            dummy = dummy.next

        dummy.data = item

from typing import Generic, TypeVar, List

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self.stack: List[T] = []

    def push(self, item: T) -> None:
        """
        Pushes an item to the stack
        :param item: The item to be pushed
        :return: None
        """
        self.stack.append(item)

    def pop(self) -> T:
        """
        Pops an item from the stack
        :return: The popped item
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")

        return self.stack.pop()

    def peek(self) -> T:
        """
        Returns the top element of the stack
        :return: The top element of the stack
        """
        if self.is_empty():
            raise IndexError("top from empty stack")

        return self.stack[-1]

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty
        :return: True if the stack is empty, False otherwise
        """
        return len(self.stack) == 0

    def size(self) -> int:
        """
        Returns the size of the stack
        :return: The size of the stack
        """
        return len(self.stack)

    def sort(self, descending: bool = False) -> None:
        """
        Sorts the stack in ascending or descending order
        :param descending: True if the stack is to be sorted in descending order, False otherwise
        :return: None
        """
        if self.is_empty():
            return

        value = self.pop()
        self.sort(descending)
        self._insert(value, descending)

    def _insert(self, value: T, descending: bool) -> None:
        """
        Inserts an element into the stack in the correct position
        :param value: The element to be inserted
        :param descending: True if the stack is to be sorted in descending order, False otherwise
        :return: None
        """
        if self.is_empty() or (descending and self.peek() > value) or (not descending and self.peek() < value):
            self.push(value)
            return

        top = self.pop()
        self._insert(value, descending)
        self.push(top)

    def reverse(self) -> None:
        """
        Reverses the stack
        :return: None
        """
        if self.is_empty():
            return

        value = self.pop()
        self.reverse()
        self._insert_at_bottom(value)

    def _insert_at_bottom(self, value: T) -> None:
        """
        Inserts an element at the bottom of the stack
        :param value: The element to be inserted
        :return: None
        """
        if self.is_empty():
            self.push(value)
            return

        top = self.pop()
        self._insert_at_bottom(value)
        self.push(top)

    def __str__(self) -> str:
        return str(self.stack)

    def __repr__(self) -> str:
        return str(self.stack)

    def __reversed__(self):
        self.reverse()
        return self


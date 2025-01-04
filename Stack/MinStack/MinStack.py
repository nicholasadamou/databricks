from typing import Generic, TypeVar
from Stack.Stack import Stack

T = TypeVar('T')

class MinStack(Stack, Generic[T]):
    def __init__(self):
        super().__init__()

        self.stack = Stack[T]()
        self.min_stack = Stack[T]()

    def push(self, x: T) -> None:
        """
        Pushes an element to the stack
        :param x: The element to be pushed
        :return: None
        """
        self.stack.push(x)

        if self.min_stack.is_empty() or x <= self.min_stack.peek():
            self.min_stack.push(x)

    def pop(self) -> T:
        """
        Pops an element from the stack
        :return: The popped element
        """
        if self.stack.is_empty():
            raise IndexError("pop from empty stack")

        value = self.stack.pop()

        if not self.min_stack.is_empty() and value == self.min_stack.peek():
            self.min_stack.pop()

        return value

    def top(self) -> T:
        """
        Returns the top element of the stack
        :return: The top element of the stack
        """
        if self.stack.is_empty():
            raise IndexError("top from empty stack")

        return self.stack.peek()

    def min(self) -> T:
        """
        Returns the minimum element in the stack
        :return: The minimum element in the stack
        """
        if self.min_stack.is_empty():
            raise IndexError("Stack is empty")

        return self.min_stack.peek()

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty
        :return: True if the stack is empty, False otherwise
        """
        return self.stack.is_empty() and self.min_stack.is_empty()

    def size(self) -> int:
        """
        Returns the size of the stack
        :return: The size of the stack
        """
        return self.stack.size()

    def __str__(self):
        return str(self.stack) + " Min: " + str(self.min_stack)

    def __repr__(self):
        return self.__str__()

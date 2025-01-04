from Stack.Stack import Stack

from typing import Generic, TypeVar

T = TypeVar("T")

"""
Why Use Two Stacks to Implement a Queue?

The main idea of using two stacks to implement a queue is to leverage the LIFO (Last In, First Out) nature of stacks to achieve the FIFO (First In, First Out) behavior of queues. We will have: a main stack and a temporary stack. The main stack stores all the queue elements, whereas the temporary stack is a temporary buffer to provide queue functionality. Here's how it works:

1. Enqueue Operation:
In every enqueue() operation, we first transfer all the elements from the main stack to the temporary stack and then push the new value to the empty main stack so that the newly inserted value is at the bottom of the main stack. Then, we transfer all the elements from the temporary stack to the main stack, reversing the order of the values in the main stack.

   - Simply push the element onto the main_stack. This operation is efficient and straightforward, with a time complexity of O(1).

2. Dequeue Operation:
The dequeue() operation is very efficient since the main stack is already reversed. Therefore, we just pop the oldest value from the top of the main stack.

   - When you need to dequeue an element, if the temp_stack is empty, move all elements from the main_stack to the temp_stack. This reverses the order of the elements, so the oldest element (the one that was enqueued first) ends up on the top of the temp_stack.
   - Pop the top element from the temp_stack, which will be the front of the queue.
   - If the temp_stack is not empty, simply pop from it.

Time Complexity

-  Enqueue: The time complexity is O(1) because you are just pushing an element onto the main_stack.

-  Dequeue:
  - The worst-case time complexity is O(n) when you need to move all elements from main_stack to temp_stack. This happens only when temp_stack is empty.
  - However, the amortized time complexity of the dequeue operation is O(1). This is because each element is moved from main_stack to temp_stack only once, and each element is popped from temp_stack exactly once. Thus, over a sequence of operations, the average time per operation is constant.

Space Complexity

-  The space complexity is O(n) because you need to store all elements in the two stacks. Each element is stored once, either in the main_stack or the temp_stack.

Comparison with a Queue Implemented Using a List

A Queue implemented using a list has a time complexity of O(n) for the dequeue operation because removing the first element from a list requires shifting all other elements by one position. In contrast, the StackQueue implementation has an amortized time complexity of O(1) for the dequeue operation, making it more efficient.
"""

class StackQueue(Generic[T]):
    def __init__(self):
        self.main_stack: Stack[T] = Stack()
        self.temp_stack: Stack[T] = Stack()

    def enqueue(self, value: T) -> None:
        """
        Inserts the element in the queue
        :param value: The value to be inserted
        :return: None
        """
        self.main_stack.push(value)

    def dequeue(self) -> T:
        """
        Removes the element from the queue
        :return: The element removed
        """
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            raise IndexError("Dequeue from an empty queue")

        if self.temp_stack.is_empty():
            while not self.main_stack.is_empty():
                popped_value = self.main_stack.pop()
                self.temp_stack.push(popped_value)

        return self.temp_stack.pop()

    def peek(self) -> T:
        """
        Returns the element at the front of the queue
        :return: The element at the front of the queue
        """
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            raise IndexError("Peek from an empty queue")

        if self.temp_stack.is_empty():
            while not self.main_stack.is_empty():
                popped_value = self.main_stack.pop()
                self.temp_stack.push(popped_value)

        return self.temp_stack.peek()

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty
        :return: True if the queue is empty, False otherwise
        """
        return self.main_stack.is_empty() and self.temp_stack.is_empty()

    def size(self) -> int:
        """
        Returns the size of the queue
        :return: The size of the queue
        """
        return self.main_stack.size() + self.temp_stack.size()

    def __str__(self) -> str:
        return str(self.temp_stack) + " <- " + str(self.main_stack)

    def __repr__(self) -> str:
        return self.__str__()

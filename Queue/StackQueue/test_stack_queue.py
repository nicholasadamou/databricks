import unittest

from Queue.StackQueue.StackQueue import StackQueue

class TestStackQueue(unittest.TestCase):
    def test_enqueue(self):
        stack_queue = StackQueue()
        stack_queue.enqueue(1)
        stack_queue.enqueue(2)
        stack_queue.enqueue(3)
        # Assuming there's a method to check the size or content of the queue
        self.assertEqual(stack_queue.size(), 3)
        # We may not directly access main_stack in a real test case; instead, verify through public methods

    def test_dequeue(self):
        stack_queue = StackQueue()
        stack_queue.enqueue(1)
        stack_queue.enqueue(2)
        stack_queue.enqueue(3)
        self.assertEqual(stack_queue.dequeue(), 1)
        self.assertEqual(stack_queue.dequeue(), 2)
        self.assertEqual(stack_queue.dequeue(), 3)
        # Test for exception when dequeuing from an empty queue
        with self.assertRaises(IndexError):
            stack_queue.dequeue()

    def test_peek(self):
        stack_queue = StackQueue()
        stack_queue.enqueue(1)
        stack_queue.enqueue(2)
        stack_queue.enqueue(3)
        self.assertEqual(stack_queue.peek(), 1)
        # Ensure peek does not remove the element
        self.assertEqual(stack_queue.size(), 3)
        # Test for exception when peeking from an empty queue
        stack_queue.dequeue()
        stack_queue.dequeue()
        stack_queue.dequeue()
        with self.assertRaises(IndexError):
            stack_queue.peek()

    def test_is_empty(self):
        stack_queue = StackQueue()
        self.assertTrue(stack_queue.is_empty())
        stack_queue.enqueue(1)
        self.assertFalse(stack_queue.is_empty())
        stack_queue.dequeue()
        self.assertTrue(stack_queue.is_empty())

    def test_size(self):
        stack_queue = StackQueue()
        self.assertEqual(stack_queue.size(), 0)
        stack_queue.enqueue(1)
        self.assertEqual(stack_queue.size(), 1)
        stack_queue.enqueue(2)
        self.assertEqual(stack_queue.size(), 2)
        stack_queue.dequeue()
        self.assertEqual(stack_queue.size(), 1)
        stack_queue.dequeue()
        self.assertEqual(stack_queue.size(), 0)

    def test_dequeue_empty(self):
        stack_queue = StackQueue()
        with self.assertRaises(IndexError):
            stack_queue.dequeue()

    def test_peek_empty(self):
        stack_queue = StackQueue()
        with self.assertRaises(IndexError):
            stack_queue.peek()

if __name__ == '__main__':
    unittest.main()

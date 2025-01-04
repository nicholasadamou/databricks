import unittest

from Queue.CircularQueue.CircularQueue import CircularQueue

class TestCircularQueue(unittest.TestCase):
    def setUp(self):
        # Set up a CircularQueue with a maximum size of 5 for each test
        self.queue = CircularQueue(5)

    def test_enqueue_dequeue(self):
        # Test basic enqueue and dequeue operations
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_overflow(self):
        # Test overflow condition
        for i in range(5):
            self.queue.enqueue(i)
        with self.assertRaises(OverflowError):
            self.queue.enqueue(5)

    def test_underflow(self):
        # Test underflow condition
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_is_empty(self):
        # Test is_empty method
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

    def test_peek(self):
        # Test peek method
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek(), 1)

    def test_size(self):
        # Test size method
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

    def test_circular_behavior(self):
        # Test circular behavior
        for i in range(5):
            self.queue.enqueue(i)
        self.queue.dequeue()
        self.queue.enqueue(5)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.size(), 5)

if __name__ == '__main__':
    unittest.main()

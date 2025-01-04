import unittest

from Queue.Queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        # Set up a Queue instance for each test
        self.queue = Queue()

    def test_is_empty(self):
        # Test is_empty method
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

    def test_enqueue(self):
        # Test enqueue operation
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.queue, [1, 2])

    def test_dequeue(self):
        # Test dequeue operation
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

        # Test dequeue from an empty queue
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek(self):
        # Test peek method
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek(), 1)

        # Test peek from an empty queue
        self.queue.dequeue()
        self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_size(self):
        # Test size method
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)

    def test_str_repr(self):
        # Test __str__ and __repr__ methods
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), '[1, 2]')
        self.assertEqual(repr(self.queue), '[1, 2]')

if __name__ == '__main__':
    unittest.main()

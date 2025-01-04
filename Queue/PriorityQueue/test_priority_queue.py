import unittest

from Queue.PriorityQueue.PriorityQueue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        # Set up a PriorityQueue instance for each test
        self.priority_queue = PriorityQueue()

    def test_enqueue(self):
        # Test enqueue operation with priorities
        self.priority_queue.enqueue('low', 5)
        self.priority_queue.enqueue('medium', 3)
        self.priority_queue.enqueue('high', 1)
        self.assertEqual(self.priority_queue.queue.get_items(), [(1, 'high'), (3, 'medium'), (5, 'low')])

    def test_dequeue(self):
        # Test dequeue operation
        self.priority_queue.enqueue('low', 5)
        self.priority_queue.enqueue('medium', 3)
        self.priority_queue.enqueue('high', 1)
        self.assertEqual(self.priority_queue.dequeue(), 'high')
        self.assertEqual(self.priority_queue.dequeue(), 'medium')
        self.assertEqual(self.priority_queue.dequeue(), 'low')

        # Test dequeue from an empty queue
        with self.assertRaises(IndexError):
            self.priority_queue.dequeue()

    def test_is_empty(self):
        # Test is_empty method
        self.assertTrue(self.priority_queue.is_empty())
        self.priority_queue.enqueue('item', 1)
        self.assertFalse(self.priority_queue.is_empty())

    def test_peek(self):
        # Test peek method
        self.priority_queue.enqueue('low', 5)
        self.priority_queue.enqueue('medium', 3)
        self.priority_queue.enqueue('high', 1)
        self.assertEqual(self.priority_queue.peek(), 'high')

        # Test peek from an empty queue
        self.priority_queue.dequeue()
        self.priority_queue.dequeue()
        self.priority_queue.dequeue()
        with self.assertRaises(IndexError):
            self.priority_queue.peek()

    def test_size(self):
        # Test size method
        self.assertEqual(self.priority_queue.size(), 0)
        self.priority_queue.enqueue('item1', 1)
        self.priority_queue.enqueue('item2', 2)
        self.assertEqual(self.priority_queue.size(), 2)

    def test_str_repr(self):
        # Test __str__ and __repr__ methods
        self.priority_queue.enqueue('low', 5)
        self.priority_queue.enqueue('medium', 3)
        self.priority_queue.enqueue('high', 1)
        self.assertEqual(str(self.priority_queue), "[(1, 'high'), (3, 'medium'), (5, 'low')]")
        self.assertEqual(repr(self.priority_queue), "[(1, 'high'), (3, 'medium'), (5, 'low')]")

if __name__ == '__main__':
    unittest.main()

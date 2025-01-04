import unittest

from Queue.Deque.Deque import Deque

class TestDeque(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_add_front(self):
        self.deque.add_front(1)
        self.deque.add_front(2)
        self.assertEqual(list(self.deque.deque), [2, 1])

    def test_add_rear(self):
        self.deque.add_rear(1)
        self.deque.add_rear(2)
        self.assertEqual(list(self.deque.deque), [1, 2])

    def test_remove_front(self):
        self.deque.add_front(1)
        self.deque.add_front(2)
        self.assertEqual(self.deque.remove_front(), 2)
        self.assertEqual(list(self.deque.deque), [1])

        self.deque.remove_front()
        with self.assertRaises(IndexError):
            self.deque.remove_front()

    def test_remove_rear(self):
        self.deque.add_rear(1)
        self.deque.add_rear(2)
        self.assertEqual(self.deque.remove_rear(), 2)
        self.assertEqual(list(self.deque.deque), [1])

        self.deque.remove_rear()
        with self.assertRaises(IndexError):
            self.deque.remove_rear()

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())
        self.deque.add_front(1)
        self.assertFalse(self.deque.is_empty())

    def test_size(self):
        self.assertEqual(self.deque.size(), 0)
        self.deque.add_front(1)
        self.deque.add_rear(2)
        self.assertEqual(self.deque.size(), 2)

    def test_rotate(self):
        self.deque.add_front(1)
        self.deque.add_rear(2)
        self.deque.rotate(1)
        self.assertEqual(list(self.deque.deque), [2, 1])

    def test_rotate_empty(self):
        self.deque.rotate(1)
        self.assertEqual(list(self.deque.deque), [])

    def test_peek_front(self):
        self.deque.add_front(1)
        self.deque.add_rear(2)
        self.assertEqual(self.deque.peek_front(), 1)

    def test_peek_rear(self):
        self.deque.add_front(1)
        self.deque.add_rear(2)
        self.assertEqual(self.deque.peek_rear(), 2)

    def test_clear(self):
        self.deque.add_front(1)
        self.deque.add_rear(2)
        self.deque.clear()
        self.assertEqual(list(self.deque.deque), [])

    def test_str_repr(self):
        self.deque.add_front(1)
        self.deque.add_rear(2)
        self.assertEqual(str(self.deque), '[1, 2]')
        self.assertEqual(repr(self.deque), '[1, 2]')

if __name__ == '__main__':
    unittest.main()

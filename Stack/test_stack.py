import unittest

from Stack.Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_increases_size(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.stack, [1, 2, 3])

    def test_pop_decreases_size_and_returns_correct_element(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_on_empty_stack_raises_exception(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_returns_last_element_without_removing_it(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.size(), 3)  # Ensure size hasn't changed

    def test_peek_on_empty_stack_raises_exception(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_is_empty_returns_true_on_new_stack(self):
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_returns_false_after_push(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_size_returns_correct_number_of_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)

    def test_sort_sorts_stack_in_ascending_order(self):
        self.stack.push(3)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.sort()
        self.assertEqual(self.stack.stack, [1, 2, 3])

    def test_sort_sorts_stack_in_descending_order(self):
        self.stack.push(3)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.sort(descending=True)
        self.assertEqual(self.stack.stack, [3, 2, 1])

    def test_sort_on_empty_stack_does_nothing(self):
        self.stack.sort()
        self.assertEqual(self.stack.stack, [])

    def test_reverse_reverses_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.reverse()
        self.assertEqual(self.stack.stack, [3, 2, 1])

    def test_reverse_on_empty_stack_does_nothing(self):
        self.stack.reverse()
        self.assertEqual(self.stack.stack, [])

    def test_reverse_on_single_element_stack_does_nothing(self):
        self.stack.push(1)
        self.stack.reverse()
        self.assertEqual(self.stack.stack, [1])

    def test_reverse_on_two_element_stack_reverses_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.reverse()
        self.assertEqual(self.stack.stack, [2, 1])

if __name__ == '__main__':
    unittest.main()

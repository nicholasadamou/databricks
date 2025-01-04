import unittest

from Stack.MinStack.MinStack import MinStack

class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.min(), -3)
        self.assertEqual(min_stack.pop(), -3)
        self.assertEqual(min_stack.top(), 0)
        self.assertEqual(min_stack.min(), -2)

    def test_min_stack_empty(self):
        min_stack = MinStack()
        with self.assertRaises(IndexError):
            min_stack.min()

    def test_min_stack_empty_pop(self):
        min_stack = MinStack()
        with self.assertRaises(IndexError):
            min_stack.pop()

    def test_min_stack_empty_top(self):
        min_stack = MinStack()
        with self.assertRaises(IndexError):
            min_stack.top()

if __name__ == '__main__':
    unittest.main()

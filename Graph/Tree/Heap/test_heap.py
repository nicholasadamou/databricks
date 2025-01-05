import unittest

from Graph.Tree.Heap.Heap import Heap

class TestHeap(unittest.TestCase):
    def test_heapify(self):
        items = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        expected_sorted = sorted(items)

        heap = Heap[int](items)

        sorted_items = []
        while not heap.is_empty():
            sorted_items.append(heap.pop())

        self.assertEqual(sorted_items, expected_sorted)

    def test_peek(self):
        heap = Heap[int]()
        self.assertIsNone(heap.peek())

        heap.insert(10)
        heap.insert(5)

        self.assertEqual(heap.peek(), 5)
        self.assertEqual(len(heap), 2)  # Ensure peek does not remove the item

    def test_clear(self):
        heap = Heap[int]([1, 2, 3])
        heap.clear()
        self.assertTrue(heap.is_empty())
        self.assertEqual(len(heap), 0)

if __name__ == '__main__':
    unittest.main()

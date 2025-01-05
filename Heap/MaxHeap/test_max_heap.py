import unittest
from Heap.MaxHeap.MaxHeap import MaxHeap

class TestMaxHeap(unittest.TestCase):
    def test_insert_and_extract_max(self):
        max_heap = MaxHeap[int]()
        max_heap.insert(3)
        max_heap.insert(1)
        max_heap.insert(2)

        self.assertEqual(max_heap.pop(), 3)
        self.assertEqual(max_heap.pop(), 2)
        self.assertEqual(max_heap.pop(), 1)
        self.assertEqual(max_heap.pop(), None)  # MaxHeap should be empty now

    def test_heapify(self):
        items = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        expected_sorted = sorted(items, reverse=True)

        max_heap = MaxHeap[int](items)

        sorted_items = []
        while not max_heap.is_empty():
            sorted_items.append(max_heap.pop())

        self.assertEqual(sorted_items, expected_sorted)

    def test_peek(self):
        max_heap = MaxHeap[int]()
        self.assertIsNone(max_heap.peek())

        max_heap.insert(10)
        max_heap.insert(5)

        self.assertEqual(max_heap.peek(), 10)
        self.assertEqual(len(max_heap), 2)  # Ensure peek does not remove the item

    def test_clear(self):
        max_heap = MaxHeap[int]([1, 2, 3])
        max_heap.clear()
        self.assertTrue(max_heap.is_empty())
        self.assertEqual(len(max_heap), 0)

if __name__ == '__main__':
    unittest.main()

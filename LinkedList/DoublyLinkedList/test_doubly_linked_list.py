import unittest

from LinkedList.DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

class TestDoubleLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_append_single_element(self):
        """Test appending a single element."""
        self.dll.append(1)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)

    def test_append_multiple_elements(self):
        """Test appending multiple elements."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(len(self.dll), 3)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 3)

    def test_prepend_single_element(self):
        """Test prepending a single element."""
        self.dll.prepend(1)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)

    def test_prepend_multiple_elements(self):
        """Test prepending multiple elements."""
        self.dll.prepend(1)
        self.dll.prepend(2)
        self.dll.prepend(3)
        self.assertEqual(len(self.dll), 3)
        self.assertEqual(self.dll.head.data, 3)
        self.assertEqual(self.dll.tail.data, 1)

    def test_insert_middle(self):
        """Test inserting element in the middle."""
        self.dll.append(1)
        self.dll.append(3)
        self.dll.insert(1, 2)
        self.assertEqual(len(self.dll), 3)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 3)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.prev.data, 2)

    def test_delete_middle(self):
        """Test deleting a middle element."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.remove(1)
        self.assertEqual(len(self.dll), 2)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 3)
        self.assertEqual(self.dll.head.next.data, 3)
        self.assertEqual(self.dll.tail.prev.data, 1)

    def test_delete_head(self):
        """Test deleting the head element."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.remove(0)
        self.assertEqual(len(self.dll), 2)
        self.assertEqual(self.dll.head.data, 2)
        self.assertEqual(self.dll.tail.data, 3)

    def test_delete_tail(self):
        """Test deleting the tail element."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.remove(2)
        self.assertEqual(len(self.dll), 2)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 2)

    def test_delete_empty(self):
        """Test deleting from an empty list."""
        with self.assertRaises(IndexError):
            self.dll.remove(0)

    def test_delete_out_of_bounds(self):
        """Test deleting with an out-of-bounds index."""
        self.dll.append(1)
        with self.assertRaises(IndexError):
            self.dll.remove(1)

    def test_delete_negative_index(self):
        """Test deleting with a negative index."""
        self.dll.append(1)
        with self.assertRaises(IndexError):
            self.dll.remove(-1)

    def test_delete_index_zero(self):
        """Test deleting the only element."""
        self.dll.append(1)
        self.dll.remove(0)
        self.assertEqual(len(self.dll), 0)
        self.assertEqual(self.dll.head, None)
        self.assertEqual(self.dll.tail, None)

if __name__ == '__main__':
    unittest.main()

import unittest

from LinkedList.SinglyLinkedList.SinglyLinkedList import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def assert_linked_list(self, singly_linked_list, expected_values):
        current = singly_linked_list.head

        for value in expected_values:
            self.assertIsNotNone(current)
            self.assertEqual(str(current), str(value))
            current = current.next

        self.assertIsNone(current)

    def test_add_at_head(self):
        singly_linked_list = SinglyLinkedList()
        values_to_add = [1, 2, 3, 4, 5]
        for value in values_to_add:
            singly_linked_list.add_at_head(value)
        self.assert_linked_list(singly_linked_list, reversed(values_to_add))

    def test_add_at_tail(self):
        singly_linked_list = SinglyLinkedList()
        values_to_add = [1, 2, 3, 4, 5]
        for value in values_to_add:
            singly_linked_list.add_at_tail(value)
        self.assert_linked_list(singly_linked_list, values_to_add)

    def test_add_at_index(self):
        singly_linked_list = SinglyLinkedList()
        values_to_add = [1, 2, 3, 4, 5]
        for index, value in enumerate(values_to_add):
            singly_linked_list.add_at_index(index, value)
        self.assert_linked_list(singly_linked_list, values_to_add)


if __name__ == '__main__':
    unittest.main()

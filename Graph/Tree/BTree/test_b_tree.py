import unittest

from Graph.Tree.BTree.BTree import BTree

class TestBTree(unittest.TestCase):

    def setUp(self):
        """Set up the B-Tree for testing."""
        self.b_tree = BTree[int](3)  # Create a B-Tree with minimum degree t=3

    def test_insert(self):
        """Test insertion of elements into the B-Tree."""
        elements = [10, 20, 5, 6, 12, 30, 7, 17]
        for element in elements:
            self.b_tree.insert(element)

        # Check if the tree structure is as expected
        expected_traversal = [5, 6, 7, 10, 12, 17, 20, 30]
        actual_traversal = self.b_tree.traverse()
        self.assertEqual(expected_traversal, actual_traversal)

    def test_traverse(self):
        """Test in-order traversal of the B-Tree."""
        elements = [10, 20, 5, 6, 12, 30, 7, 17]
        for element in elements:
            self.b_tree.insert(element)

        expected_traversal = [5, 6, 7, 10, 12, 17, 20, 30]
        actual_traversal = self.b_tree.traverse()
        self.assertEqual(expected_traversal, actual_traversal)

    def test_search(self):
        """Test searching for elements in the B-Tree."""
        elements = [10, 20, 5, 6, 12, 30, 7, 17]
        for element in elements:
            self.b_tree.insert(element)

        # Search for existing elements
        for element in elements:
            node = self.b_tree.search(element)
            self.assertIsNotNone(node, f"Element {element} should be found in the tree")
            self.assertIn(element, node.keys, f"Element {element} should be in node keys")

        # Search for a non-existing element
        non_existing = 100
        node = self.b_tree.search(non_existing)
        self.assertIsNone(node, f"Element {non_existing} should not be found in the tree")

if __name__ == '__main__':
    unittest.main()

import unittest

from Graph.Tree.BinarySearchTree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """Set up a test case environment."""
        self.tree = BinarySearchTree[int]()
        self.values = [15, 10, 20, 8, 12, 17, 25]
        for value in self.values:
            self.tree.insert(value)

    def test_insert(self):
        """Test insertion of values into the tree."""
        self.assertEqual(len(self.tree), len(self.values))
        self.assertIn(15, self.tree)
        self.assertIn(10, self.tree)
        self.assertIn(20, self.tree)

    def test_search(self):
        """Test searching for values in the tree."""
        for value in self.values:
            self.assertTrue(self.tree.search(value))
        self.assertFalse(self.tree.search(100))

    def test_delete_leaf(self):
        """Test deletion of a leaf node."""
        self.tree.delete(8)  # 8 is a leaf node
        self.assertFalse(self.tree.search(8))
        self.assertEqual(len(self.tree), len(self.values) - 1)

    def test_delete_node_with_one_child(self):
        """Test deletion of a node with one child."""
        self.tree.delete(10)  # 10 has one child (8 or 12)
        self.assertFalse(self.tree.search(10))
        self.assertEqual(len(self.tree), len(self.values) - 1)

    def test_delete_node_with_two_children(self):
        """Test deletion of a node with two children."""
        self.tree.delete(15)  # 15 has two children (10 and 20)
        self.assertFalse(self.tree.search(15))
        self.assertEqual(len(self.tree), len(self.values) - 1)

    def test_in_order_traversal(self):
        """Test the in-order traversal of the tree."""
        expected_order = sorted(self.values)
        actual_order = list(self.tree)
        self.assertEqual(actual_order, expected_order)

if __name__ == "__main__":
    unittest.main()

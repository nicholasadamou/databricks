import unittest
from Graph.Tree.RedBlackTree.RedBlackTree import RedBlackTree, RedBlackNode

class TestRedBlackTree(unittest.TestCase):

    def setUp(self):
        """Set up the Red-Black tree for testing."""
        self.rb_tree = RedBlackTree[int]()

    def test_insert(self):
        """Test insertion of elements into the Red-Black tree."""
        elements = [10, 20, 30, 15, 25, 5]
        for element in elements:
            self.rb_tree.insert(element)

        # Check if root is black
        self.assertFalse(self.rb_tree.root.color, "Root should be black")

    def test_in_order_traversal(self):
        """Test in-order traversal of the Red-Black tree."""
        elements = [10, 20, 30, 15, 25, 5]
        for element in elements:
            self.rb_tree.insert(element)

        expected_in_order = [5, 10, 15, 20, 25, 30]
        actual_in_order = list(self.rb_tree)
        self.assertEqual(expected_in_order, actual_in_order)

    def test_tree_properties(self):
        """Test Red-Black tree properties after insertions."""
        elements = [10, 20, 30, 15, 25, 5]
        for element in elements:
            self.rb_tree.insert(element)

        self._check_red_black_properties(self.rb_tree.root)

    def _check_red_black_properties(self, node: RedBlackNode[int]):
        """Helper method to check Red-Black tree properties."""
        if node == self.rb_tree.NIL_LEAF:
            return

        # Check red node's children are black
        if node.color:  # If node is red
            self.assertFalse(node.left.color, f"Left child of red node {node.key} must be black")
            self.assertFalse(node.right.color, f"Right child of red node {node.key} must be black")

        self._check_red_black_properties(node.left)
        self._check_red_black_properties(node.right)

    def test_structure_after_inserts(self):
        """Test the structure of the tree after insertions."""
        elements = [10, 20, 30, 15, 25, 5]
        for element in elements:
            self.rb_tree.insert(element)

        # Manually verify some expected structure aspects
        self.assertIsNotNone(self.rb_tree.root)
        self.assertIsNotNone(self.rb_tree.root.left)
        self.assertIsNotNone(self.rb_tree.root.right)

if __name__ == '__main__':
    unittest.main()

import unittest
from typing import List

from Graph.Tree.AVLTree.AVLTree import AVLTree, AVLNode

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        """Set up the AVL tree for testing."""
        self.avl_tree = AVLTree[int]()

    def _insert_elements(self, elements: List[int]):
        """Helper method to insert multiple elements into the AVL tree."""
        for element in elements:
            self.avl_tree.insert_key(element)

    def _collect_pre_order(self, node: AVLNode[int], result: List[int]):
        """Helper method to collect pre-order traversal of the tree."""
        if node is not None:
            result.append(node.key)
            self._collect_pre_order(node.left, result)
            self._collect_pre_order(node.right, result)

    def _check_balance(self, node: AVLNode[int]):
        """Helper method to check balance factor of each node."""
        if node is not None:
            balance = self.avl_tree.get_balance(node)
            self.assertTrue(-1 <= balance <= 1, f"Node with key {node.key} is unbalanced with balance factor {balance}")
            self._check_balance(node.left)
            self._check_balance(node.right)

    def test_insert(self):
        """Test insertion of elements into the AVL tree."""
        elements = [10, 20, 30, 40, 50, 25]
        self._insert_elements(elements)

        # Check if root is balanced
        self.assertEqual(self.avl_tree.root.key, 30)
        self.assertEqual(self.avl_tree.get_balance(self.avl_tree.root), 0)

    def test_pre_order_traversal(self):
        """Test pre-order traversal of the AVL tree."""
        elements = [10, 20, 30, 40, 50, 25]
        self._insert_elements(elements)

        expected_pre_order = [30, 20, 10, 25, 40, 50]
        actual_pre_order = []
        self._collect_pre_order(self.avl_tree.root, actual_pre_order)
        self.assertEqual(expected_pre_order, actual_pre_order)

    def test_balance_after_insertions(self):
        """Test balance of AVL tree after multiple insertions."""
        elements = [10, 20, 30, 40, 50, 25]
        self._insert_elements(elements)

        # Check balance factor for each node
        self._check_balance(self.avl_tree.root)

    def test_single_rotation(self):
        """Test single right and left rotations."""
        self._insert_elements([30, 20, 10])  # Should trigger a right rotation

        self.assertEqual(self.avl_tree.root.key, 20)
        self.assertEqual(self.avl_tree.root.left.key, 10)
        self.assertEqual(self.avl_tree.root.right.key, 30)

        self.avl_tree = AVLTree[int]()  # Reset tree
        self._insert_elements([10, 20, 30])  # Should trigger a left rotation

        self.assertEqual(self.avl_tree.root.key, 20)
        self.assertEqual(self.avl_tree.root.left.key, 10)
        self.assertEqual(self.avl_tree.root.right.key, 30)

    def test_double_rotation(self):
        """Test double rotations: left-right and right-left."""
        self._insert_elements([30, 10, 20])  # Should trigger a left-right rotation

        self.assertEqual(self.avl_tree.root.key, 20)
        self.assertEqual(self.avl_tree.root.left.key, 10)
        self.assertEqual(self.avl_tree.root.right.key, 30)

        self.avl_tree = AVLTree[int]()  # Reset tree
        self._insert_elements([10, 30, 20])  # Should trigger a right-left rotation

        self.assertEqual(self.avl_tree.root.key, 20)
        self.assertEqual(self.avl_tree.root.left.key, 10)
        self.assertEqual(self.avl_tree.root.right.key, 30)

if __name__ == '__main__':
    unittest.main()

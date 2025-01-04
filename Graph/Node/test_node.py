import unittest

from Graph.Node.Node import Node

class TestNode(unittest.TestCase):
    def test_node(self):
        node = Node(1)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.adjacent_nodes, [])

        node.add_adjacent(Node(2))
        self.assertEqual(len(node.adjacent_nodes), 1)
        self.assertEqual(node.adjacent_nodes[0].value, 2)

if __name__ == '__main__':
    unittest.main()

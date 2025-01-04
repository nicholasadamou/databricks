import unittest

from Graph.UndirectedGraph.UndirectedGraph import UndirectedGraph

def format_sorted_nodes(nodes):
    """Helper function to format sorted nodes into a string."""
    result = []

    for node in nodes:
        adjacent_nodes = ', '.join(str(adj.value) for adj in node.adjacent_nodes)
        result.append(f"{node.value} -> [{adjacent_nodes}]")

    return "\n".join(result)

class TestUndirectedGraph(unittest.TestCase):

    def setUp(self):
        """Set up a sample undirected graph for testing."""
        self.graph = UndirectedGraph()
        self.a = self.graph.add_node("a")
        self.b = self.graph.add_node("b")
        self.c = self.graph.add_node("c")
        self.d = self.graph.add_node("d")
        self.e = self.graph.add_node("e")
        self.f = self.graph.add_node("f")

        self.graph.add_edge(self.a, self.b)
        self.graph.add_edge(self.a, self.c)
        self.graph.add_edge(self.b, self.d)
        self.graph.add_edge(self.c, self.d)
        self.graph.add_edge(self.d, self.e)
        self.graph.add_edge(self.f, self.e)

    def test_undirected_graph(self):
        expected_representation = (
            "a -> [b, c]\n"
            "b -> [a, d]\n"
            "c -> [a, d]\n"
            "d -> [b, c, e]\n"
            "e -> [d, f]\n"
            "f -> [e]"
        )
        self.assertEqual(str(self.graph), expected_representation)

    def test_bidirectional_edges(self):
        """Test that all edges are bidirectional."""
        for node in self.graph.nodes:
            for adj in node.adjacent_nodes:
                self.assertIn(node, adj.adjacent_nodes, f"Edge from {node.value} to {adj.value} is not bidirectional")

if __name__ == '__main__':
    unittest.main()

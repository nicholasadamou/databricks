import unittest

from Graph.DirectedGraph.DirectedGraph import DirectedGraph

def format_sorted_nodes(nodes):
    """Helper function to format sorted nodes into a string."""
    result = []

    for node in nodes:
        adjacent_nodes = ', '.join(str(adj.value) for adj in node.adjacent_nodes)
        result.append(f"{node.value} -> [{adjacent_nodes}]")

    return "\n".join(result)

class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        """Set up a sample directed graph for testing."""
        self.graph = DirectedGraph()
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

    def test_directed_graph(self):
        expected_representation = (
            "a -> [b, c]\n"
            "b -> [d]\n"
            "c -> [d]\n"
            "d -> [e]\n"
            "e -> []\n"
            "f -> [e]"
        )
        self.assertEqual(str(self.graph), expected_representation)

    def test_sort(self):
        sorted_nodes = self.graph.sort()
        sorted_values = [node.value for node in sorted_nodes]

        # Check if the sorted order is a valid topological sort
        self.assertTrue(self.is_valid_topological_sort(sorted_values))

    def is_valid_topological_sort(self, sorted_values):
        """Helper function to validate topological sort order."""
        index_map = {value: index for index, value in enumerate(sorted_values)}

        # Check all edges to ensure the source comes before the destination
        for node in self.graph.nodes:
            for adj in node.adjacent_nodes:
                if index_map[node.value] > index_map[adj.value]:
                    return False

        return True

if __name__ == '__main__':
    unittest.main()

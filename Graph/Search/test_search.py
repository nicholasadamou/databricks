import unittest

from Graph.Node.Node import Node
from Graph.Search.search import dfs, bfs

class TestGraphTraversal(unittest.TestCase):
    def setUp(self):
        """
        Set up a sample graph for testing.
        Graph structure:
        a -> b -> c
        a -> d
        d -> e
        f -> g
        """
        self.a = Node("a")
        self.b = Node("b")
        self.c = Node("c")
        self.d = Node("d")
        self.e = Node("e")
        self.f = Node("f")
        self.g = Node("g")

        self.a.adjacent_nodes = [self.b, self.d]
        self.b.adjacent_nodes = [self.c]
        self.d.adjacent_nodes = [self.e]
        self.f.adjacent_nodes = [self.g]

    def test_dfs(self):
        """
        Test Depth-First Search (DFS) traversal order.
        """
        visited_nodes_pre = []
        visited_nodes_post = []

        def pre_visit(node):
            visited_nodes_pre.append(node.value)

        def post_visit(node):
            visited_nodes_post.append(node.value)

        dfs(self.a, pre_fn=pre_visit, post_fn=post_visit)

        # DFS (pre-processing order): a -> b -> c -> d -> e
        self.assertEqual(visited_nodes_pre, ["a", "b", "c", "d", "e"])

        # DFS (post-processing order): c -> b -> e -> d -> a
        self.assertEqual(visited_nodes_post, ["c", "b", "e", "d", "a"])

    def test_bfs(self):
        """
        Test Breadth-First Search (BFS) traversal order.
        """
        visited_nodes_process = []
        visited_nodes_enqueue = []

        def process(node):
            visited_nodes_process.append(node.value)

        def enqueue(node):
            visited_nodes_enqueue.append(node.value)

        bfs(self.a, process_fn=process, enqueue_fn=enqueue)

        # BFS (process order): a -> b -> d -> c -> e
        self.assertEqual(visited_nodes_process, ["a", "b", "d", "c", "e"])

        # BFS (enqueue order): a -> b -> d -> c -> e
        self.assertEqual(visited_nodes_enqueue, ["a", "b", "d", "c", "e"])


    def test_disconnected_graph_dfs(self):
        """
        Test DFS with a disconnected graph.
        """
        visited_nodes = []
        visited = set()

        def visit(node):
            visited_nodes.append(node.value)

        dfs(self.a, pre_fn=visit, visited=visited)
        dfs(self.f, pre_fn=visit, visited=visited)

        # DFS should follow: a -> b -> c -> d -> e -> f -> g
        self.assertEqual(visited_nodes, ["a", "b", "c", "d", "e", "f", "g"])

    def test_disconnected_graph_bfs(self):
        """
        Test BFS with a disconnected graph.
        """
        visited_nodes = []

        def visit(node):
            visited_nodes.append(node.value)

        bfs(self.a, process_fn=visit)
        bfs(self.f, visit)

        # BFS should follow: a -> b -> d -> c -> e -> f -> g
        self.assertEqual(visited_nodes, ["a", "b", "d", "c", "e", "f", "g"])


if __name__ == "__main__":
    unittest.main()

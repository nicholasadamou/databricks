from Graph.Node.Node import Node
from Graph.Search.search import dfs
from LinkedList.DoublyLinkedList.DoublyLinkedList import DoublyLinkedList
from typing import Generic, TypeVar

T = TypeVar("T")

class DirectedGraph(Generic[T]):
    def __init__(self):
        self.nodes: DoublyLinkedList[Node[T]] = DoublyLinkedList()

    def add_node(self, value: T) -> Node[T]:
        """
        Add a node to the graph
        :param value: The value of the node
        :return: The node that was added
        """
        node = Node(value)
        self.nodes.append(node)

        return node

    def add_edge(self, source: Node[T], destination: Node[T]) -> None:
        """
        Add an edge between two nodes
        :param source: The source node
        :param destination: The destination node
        """
        if source not in self.nodes or destination not in self.nodes:
            raise ValueError("Source and destination nodes must be in the graph")

        source.add_adjacent(destination)

    def sort(self) -> DoublyLinkedList[Node[T]]:
        """
        Topological sort using DFS
        :return: The sorted nodes
        """
        sorted_nodes = DoublyLinkedList()

        def fn(node: Node[T]):
            sorted_nodes.prepend(node)

        for node in self.nodes:
            dfs(node, post_fn=fn)

        return sorted_nodes


    def __str__(self):
        result = []

        for node in self.nodes:
            adjacent_nodes = ', '.join(str(adj) for adj in node.adjacent_nodes)
            result.append(f"{node.value} -> [{adjacent_nodes}]")

        return "\n".join(result)

    def __repr__(self):
        return self.__str__()

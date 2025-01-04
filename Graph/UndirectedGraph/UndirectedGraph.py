from Graph.Node.Node import Node
from LinkedList.DoublyLinkedList.DoublyLinkedList import DoublyLinkedList
from typing import Generic, TypeVar

T = TypeVar("T")

class UndirectedGraph(Generic[T]):
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

    def add_edge(self, node1: Node[T], node2: Node[T]) -> None:
        """
        Add an edge between two nodes
        :param node1: The first node
        :param node2: The second node
        """
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Both nodes must be in the graph")

        # Add each node to the other's adjacency list to make the edge bidirectional
        node1.add_adjacent(node2)
        node2.add_adjacent(node1)

    def __str__(self):
        result = []

        for node in self.nodes:
            adjacent_nodes = ', '.join(str(adj) for adj in node.adjacent_nodes)
            result.append(f"{node.value} -> [{adjacent_nodes}]")

        return "\n".join(result)

    def __repr__(self):
        return self.__str__()

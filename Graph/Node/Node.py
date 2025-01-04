from typing import Generic, TypeVar, List

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.adjacent_nodes: List['Node[T]'] = []

    def add_adjacent(self, node: 'Node[T]') -> None:
        """
        Add an adjacent node to the current node's adjacency list.
        :param node: The node to add as adjacent
        """
        self.adjacent_nodes.append(node)

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other) -> bool:
        return isinstance(other, Node) and self.value == other.value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.__str__()

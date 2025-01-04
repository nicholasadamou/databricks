from typing import TypeVar, Generic, Optional, Iterator

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T):
        """
        Initialize a new node with a given value.

        :param value: The value to store in the node.
        """
        self.value: T = value
        self.parent: Optional['Node[T]'] = None
        self.left: Optional['Node[T]'] = None
        self.right: Optional['Node[T]'] = None

    def __hash__(self) -> int:
        """
        Return the hash of the node based on its value.

        :return: Hash value of the node.
        """
        return hash(self.value)

    def __eq__(self, other) -> bool:
        """
        Check if this node is equal to another node.

        :param other: The node to compare with.
        :return: True if nodes are equal, otherwise False.
        """
        return isinstance(other, Node) and self.value == other.value

    def __str__(self) -> str:
        """
        Return the string representation of the node's value.

        :return: String representation of the node's value.
        """
        return str(self.value)

    def __repr__(self) -> str:
        """
        Return the string representation of the node for debugging.

        :return: String representation of the node.
        """
        return self.__str__()

    def is_leaf(self) -> bool:
        """
        Check if the node is a leaf node (has no children).

        :return: True if the node is a leaf, otherwise False.
        """
        return self.left is None and self.right is None

    def has_left_child(self) -> bool:
        """
        Check if the node has a left child.

        :return: True if the node has a left child, otherwise False.
        """
        return self.left is not None

    def has_right_child(self) -> bool:
        """
        Check if the node has a right child.

        :return: True if the node has a right child, otherwise False.
        """
        return self.right is not None

    def has_both_children(self) -> bool:
        """
        Check if the node has both left and right children.

        :return: True if the node has both children, otherwise False.
        """
        return self.has_left_child() and self.has_right_child()

    def has_any_children(self) -> bool:
        """
        Check if the node has any children.

        :return: True if the node has any children, otherwise False.
        """
        return self.has_left_child() or self.has_right_child()

    def __iter__(self) -> Iterator[T]:
        """
        In-order traversal of the tree starting from this node.

        :yield: Node values in in-order sequence.
        """
        if self.has_left_child():
            yield from self.left

        yield self.value

        if self.has_right_child():
            yield from self.right


class BinarySearchTree(Generic[T]):
    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        """
        self.root: Optional[Node[T]] = None
        self.size: int = 0

    def __len__(self) -> int:
        """
        Return the number of nodes in the tree.

        :return: The size of the tree.
        """
        return self.size

    def __iter__(self) -> Iterator[T]:
        """
        In-order traversal of the tree.

        :yield: Node values in in-order sequence.
        """
        if self.root:
            yield from self.root

    def __str__(self) -> str:
        """
        Return the string representation of the tree's root.

        :return: String representation of the root node.
        """
        return str(self.root)

    def __repr__(self) -> str:
        """
        Return the string representation of the tree for debugging.

        :return: String representation of the tree.
        """
        return self.__str__()

    def insert(self, value: T) -> None:
        """
        Insert a value into the tree.

        :param value: The value to insert.
        """
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        else:
            self._insert(self.root, value)

    def _insert(self, node: Node[T], value: T) -> None:
        """
        Helper method to insert a value starting from a given node.

        :param node: The node to start the insertion from.
        :param value: The value to insert.
        """
        if value < node.value:
            if node.has_left_child():
                self._insert(node.left, value)
            else:
                node.left = Node(value)
                node.left.parent = node
                self.size += 1
        else:
            if node.has_right_child():
                self._insert(node.right, value)
            else:
                node.right = Node(value)
                node.right.parent = node
                self.size += 1

    def search(self, value: T) -> bool:
        """
        Search for a value in the tree.

        :param value: The value to search for.
        :return: True if the value is found, otherwise False.
        """
        return self._search(self.root, value)

    def _search(self, node: Optional[Node[T]], value: T) -> bool:
        """
        Helper method to search for a value starting from a given node.

        :param node: The node to start the search from.
        :param value: The value to search for.
        :return: True if the value is found, otherwise False.
        """
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def delete(self, value: T) -> None:
        """
        Delete a value from the tree.

        :param value: The value to delete.
        """
        self._delete(self.root, value)

    def _delete(self, node: Optional[Node[T]], value: T) -> None:
        """
        Helper method to delete a value starting from a given node.

        :param node: The node to start the deletion from.
        :param value: The value to delete.
        """
        if node is None:
            return
        elif value < node.value:
            self._delete(node.left, value)
        elif value > node.value:
            self._delete(node.right, value)
        else:
            if node.is_leaf():
                self._delete_leaf(node)
            elif node.has_both_children():
                self._delete_internal(node)
            else:
                self._delete_one_child(node)

    def _delete_leaf(self, node: Node[T]) -> None:
        """
        Helper method to delete a leaf node.

        :param node: The leaf node to delete.
        """
        if node.parent is None:
            self.root = None
        elif node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None
        self.size -= 1

    def _delete_internal(self, node: Node[T]) -> None:
        """
        Helper method to delete a node with two children.

        :param node: The node to delete.
        """
        successor = self._find_min(node.right)
        node.value = successor.value
        if successor.is_leaf():
            self._delete_leaf(successor)
        else:
            self._delete_one_child(successor)

    def _find_min(self, node: Node[T]) -> Node[T]:
        """
        Find the node with the minimum value starting from a given node.

        :param node: The node to start the search from.
        :return: The node with the minimum value.
        """
        current = node
        while current.left:
            current = current.left
        return current

    def _delete_one_child(self, node: Node[T]) -> None:
        """
        Helper method to delete a node with one child.

        :param node: The node to delete.
        """
        child = node.left if node.has_left_child() else node.right
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        if child:
            child.parent = node.parent
        self.size -= 1

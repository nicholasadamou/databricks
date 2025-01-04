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

    def insert(self, value: T) -> None:
        """
        Insert a value into the subtree rooted at this node.

        :param value: The value to insert.
        """
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
                self.right.parent = self
            else:
                self.right.insert(value)

    def search(self, value: T) -> bool:
        """
        Search for a value in the subtree rooted at this node.
        :param value: The value to search for.
        :return: True if the value is found, otherwise False.
        """
        if self.value == value:
            return True
        elif value < self.value and self.left is not None:
            return self.left.search(value)
        elif value > self.value and self.right is not None:
            return self.right.search(value)
        return False

    def delete(self, value: T) -> Optional['Node[T]']:
        """
        Delete a value from the subtree rooted at this node.
        :param value: The value to delete.
        :return: The root of the updated subtree.
        """
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Node to be deleted found
            if self.is_leaf():
                return None

            if self.has_both_children():
                # Node has two children
                successor = self.right.find_min()
                self.value = successor.value
                self.right = self.right.delete(successor.value)
            else:
                # Node has one child
                return self.left or self.right

        return self # Return the root of the updated subtree

    def find_min(self) -> 'Node[T]':
        """
        Find the node with the minimum value in the subtree rooted at this node.
        :return: The node with the minimum value.
        """
        current = self
        while current.left:
            current = current.left
        return current

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
        else:
            self.root.insert(value)
        self.size += 1

    def search(self, value: T) -> bool:
        """
        Search for a value in the tree.

        :param value: The value to search for.
        :return: True if the value is found, otherwise False.
        """
        if self.root is None:
            return False

        return self.root.search(value)

    def delete(self, value: T) -> None:
        """
        Delete a value from the tree.

        :param value: The value to delete.
        """
        if self.root is None:
            return

        self.root = self.root.delete(value)
        self.size -= 1

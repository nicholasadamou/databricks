from typing import TypeVar, Generic, Optional, Iterator

T = TypeVar('T')

class AVLNode(Generic[T]):
    """
    A node in an AVL tree.

    :param key: The value stored in the node.
    :type key: T
    """
    def __init__(self, key: T):
        self.key = key
        self.height = 1
        self.left: Optional['AVLNode[T]'] = None
        self.right: Optional['AVLNode[T]'] = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return f"AVLNode(key={self.key}, height={self.height})"

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return str(self)

    def __eq__(self, other: object) -> bool:
        """Check equality between two nodes."""
        if not isinstance(other, AVLNode):
            return NotImplemented
        return self.key == other.key and self.height == other.height

class AVLTree(Generic[T]):
    """
    An AVL tree implementation.
    """
    def __init__(self):
        self.root: Optional[AVLNode[T]] = None

    def __str__(self) -> str:
        """Return a string representation of the AVL tree."""
        nodes = list(self)
        return f"AVLTree({nodes})"

    def __repr__(self) -> str:
        """Return a string representation of the AVL tree."""
        return str(self)

    def __eq__(self, other: object) -> bool:
        """Check equality between two AVL trees."""
        if not isinstance(other, AVLTree):
            return NotImplemented
        return list(self) == list(other)

    def __iter__(self) -> Iterator[T]:
        """Iterate through the tree in-order."""
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node: Optional[AVLNode[T]]) -> Iterator[T]:
        """Generator for in-order traversal."""
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield node.key
            yield from self._in_order_traversal(node.right)

    def get_height(self, node: Optional[AVLNode[T]]) -> int:
        """
        Get the height of a node.

        :param node: The node to check.
        :return: The height of the node.
        """
        return node.height if node else 0

    def get_balance(self, node: Optional[AVLNode[T]]) -> int:
        """
        Calculate the balance factor of a node.

        :param node: The node to check.
        :return: The balance factor.
        """
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y: AVLNode[T]) -> AVLNode[T]:
        """
        Perform a right rotation.

        :param y: The root of the subtree to rotate.
        :return: The new root of the subtree.
        """
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x: AVLNode[T]) -> AVLNode[T]:
        """
        Perform a left rotation.

        :param x: The root of the subtree to rotate.
        :return: The new root of the subtree.
        """
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, node: Optional[AVLNode[T]], key: T) -> AVLNode[T]:
        """
        Insert a key and balance the tree.

        :param node: The root of the subtree to insert into.
        :param key: The key to insert.
        :return: The new subtree root.
        """
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert_key(self, key: T):
        """
        Insert a key into the AVL tree.

        :param key: The key to insert.
        """
        self.root = self.insert(self.root, key)

    def pre_order(self, node: Optional[AVLNode[T]]):
        """
        Perform a pre-order traversal.

        :param node: The root of the subtree to traverse.
        """
        if not node:
            return
        print(node.key, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

from typing import TypeVar, Generic, Optional, Iterator

T = TypeVar('T')

class RedBlackNode(Generic[T]):
    """
    A node in a Red-Black tree.

    :param key: The value stored in the node.
    :type key: T
    :param color: The color of the node (True for Red, False for Black).
    :type color: bool
    """
    def __init__(self, key: T, color: bool):
        self.key = key
        self.color = color  # True for Red, False for Black
        self.left: Optional['RedBlackNode[T]'] = None
        self.right: Optional['RedBlackNode[T]'] = None
        self.parent: Optional['RedBlackNode[T]'] = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        color = 'Red' if self.color else 'Black'
        return f"RedBlackNode(key={self.key}, color={color})"

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return str(self)

    def __eq__(self, other: object) -> bool:
        """Check equality between two nodes."""
        if not isinstance(other, RedBlackNode):
            return NotImplemented
        return self.key == other.key and self.color == other.color

class RedBlackTree(Generic[T]):
    """
    A Red-Black tree implementation.
    """
    def __init__(self):
        self.NIL_LEAF = RedBlackNode(None, False)  # Sentinel node for leaves
        self.root: RedBlackNode[T] = self.NIL_LEAF

    def __str__(self) -> str:
        """Return a string representation of the Red-Black tree."""
        nodes = list(self)
        return f"RedBlackTree({nodes})"

    def __repr__(self) -> str:
        """Return a string representation of the Red-Black tree."""
        return str(self)

    def __eq__(self, other: object) -> bool:
        """Check equality between two Red-Black trees."""
        if not isinstance(other, RedBlackTree):
            return NotImplemented
        return list(self) == list(other)

    def __iter__(self) -> Iterator[T]:
        """Iterate through the tree in-order."""
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node: RedBlackNode[T]) -> Iterator[T]:
        """Generator for in-order traversal."""
        if node != self.NIL_LEAF:
            yield from self._in_order_traversal(node.left)
            yield node.key
            yield from self._in_order_traversal(node.right)

    def left_rotate(self, x: RedBlackNode[T]):
        """
        Perform a left rotation.

        :param x: The root of the subtree to rotate.
        """
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y: RedBlackNode[T]):
        """
        Perform a right rotation.

        :param y: The root of the subtree to rotate.
        """
        x = y.left
        y.left = x.right
        if x.right != self.NIL_LEAF:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def insert(self, key: T):
        """
        Insert a key into the Red-Black tree.

        :param key: The key to insert.
        """
        new_node = RedBlackNode(key, True)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        parent = None
        current = self.root

        while current != self.NIL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = False  # Root is always black
            return

        if new_node.parent.parent is None:
            return

        self._fix_insert(new_node)

    def _fix_insert(self, k: RedBlackNode[T]):
        """Fix the Red-Black tree after insertion."""
        while k.parent and k.parent.color:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color:
                    u.color = False
                    k.parent.color = False
                    k.parent.parent.color = True
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = False
                    k.parent.parent.color = True
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color:
                    u.color = False
                    k.parent.color = False
                    k.parent.parent.color = True
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = False
                    k.parent.parent.color = True
                    self.left_rotate(k.parent.parent)

            if k == self.root:
                break

        self.root.color = False

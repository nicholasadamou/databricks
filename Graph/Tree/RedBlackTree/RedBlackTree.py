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

    def delete(self, key: T):
        """
        Delete a node with the given key from the Red-Black tree.

        :param key: The key of the node to delete.
        """
        z = self._find_node(self.root, key)
        if z == self.NIL_LEAF:
            return  # Key not found in the tree

        y = z
        y_original_color = y.color
        if z.left == self.NIL_LEAF:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL_LEAF:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if not y_original_color:
            self._fix_delete(x)

    def _transplant(self, u: RedBlackNode[T], v: RedBlackNode[T]):
        """
        Replace the subtree rooted at node u with the subtree rooted at node v.

        :param u: The node to be replaced.
        :param v: The replacement node.
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node: RedBlackNode[T]) -> RedBlackNode[T]:
        """
        Find the node with the minimum key in the subtree rooted at the given node.

        :param node: The root of the subtree.
        :return: The node with the minimum key.
        """
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def _fix_delete(self, x: RedBlackNode[T]):
        """
        Fix the Red-Black tree after a deletion to maintain Red-Black properties.

        :param x: The node to fix starting from.
        """
        while x != self.root and x.color == False:
            if x == x.parent.left:
                w = x.parent.right
                if w.color:  # Case 1
                    w.color = False
                    x.parent.color = True
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == False and w.right.color == False:  # Case 2
                    w.color = True
                    x = x.parent
                else:
                    if not w.right.color:  # Case 3
                        w.left.color = False
                        w.color = True
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color  # Case 4
                    x.parent.color = False
                    w.right.color = False
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color:  # Case 1
                    w.color = False
                    x.parent.color = True
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == False and w.right.color == False:  # Case 2
                    w.color = True
                    x = x.parent
                else:
                    if not w.left.color:  # Case 3
                        w.right.color = False
                        w.color = True
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color  # Case 4
                    x.parent.color = False
                    w.left.color = False
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = False

    def _find_node(self, node: RedBlackNode[T], key: T) -> RedBlackNode[T]:
        """
        Find a node with the given key in the subtree rooted at the given node.

        :param node: The root of the subtree.
        :param key: The key to search for.
        :return: The node with the given key, or NIL_LEAF if not found.
        """
        while node != self.NIL_LEAF and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

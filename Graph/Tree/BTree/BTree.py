from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class BTreeNode(Generic[T]):
    """
    A node in a B-Tree.

    :param t: The minimum degree (defines the range for the number of keys).
    :type t: int
    :param leaf: Indicates whether the node is a leaf node.
    :type leaf: bool
    """
    def __init__(self, t: int, leaf: bool = False):
        self.t = t  # Minimum degree
        self.leaf = leaf  # True if leaf node, otherwise false
        self.keys: List[T] = []  # List to store keys
        self.children: List['BTreeNode[T]'] = []  # List to store child pointers

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return f"BTreeNode(keys={self.keys}, leaf={self.leaf})"

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return str(self)

    def traverse(self) -> List[T]:
        """
        Traverse the subtree rooted at this node and return all keys in sorted order.

        :return: A list of keys in sorted order.
        :rtype: List[T]
        """
        keys = []
        for i in range(len(self.keys)):
            if not self.leaf:
                keys.extend(self.children[i].traverse())
            keys.append(self.keys[i])
        if not self.leaf:
            keys.extend(self.children[len(self.keys)].traverse())
        return keys

    def search(self, k: T) -> Optional['BTreeNode[T]']:
        """
        Search for a key in the subtree rooted at this node.

        :param k: The key to search for.
        :type k: T
        :return: The node containing the key, or None if the key is not found.
        :rtype: Optional[BTreeNode[T]]
        """
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1

        if i < len(self.keys) and self.keys[i] == k:
            return self

        if self.leaf:
            return None

        return self.children[i].search(k)

    def insert_non_full(self, k: T):
        """
        Insert a new key into this node. Assumes the node is not full.

        :param k: The key to insert.
        :type k: T
        """
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)  # Add a dummy key to extend the list
            while i >= 0 and self.keys[i] > k:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            while i >= 0 and self.keys[i] > k:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if self.keys[i] < k:
                    i += 1
            self.children[i].insert_non_full(k)

    def split_child(self, i: int):
        """
        Split the child of this node at index i.

        :param i: The index of the child to split.
        :type i: int
        """
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t: (2 * t - 1)]
        y.keys = y.keys[0: t - 1]

        if not y.leaf:
            z.children = y.children[t: (2 * t)]
            y.children = y.children[0: t]

class BTree(Generic[T]):
    """
    A B-Tree implementation.

    :param t: The minimum degree of the B-Tree.
    :type t: int
    """
    def __init__(self, t: int):
        self.root: Optional[BTreeNode[T]] = None
        self.t = t  # Minimum degree

    def __str__(self) -> str:
        """Return a string representation of the B-Tree."""
        return f"BTree(t={self.t}, root={self.root})"

    def __repr__(self) -> str:
        """Return a string representation of the B-Tree."""
        return str(self)

    def traverse(self) -> List[T]:
        """
        Traverse the entire B-Tree and return all keys in sorted order.

        :return: A list of keys in sorted order.
        :rtype: List[T]
        """
        return self.root.traverse() if self.root else []

    def search(self, k: T) -> Optional[BTreeNode[T]]:
        """
        Search for a key in the B-Tree.

        :param k: The key to search for.
        :type k: T
        :return: The node containing the key, or None if the key is not found.
        :rtype: Optional[BTreeNode[T]]
        """
        return self.root.search(k) if self.root else None

    def insert(self, k: T):
        """
        Insert a new key into the B-Tree.

        :param k: The key to insert.
        :type k: T
        """
        if not self.root:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(k)
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                s = BTreeNode(self.t)
                s.children.append(self.root)
                s.split_child(0)
                i = 0
                if s.keys[0] < k:
                    i += 1
                s.children[i].insert_non_full(k)
                self.root = s
            else:
                self.root.insert_non_full(k)

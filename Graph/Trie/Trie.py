class TrieNode:
    """
    Represents a single node in the Trie.

    :ivar children: A dictionary mapping characters to TrieNode children.
    :ivar is_end_of_word: A boolean indicating if the node marks the end of a word.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    A Trie (prefix tree) implementation for efficient string storage and lookup.
    """
    def __init__(self):
        """
        Initializes the Trie with a root node.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.

        :param word: The word to insert into the Trie.
        :type word: str
        :return: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Searches for a word in the Trie.

        :param word: The word to search for in the Trie.
        :type word: str
        :return: True if the word is in the Trie, otherwise False.
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Checks if there is any word in the Trie that starts with the given prefix.

        :param prefix: The prefix to search for in the Trie.
        :type prefix: str
        :return: True if there is a word in the Trie that starts with the prefix, otherwise False.
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

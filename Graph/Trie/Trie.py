"""
Why use a dictionary to store children in a Trie?

The TrieNode class uses a dictionary to store children because it provides a more efficient way to look up child nodes based on the character.

The alternative of using an array or list to store children would require iterating over all children to find the one with the matching character.
This would result in a time complexity of O(n) for each character lookup, where n is the number of children.

By using a dictionary, the lookup time is reduced to O(1) on average, as dictionaries provide constant-time access to values based on keys.
"""

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

    def delete(self, word):
        """
        Deletes a word from the Trie.

        :param word: The word to delete from the Trie.
        :type word: str
        :return: None
        """
        def _delete(current, word, index):
            """
            Recursively deletes a word from the Trie.
            :param current: The current Trie node.
            :param word: The word to delete.
            :param index: The current index in the word.
            :return: True if the current node should be deleted, otherwise False.
            """
            if index == len(word):
                # Reached the end of the word to be deleted
                if not current.is_end_of_word:
                    return False  # Word does not exist
                current.is_end_of_word = False
                # If no children, this node can be deleted
                return len(current.children) == 0
            char = word[index]
            if char not in current.children:
                return False  # Word does not exist
            node = current.children[char]
            should_delete_current_node = _delete(node, word, index + 1)

            # If true, delete the reference to the child node
            if should_delete_current_node:
                del current.children[char]
                # Return true if no children are left and the current node is not the end of another word
                return len(current.children) == 0 and not current.is_end_of_word
            return False

        return _delete(self.root, word, 0)

    def total_words(self):
        """
        Returns the total number of words in the Trie.
        :return: The total number of words in the Trie.
        :rtype: int
        """
        def _count_words(node):
            """
            Recursively counts the number of words in the Trie.
            :param node: The current Trie node.
            :return: The total number of words in the Trie.
            :rtype: int
            """
            count = 0

            # Leaf nodes mark the end of a word
            if node.is_end_of_word:
                count += 1

            for child in node.children.values():
                count += _count_words(child)

            return count

        return _count_words(self.root)

    def get_words(self):
        """
        Returns all the words in the Trie.
        :return: A list of all words in the Trie.
        :rtype: List[str]
        """
        def _get_words(node, prefix):
            """
            Recursively retrieves all words in the Trie.
            :param node: The current Trie node.
            :param prefix: The prefix formed by the characters traversed so far.
            :return: A list of all words in the Trie.
            :rtype: List[str]
            """
            words = []

            if node.is_end_of_word:
                words.append(prefix)

            for char, child in node.children.items():
                words.extend(_get_words(child, prefix + char))

            return words

        return _get_words(self.root, "")

    def sort(self):
        """
        Returns all the words in the Trie in sorted order (lexicographically).
        :return: A list of all words in the Trie in sorted order.
        :rtype: List[str]
        """
        def _sort(node, prefix):
            """
            Recursively retrieves all words in the Trie in sorted order.
            :param node: The current Trie node.
            :param prefix: The prefix formed by the characters traversed so far.
            :return: A list of all words in the Trie in sorted order.
            :rtype: List[str]
            """
            words = []

            if node.is_end_of_word:
                words.append(prefix)

            for char, child in sorted(node.children.items()):
                words.extend(_sort(child, prefix + char))

            return words

        return _sort(self.root, "")

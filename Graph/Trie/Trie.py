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

import unittest

from Graph.Trie.Trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        """Set up a new Trie instance before each test."""
        self.trie = Trie()

    def test_insert_and_search(self):
        """Test inserting words and searching for them."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))

    def test_insert_and_starts_with(self):
        """Test inserting words and checking prefixes."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.starts_with("app"))
        self.assertFalse(self.trie.starts_with("apl"))

    def test_search_empty_trie(self):
        """Test searching in an empty Trie."""
        self.assertFalse(self.trie.search("any"))
        self.assertFalse(self.trie.starts_with("any"))

    def test_insert_multiple_words(self):
        """Test inserting multiple words and verifying their existence."""
        words = ["apple", "app", "bat", "ball", "cat"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertFalse(self.trie.search("dog"))
        self.assertTrue(self.trie.starts_with("ba"))
        self.assertTrue(self.trie.starts_with("ca"))

    def test_delete(self):
        """Test deleting a word from the Trie."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.trie.delete("apple")
        self.assertFalse(self.trie.search("apple"))

if __name__ == '__main__':
    unittest.main()

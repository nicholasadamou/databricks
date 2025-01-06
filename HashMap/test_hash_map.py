import unittest

from HashMap.HashMap import HashMap

class TestHashMap(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up a HashMap instance for testing.
        """
        self.hash_map = HashMap[str, int]()

    def test_put_and_get(self):
        """
        Test inserting key-value pairs and retrieving them.
        """
        self.hash_map.put("apple", 10)
        self.hash_map.put("banana", 20)

        self.assertEqual(self.hash_map.get("apple"), 10)
        self.assertEqual(self.hash_map.get("banana"), 20)
        self.assertIsNone(self.hash_map.get("cherry"))

    def test_update_value(self):
        """
        Test updating the value of an existing key.
        """
        self.hash_map.put("apple", 10)
        self.hash_map.put("apple", 15)  # Update the value

        self.assertEqual(self.hash_map.get("apple"), 15)

    def test_remove(self):
        """
        Test removing a key-value pair.
        """
        self.hash_map.put("apple", 10)
        self.hash_map.put("banana", 20)

        self.hash_map.remove("apple")
        self.assertIsNone(self.hash_map.get("apple"))
        self.assertEqual(self.hash_map.get("banana"), 20)

    def test_resize(self):
        """
        Test that the HashMap resizes correctly when load factor exceeds threshold.
        """
        for i in range(20):  # Insert more than the initial capacity
            self.hash_map.put(f"key{i}", i)

        for i in range(20):
            self.assertEqual(self.hash_map.get(f"key{i}"), i)

    def test_len(self):
        """
        Test the __len__ method to ensure it returns the correct size.
        """
        self.assertEqual(len(self.hash_map), 0)

        self.hash_map.put("apple", 10)
        self.assertEqual(len(self.hash_map), 1)

        self.hash_map.put("banana", 20)
        self.assertEqual(len(self.hash_map), 2)

        self.hash_map.remove("apple")
        self.assertEqual(len(self.hash_map), 1)

    def test_collision_handling(self):
        """
        Test that the HashMap handles hash collisions correctly.
        """
        class CollidingKey:
            def __init__(self, value):
                self.value = value

            def __hash__(self):
                # Force collision by returning the same hash for all keys
                return 42

            def __eq__(self, other):
                return isinstance(other, CollidingKey) and self.value == other.value

        map_with_collisions = HashMap[CollidingKey, int]()
        key1 = CollidingKey("key1")
        key2 = CollidingKey("key2")

        map_with_collisions.put(key1, 100)
        map_with_collisions.put(key2, 200)

        self.assertEqual(map_with_collisions.get(key1), 100)
        self.assertEqual(map_with_collisions.get(key2), 200)

if __name__ == "__main__":
    unittest.main()

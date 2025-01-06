from typing import TypeVar, Generic, List, Optional, Union, Tuple

from LinkedList.DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

K = TypeVar('K')
V = TypeVar('V')

"""
HashMap implementation using both lists and linked lists for buckets.

This implementation uses a hybrid approach to handle hash collisions. When a collision occurs, the bucket is
converted from a list to a DoublyLinkedList. This allows for O(1) insertion and deletion in the average case.

This hybrid approach combines the advantages of both list and DoublyLinkedList, optimizing performance for different scenarios.
"""


class HashMap(Generic[K, V]):
    """
    A hybrid HashMap implementation using both lists and linked lists for buckets.
    """

    def __init__(self, capacity: int = 10) -> None:
        """
        Initialize the HashMap with a given capacity.

        :param capacity: The initial capacity of the hash map. Defaults to 10.
        """
        self.capacity = capacity
        self.size = 0
        self.buckets: List[Union[List[Tuple[K, V]], DoublyLinkedList[Tuple[K, V]]]] = [
            [] for _ in range(capacity)
        ]
        self.collision_threshold = 3  # Switch to DoublyLinkedList after this many collisions

    def _hash(self, key: K) -> int:
        """
        Compute the hash index for a given key.

        :param key: The key to hash.
        :return: The hash index within the bucket list.
        """
        return hash(key) % self.capacity

    def _convert_to_linked_list(self, bucket: List[Tuple[K, V]]) -> DoublyLinkedList[Tuple[K, V]]:
        """
        Convert a list bucket to a DoublyLinkedList.

        :param bucket: The list bucket to convert.
        :return: A DoublyLinkedList with the same elements.
        """
        return DoublyLinkedList(bucket)

    def put(self, key: K, value: V) -> None:
        """
        Insert or update a key-value pair in the HashMap.

        :param key: The key to insert.
        :param value: The value associated with the key.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Handle the case where the bucket is a list
        if isinstance(bucket, list):
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)  # Update the value
                    return

            bucket.append((key, value))
            self.size += 1

            # Convert to DoublyLinkedList if collision threshold is exceeded
            if len(bucket) > self.collision_threshold:
                self.buckets[index] = self._convert_to_linked_list(bucket)

        # Handle the case where the bucket is a DoublyLinkedList
        elif isinstance(bucket, DoublyLinkedList):
            for node_data in bucket:
                if node_data[0] == key:
                    node_data = (key, value)  # Update the value
                    return

            bucket.append((key, value))
            self.size += 1

        # Resize if load factor exceeds threshold
        if self.size / self.capacity > 0.7:
            self._resize()

    def get(self, key: K) -> Optional[V]:
        """
        Retrieve the value associated with a key.

        :param key: The key to look up.
        :return: The value associated with the key, or None if the key does not exist.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        if isinstance(bucket, list):
            for k, v in bucket:
                if k == key:
                    return v

        elif isinstance(bucket, DoublyLinkedList):
            for k, v in bucket:
                if k == key:
                    return v

        return None

    def remove(self, key: K) -> None:
        """
        Remove a key-value pair from the HashMap.

        :param key: The key to remove.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        if isinstance(bucket, list):
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    self.size -= 1
                    return

        elif isinstance(bucket, DoublyLinkedList):
            current = bucket.head
            while current:
                if current.data[0] == key:
                    if current.prev:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                    if current == bucket.head:
                        bucket.head = current.next
                    if current == bucket.tail:
                        bucket.tail = current.prev
                    bucket.size -= 1
                    self.size -= 1
                    return

    def _resize(self) -> None:
        """
        Resize the HashMap when the load factor exceeds the threshold.
        """
        new_capacity = self.capacity * 2
        new_buckets: List[Union[List[Tuple[K, V]], DoublyLinkedList[Tuple[K, V]]]] = [
            [] for _ in range(new_capacity)
        ]

        for bucket in self.buckets:
            if isinstance(bucket, list):
                for key, value in bucket:
                    index = hash(key) % new_capacity
                    new_buckets[index].append((key, value))
            elif isinstance(bucket, DoublyLinkedList):
                for key, value in bucket:
                    index = hash(key) % new_capacity
                    new_buckets[index].append((key, value))

        self.buckets = new_buckets
        self.capacity = new_capacity

    def __len__(self) -> int:
        """
        Get the number of elements in the HashMap.

        :return: The number of key-value pairs in the HashMap.
        """
        return self.size

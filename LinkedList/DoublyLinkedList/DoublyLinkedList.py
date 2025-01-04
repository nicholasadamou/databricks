from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class ListNode(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next: Optional['ListNode[T]'] = None
        self.prev: Optional['ListNode[T]'] = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList(Generic[T]):
    def __init__(self, items: Optional[list[T]] = None):
        self.head: Optional[ListNode[T]] = None
        self.tail: Optional[ListNode[T]] = None
        self.size = 0

        if items is not None:
            for item in items:
                self.append(item)

    def __len__(self) -> int:
        return self.size

    def append(self, data: T) -> None:
        """
        Append a new node to the end of the list
        :param data: The data of the new node
        :return: The new node
        """
        new_node = ListNode(data)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def prepend(self, data: T) -> None:
        """
        Prepend a new node to the beginning of the list
        :param data: The data of the new node
        :return: The new node
        """
        new_node = ListNode(data)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert(self, index: int, data: T) -> None:
        """
        Insert a new node at the given index
        :param index: The index to insert the new node
        :param data: The data of the new node
        :return: The new node
        """
        if index < 0 or index > self.size:
            raise ValueError("Invalid index")

        if index == 0:
            self.prepend(data)
        elif index == self.size:
            self.append(data)
        else:
            new_node = ListNode(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next

            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

            self.size += 1

    def remove(self, index: int) -> None:
        """
        Remove the node at the given index
        :param index: The index to remove the node
        :return: The removed node
        """
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next

            current.prev.next = current.next
            current.next.prev = current.prev

        self.size -= 1

    def clear(self) -> None:
        """
        Clear the list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __getitem__(self, index: int) -> T:
        """
        Get the data of the node at the given index
        :param index: The index to get the data
        :return: The data of the node
        """
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index: int, data: T) -> None:
        """
        Set the data of the node at the given index
        :param index: The index to set the data
        :param data: The new data of the node
        """
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")

        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def __str__(self):
        if self.size == 0:
            return "Empty"

        current = self.head
        res = "["
        while current:
            res += str(current.data)
            if current.next:  # Only add a comma if there's a next element
                res += ", "
            current = current.next
        res += "]"

        return res

    def __iter__(self):
        current = self.head

        while current:
            yield current.data
            current = current.next

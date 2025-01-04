from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class ListNode(Generic[T]):
    def __init__(self, value: T = 0, nxt: 'Optional[ListNode[T]]' = None):
        self.value = value
        self.next = nxt

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class SinglyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[ListNode[T]] = None

    def add_at_head(self, data: T) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :param data: The data of the node to prepend
        :return: The linked list after the insertion
        """
        self.head = ListNode(data, self.head)

    def add_at_tail(self, data: T) -> None:
        """
        Add a node of value val to the last element of the linked list.
        :param data: The data of the node to append
        :return: The linked list after the insertion
        """
        if not self.head:
            self.head = ListNode(data)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(data)

    def add_at_index(self, index: int, data: T) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :param index: The index of the node to insert
        :param data: The data of the node to insert
        :return: The linked list after the insertion
        """
        if index < 0:
            return

        if index == 0:
            self.add_at_head(data)
            return

        current = self.head
        for _ in range(index - 1):
            if not current:
                return
            current = current.next

        if not current:
            return

        current.next = ListNode(data, current.next)

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        :param index: The index of the node to delete
        :return: The linked list after the deletion
        """
        if index < 0:
            return

        if index == 0 and self.head:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if not current:
                return
            current = current.next

        if not current or not current.next:
            return

        current.next = current.next.next

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return '->'.join(result)

    def __repr__(self):
        return self.__str__()

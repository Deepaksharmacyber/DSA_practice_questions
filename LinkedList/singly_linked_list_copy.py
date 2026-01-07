"""
File: singly_linked_list_copy.py
Author: Deepak Sharma
Description:
    Deep copy implementation of a singly linked list.

    The copied list is fully independent of the original list.

Time Complexity:
    O(n)

Space Complexity:
    O(n)
"""


class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        self.head = None

    def traversal(self, head=None):
        """
        Traverses and prints the linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = head if head else self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def create_duplicate_list(self):
        """
        Creates a deep copy of the linked list.

        Returns:
            Node: Head of the copied linked list

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        current = self.head
        dummy = Node(0)
        prev = dummy

        while current:
            new_node = Node(current.data)
            prev.next = new_node
            prev = new_node
            current = current.next

        return dummy.next


if __name__ == "__main__":
    ll = LinkedList()

    # Manually create list: 10 -> 20 -> 30 -> 40 -> 50
    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.head.next.next.next = Node(40)
    ll.head.next.next.next.next = Node(50)

    print("Original List:")
    ll.traversal()

    copied_head = ll.create_duplicate_list()

    print("\nCopied List:")
    ll.traversal(copied_head)

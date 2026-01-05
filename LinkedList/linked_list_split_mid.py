"""
Singly Linked List – Equal Split Using Slow and Fast Pointers

This implementation splits a singly linked list into two equal halves.
For even-length lists, both halves contain the same number of nodes.
For odd-length lists, the first half contains one extra node.

Time Complexity:
- Traversal: O(n)
- Split (find_mid): O(n)

Space Complexity:
- All operations use O(1) auxiliary space
"""


class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    Singly Linked List with traversal and equal split functionality.
    """

    def __init__(self):
        self.head = None

    def traversal(self, head=None):
        """
        Traverses and prints the linked list starting from the given head.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = head if head else self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find_mid(self):
        """
        Splits the linked list into two halves using the slow-fast pointer technique.

        - First half remains attached to self.head
        - Second half is returned as a new head

        For even-length lists:
            Equal split is guaranteed.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None or self.head.next is None:
            return None

        slow = self.head
        fast = self.head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None

        return second_head


if __name__ == "__main__":
    ll = LinkedList()

    # Build linked list from values
    values = [0, 1, 2, 3, 4, 5, 6]

    ll.head = Node(values[0])
    current = ll.head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    print("Original List:")
    ll.traversal()

    second_half = ll.find_mid()

    print("\nFirst Half:")
    ll.traversal()

    print("\nSecond Half:")
    ll.traversal(second_half)

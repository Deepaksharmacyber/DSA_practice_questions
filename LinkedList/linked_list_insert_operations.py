class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # -------------------------
    # READ (Traversal)
    # -------------------------
    def traversal(self):
        """
        Traverses the linked list and prints elements

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # -------------------------
    # INSERT OPERATIONS
    # -------------------------

    def insert_at_beginning(self, data):
        """
        Inserts a node at the beginning of the list

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a node at the end of the list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        new_node = Node(data)

        # Case 1: Empty list
        if self.head is None:
            self.head = new_node
            return

        # Case 2: Non-empty list
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_at_position(self, data, pos):
        """
        Inserts a node at a specific position (0-based index)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Case 1: Insert at beginning
        if pos == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        # Traverse to (pos - 1)
        while current is not None and count < pos - 1:
            current = current.next
            count += 1

        # Case 2: Invalid position
        if current is None:
            print("Position out of range")
            return

        # Case 3: Insert in middle or end
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node


# -------------------------
# Testing INSERT operations
# -------------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Manually creating initial list: 10 -> 20 -> 30
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)

    ll.head = n1
    n1.next = n2
    n2.next = n3

    print("Original List:")
    ll.traversal()

    print("\nInsert at Beginning (5):")
    ll.insert_at_beginning(5)
    ll.traversal()

    print("\nInsert at End (40):")
    ll.insert_at_end(40)
    ll.traversal()

    print("\nInsert at Position 1 (15):")
    ll.insert_at_position(15, 1)
    ll.traversal()

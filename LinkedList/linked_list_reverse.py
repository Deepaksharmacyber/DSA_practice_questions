class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        """
        Traverses the linked list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        """
        Inserts a node at the end

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def reverse(self):
        """
        Reverses the linked list (ITERATIVE)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next     # store next
            current.next = prev          # reverse link
            prev = current               # move prev
            current = next_node          # move current

        self.head = prev

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    print("Original List:")
    ll.traversal()

    print("\nReversed List:")
    ll.reverse()
    ll.traversal()

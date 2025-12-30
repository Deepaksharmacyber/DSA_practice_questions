class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # -------------------------
    # Utility methods
    # -------------------------
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # -------------------------
    # DELETE OPERATIONS
    # -------------------------

    # 1️⃣ Delete at Beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return

        self.head = self.head.next

    # 2️⃣ Delete at End
    def delete_at_end(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return

        # If only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None

    # 3️⃣ Delete by Value (first occurrence)
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        # If value is at head
        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print("Value not found")


# -------------------------
# Testing the delete operations
# -------------------------
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    print("Original List:")
    ll.traverse()

    print("\nDelete at Beginning:")
    ll.delete_at_beginning()
    ll.traverse()

    print("\nDelete at End:")
    ll.delete_at_end()
    ll.traverse()

    print("\nDelete by Value (20):")
    ll.delete_by_value(20)
    ll.traverse()

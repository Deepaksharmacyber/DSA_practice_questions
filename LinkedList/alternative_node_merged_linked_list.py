class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def alternate_merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1

        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2

            if not l1_next:
                break

            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next

        return head


# ------------------ BEFORE MERGE ------------------

# List1: 2 -> 4 -> 6
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(6)

# List2: 10 -> 8
l2 = Node(10)
l2.next = Node(8)

print("Before merge:")
cur = l1
print("List1:", end=" ")
while cur:
    print(cur.data, end=" -> ")
    cur = cur.next
print("None")

cur = l2
print("List2:", end=" ")
while cur:
    print(cur.data, end=" -> ")
    cur = cur.next
print("None")


# ------------------ MERGE ------------------

ll = LinkedList()
merged_head = ll.alternate_merge(l1, l2)


# ------------------ AFTER MERGE ------------------

print("\nAfter merge:")
cur = merged_head
print("Merged:", end=" ")
while cur:
    print(cur.data, end=" -> ")
    cur = cur.next
print("None")

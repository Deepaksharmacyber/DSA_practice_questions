"""
Alternate Merge of Two Singly Linked Lists

This script demonstrates how to:
1. Create two independent linked lists
2. Merge them alternately (zig-zag merge)
3. Print lists before and after merging

Time Complexity: O(n + m)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self, head=None):
        current = head if head else self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

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


def build_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


if __name__ == "__main__":

    # -------- CREATE TWO SEPARATE LISTS --------

    values_1 = [0, 2, 4, 6]
    values_2 = [1, 3, 5]

    ll = LinkedList()

    list1_head = build_list(values_1)
    list2_head = build_list(values_2)

    print("List 1 (before merge):")
    ll.traversal(list1_head)

    print("\nList 2 (before merge):")
    ll.traversal(list2_head)

    # -------- ALTERNATE MERGE --------

    merged_head = ll.alternate_merge(list1_head, list2_head)

    print("\nAfter alternate merge:")
    ll.traversal(merged_head)

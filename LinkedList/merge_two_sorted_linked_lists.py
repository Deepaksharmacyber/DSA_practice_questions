"""
Merge Two Sorted Linked Lists
-----------------------------
Problem:
Given two sorted linked lists, merge them into one sorted linked list.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1, list2):
    """
    Merges two sorted linked lists and returns the head of the merged list.
    """

    # Dummy node to simplify merging
    dummy = ListNode(-1)
    current = dummy

    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # Attach remaining nodes (if any)
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


# ---------- Helper Functions ----------

def create_linked_list(values):
    """Creates a linked list from a Python list."""
    dummy = ListNode(-1)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(head):
    """Prints a linked list."""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# ---------- Example Usage ----------

if __name__ == "__main__":
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])

    print("List 1:")
    print_linked_list(list1)

    print("List 2:")
    print_linked_list(list2)

    merged_list = merge_two_sorted_lists(list1, list2)

    print("Merged List:")
    print_linked_list(merged_list)

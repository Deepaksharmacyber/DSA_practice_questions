"""
Reorder Linked List (In-Place)

Problem:
Reorder a singly linked list such that:
L0 → L1 → L2 → ... → Ln
becomes:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

Approach:
1. Find the middle of the linked list using slow and fast pointers
2. Reverse the second half of the list
3. Merge the two halves alternately

Time Complexity:
- O(n), where n is the number of nodes in the list

Space Complexity:
- O(1), in-place modification without extra memory
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        # -------- STEP 1: FIND MIDDLE --------
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None  # split the list

        # -------- STEP 2: REVERSE SECOND HALF --------
        prev = None
        current = second
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        second = prev

        # -------- STEP 3: MERGE TWO HALVES --------
        first = head
        while first and second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

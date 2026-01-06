"""
LeetCode: Remove Nth Node From End of List
Problem Link:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Approach:
- Use a dummy node to handle edge cases (like deleting the head).
- Traverse the linked list in a single pass.
- Maintain a gap of N nodes between pointers to locate the node to delete.

Time Complexity:
- O(n), where n is the number of nodes in the linked list.
  The list is traversed once.

Space Complexity:
- O(1)
  Only constant extra space is used (dummy node and pointers).
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node to simplify deletion of the head node
        dummy = ListNode(0)
        dummy.next = head

        count = 0
        prev = None
        current = dummy

        # Single traversal of the list
        while current:
            if count == n:
                prev = dummy
            elif prev:
                prev = prev.next

            current = current.next
            count += 1

        # Remove the target node
        if prev and prev.next:
            prev.next = prev.next.next

        return dummy.next

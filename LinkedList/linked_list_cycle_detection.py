# LeetCode Problem: Linked List Cycle Detection
# Problem Link (NeetCode): https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects whether the linked list has a cycle.
        Uses Floyd's Cycle Detection Algorithm (Tortoise and Hare).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            head (ListNode | None): The head of the linked list.
        
        Returns:
            bool: True if there is a cycle, otherwise False.
        """
        slow = head
        fast = head

        # Move through list with two pointers
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # slow and fast met → cycle exists
                return True

        # fast reached the end → no cycle
        return False


# Example Usage
if __name__ == "__main__":
    # Create list: 3 -> 2 -> 0 -> -4 → back to 1 (cycle)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle here

    solution = Solution()
    print(solution.hasCycle(node1))  # Expected Output: True

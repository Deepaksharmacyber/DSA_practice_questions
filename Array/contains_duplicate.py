from typing import List

class Solution:
    """
    LeetCode Problem 217: Contains Duplicate
    https://leetcode.com/problems/contains-duplicate/

    Given an integer array `nums`, return `True` if any value appears at least twice
    in the array, and return `False` if every element is distinct.

    Time Complexity: O(n)
        - We use a set to track seen values. 
        - Each lookup/add operation on a set is, on average, constant time.

    Space Complexity: O(n)
        - In the worst case (no duplicates), all elements are stored in the set.

    Example:
        Input: nums = [1, 2, 3, 1]
        Output: True

        Input: nums = [1, 2, 3, 4]
        Output: False
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the list contains any duplicates.

        Args:
            nums (List[int]): The list of integers to check.

        Returns:
            bool: True if duplicates exist, False otherwise.
        """
        seen = set()
        for n in nums:
            # If we've already seen this number, it's a duplicate
            if n in seen:
                return True
            # Otherwise, add it to the set of seen numbers
            seen.add(n)

        # No duplicates found
        return False

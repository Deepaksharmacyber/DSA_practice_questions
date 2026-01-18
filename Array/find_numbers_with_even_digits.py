"""
LeetCode Problem: Find Numbers with Even Number of Digits
Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Problem Statement:
Given an integer array nums, return how many numbers contain an even number of digits.

Example:
Input: nums = [12, 345, 2, 6, 7896]
Output: 2
Explanation: Only 12 and 7896 contain even number of digits.

Time Complexity: O(n * d)
- n: number of elements
- d: number of digits (since we convert integer to string)

Space Complexity: O(1)
- Constant extra space is used.
"""

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Counts how many numbers in the list contain an even number of digits.

        :param nums: List of integers
        :return: Count of numbers with even number of digits
        """
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

"""
LeetCode Problem: Running Sum of 1D Array
Link: https://leetcode.com/problems/running-sum-of-1d-array/

Problem Statement:
Given an array nums, return the running sum of nums.
The running sum of an array is defined as:
runningSum[i] = sum(nums[0] + nums[1] + ... + nums[i])

Example:
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]

Time Complexity: O(n)
- We traverse the array once.

Space Complexity: O(n)
- A new list is used to store the running sum.
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Computes the running sum of a 1D array.

        :param nums: List of integers
        :return: List containing running sums
        """
        result_array = [nums[0]]

        for i in range(1, len(nums)):
            result_array.append(nums[i] + result_array[i - 1])

        return result_array

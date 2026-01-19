"""
LeetCode Problem: Kids With the Greatest Number of Candies
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Problem Statement:
Given an integer array candies, where candies[i] represents the number of candies
the i-th kid has, and an integer extraCandies, return a boolean array result.
result[i] is True if, after giving the i-th kid all the extraCandies,
they will have the greatest number of candies among all kids.

Example:
Input: candies = [2, 3, 5, 1, 3], extraCandies = 3
Output: [True, True, True, False, True]

Time Complexity: O(n)
- Finding the maximum and iterating through the list once.

Space Complexity: O(n)
- A result list is used to store boolean values.
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Determines which kids can have the greatest number of candies.

        :param candies: List of candies each kid has
        :param extraCandies: Extra candies available
        :return: List of booleans indicating if each kid can have the maximum candies
        """
        max_candies = max(candies)
        return [(candy + extraCandies) >= max_candies for candy in candies]

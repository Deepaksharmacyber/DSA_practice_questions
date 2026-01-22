"""
LeetCode Problem: Richest Customer Wealth
Link: https://leetcode.com/problems/richest-customer-wealth/

Problem Statement:
You are given an m x n integer grid accounts where accounts[i][j] is the amount
of money the i-th customer has in the j-th bank.
Return the wealth that the richest customer has.

A customer's wealth is the sum of money in all their bank accounts.

Example:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

Time Complexity: O(m * n)
- m: number of customers
- n: number of banks per customer

Space Complexity: O(1)
- No extra space used.
"""

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Returns the maximum wealth among all customers.

        :param accounts: 2D list representing customer bank balances
        :return: Maximum customer wealth
        """
        max_wealth = 0

        for customer in accounts:
            customer_wealth = sum(customer)
            max_wealth = max(max_wealth, customer_wealth)

        return max_wealth

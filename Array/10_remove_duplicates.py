"""
Problem: Remove Duplicates from Sorted Array

LeetCode:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Difficulty: Easy
Pattern: Two Pointers

Problem Statement:
Given a sorted array of integers, remove the duplicates in-place
such that each unique element appears only once.

Return the number of unique elements.

The first k elements of the array should contain the unique elements.

Example:
Input:
    [1, 1, 2, 2, 3]

Output:
    k = 3
    Array:
    [1, 2, 3, ...]

Approach:
Use two pointers:

- p1: points to the position of the last unique element.
- p2: scans the array to find the next unique element.

When arr[p1] != arr[p2], a new unique element is found.
Move p1 forward and copy arr[p2] to arr[p1].

Since the array is sorted, duplicates are adjacent.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def remove_duplicates(arr):
    p1 = 0

    for p2 in range(1, len(arr)):
        if arr[p1] != arr[p2]:
            p1 += 1
            arr[p1] = arr[p2]

    return p1 + 1


# Test Case
arr = [1, 1, 2, 2, 3]

k = remove_duplicates(arr)

print("Number of unique elements:", k)
print("Unique elements:", arr[:k])
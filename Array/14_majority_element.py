"""
LeetCode 169: Majority Element

Problem:
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than n / 2
    times in the array.

    You may assume that the majority element always exists.

LeetCode:
    https://leetcode.com/problems/majority-element/

Approach:
    HashMap / Dictionary

    1. Count the frequency of each element using a dictionary.
    2. Find the element whose frequency is greater than n / 2.

Complexity:
    Time:  O(n)
    Space: O(n)
"""


def majority_element(nums: list[int]) -> int:
    """
    Find the majority element in the array.

    Args:
        nums: List of integers.

    Returns:
        The element that appears more than n / 2 times.
    """

    frequency = {}

    # Count the frequency of each element.
    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1

    majority_threshold = len(nums) // 2

    # Find the element whose frequency is greater than n / 2.
    for num in frequency:
        if frequency[num] > majority_threshold:
            return num

    raise ValueError("Majority element not found.")


if __name__ == "__main__":
    nums = [3, 2, 3]

    result = majority_element(nums)

    print(result)

    # Output:
    # 3
"""
LeetCode 1: Two Sum

Problem:
    Given an array of integers nums and an integer target, return the
    indices of the two numbers such that they add up to target.

    Each input has exactly one solution, and the same element cannot
    be used twice.

LeetCode:
    https://leetcode.com/problems/two-sum/

Approach:
    HashMap / Dictionary

    For each number:
        1. Calculate the value needed to reach the target.
        2. Check if that value has already been seen.
        3. If found, return the stored index and current index.
        4. Otherwise, store the current number and its index.

Complexity:
    Time:  O(n)
    Space: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two indices whose values add up to the target.

    Args:
        nums: List of integers.
        target: Target sum.

    Returns:
        A list containing the indices of the two numbers.

    Raises:
        ValueError: If no valid pair is found.
    """

    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    raise ValueError("No valid two-sum pair found.")


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    result = two_sum(nums, target)

    print(result)

    # Output:
    # [0, 1]
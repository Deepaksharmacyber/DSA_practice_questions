"""
LeetCode 53: Maximum Subarray

Problem:
    Given an integer array nums, find the subarray with the largest sum
    and return its sum.

LeetCode:
    https://leetcode.com/problems/maximum-subarray/

Approach:
    Kadane's Algorithm

    At each element, decide whether to:
        1. Start a new subarray from the current element.
        2. Continue the previous subarray.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


def max_subarray_if_else(nums: list[int]) -> int:
    """
    Find the maximum subarray sum using explicit if/else logic.

    Args:
        nums: List of integers.

    Returns:
        The maximum sum of a contiguous subarray.
    """

    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        # Compare:
        # 1. Start a new subarray: nums[i]
        # 2. Continue the current subarray: current_sum + nums[i]
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
        else:
            current_sum += nums[i]

        # Update the best sum found so far.
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def max_subarray(nums: list[int]) -> int:
    """
    Find the maximum subarray sum using the concise Kadane approach.

    Args:
        nums: List of integers.

    Returns:
        The maximum sum of a contiguous subarray.
    """

    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        # Choose between starting a new subarray
        # or continuing the current subarray.
        current_sum = max(num, current_sum + num)

        # Keep track of the best sum found so far.
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # Method 1: Explicit if/else logic
    result_if_else = max_subarray_if_else(nums)
    print("If/Else Method:", result_if_else)

    # Method 2: Concise Kadane's Algorithm
    result_max = max_subarray(nums)
    print("Max Method:", result_max)

    # Expected Output:
    # If/Else Method: 6
    # Max Method: 6
"""
LeetCode 189: Rotate Array

Problem:
    Given an integer array nums, rotate the array to the right by k steps,
    where k is a non-negative integer.

LeetCode:
    https://leetcode.com/problems/rotate-array/

Approach:
    Three Reversals

    1. Reverse the entire array.
    2. Reverse the first k elements.
    3. Reverse the remaining elements.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


def reverse_array(nums: list[int], left: int, right: int) -> None:
    """
    Reverse a portion of the array in-place.

    Args:
        nums: List of integers to modify.
        left: Starting index of the portion to reverse.
        right: Ending index of the portion to reverse.

    Returns:
        None. The array is modified in-place.
    """

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]

        left += 1
        right -= 1


def rotate(nums: list[int], k: int) -> None:
    """
    Rotate the array to the right by k steps.

    Args:
        nums: List of integers to rotate.
        k: Number of positions to rotate to the right.

    Returns:
        None. The array is modified in-place.
    """

    if not nums:
        return

    k %= len(nums)

    # Step 1: Reverse the entire array.
    reverse_array(nums, 0, len(nums) - 1)

    # Step 2: Reverse the first k elements.
    reverse_array(nums, 0, k - 1)

    # Step 3: Reverse the remaining elements.
    reverse_array(nums, k, len(nums) - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    rotate(nums, k)

    print(nums)

    # Output:
    # [5, 6, 7, 1, 2, 3, 4]
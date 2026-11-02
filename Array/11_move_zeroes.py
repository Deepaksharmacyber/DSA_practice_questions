"""
LeetCode 283: Move Zeroes

Problem:
    Move all zeroes to the end of the array while maintaining
    the relative order of the non-zero elements.

LeetCode:
    https://leetcode.com/problems/move-zeroes/

Approach:
    Two Pointers

    p1 -> Points to the position where the next non-zero element
          should be placed.

    p2 -> Scans through the array to find non-zero elements.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


def move_zeroes(nums: list[int]) -> None:
    """
    Move all zeroes to the end of nums in-place.

    Args:
        nums: List of integers to modify.

    Returns:
        None. The input list is modified in-place.
    """

    p1 = 0
    p2 = 1

    while p2 < len(nums):

        # If p1 is pointing to zero and p2 finds a non-zero,
        # swap them and move p1 forward.
        if nums[p1] == 0 and nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1

        p2 += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]

    move_zeroes(nums)

    print(nums)

    # Output:
    # [1, 3, 12, 0, 0]
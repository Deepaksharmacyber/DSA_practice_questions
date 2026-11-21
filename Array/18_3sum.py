
"""
18 - 3Sum

LeetCode:
https://leetcode.com/problems/3sum/

LeetCode #: 15
Difficulty: Medium

Pattern:
- Sorting
- Two Pointers
- Duplicate Handling

Problem:
Given an integer array nums, find all unique triplets
[nums[i], nums[j], nums[k]] such that:

    nums[i] + nums[j] + nums[k] == 0

The solution must not contain duplicate triplets.

Example:
Input:
    [-1, 0, 1, 2, -1, -4]

Output:
    [[-1, -1, 2], [-1, 0, 1]]

Approach:
1. Sort the array.
2. Fix one number using index i.
3. Use two pointers (left and right) to find the other two numbers.
4. If the sum is less than 0, move left forward.
5. If the sum is greater than 0, move right backward.
6. If the sum is 0, store the triplet and move both pointers.
7. Skip duplicate values to avoid duplicate triplets.

Time Complexity:
    O(n²)

Space Complexity:
    O(1) auxiliary space
    (excluding the space used by the output)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []

        for i in range(len(nums) - 2):

            # Skip duplicate fixed values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result


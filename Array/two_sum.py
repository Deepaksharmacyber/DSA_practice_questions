from typing import List

class Solution:
    """
    Two Sum (LeetCode Problem 1)

    Problem Link:
    https://leetcode.com/problems/two-sum/

    Problem:
    Given an array of integers `nums` and an integer `target`,
    return indices of the two numbers such that they add up to `target`.

    Assumptions:
    - Each input has exactly one solution.
    - You may not use the same element twice.
    - The answer can be returned in any order.

    Approach:
    - Use a hash map (dictionary) to store numbers and their indices.
    - For each number, calculate the difference needed to reach the target.
    - If the difference exists in the dictionary, return the stored index
      and the current index.

    Time Complexity: O(n)
        - Each element is processed once.
        - Dictionary lookup is O(1) on average.

    Space Complexity: O(n)
        - Dictionary stores up to n elements.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in d:
                return [d[difference], i]
            else:
                d[nums[i]] = i


# Example usage (for local testing)
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    print(solution.twoSum(nums, target))  # Expected output: [0, 1]

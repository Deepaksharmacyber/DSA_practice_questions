class Solution:
    """
    Valid Anagram (NeetCode / LeetCode 242)
    Problem Link:
    https://leetcode.com/problems/valid-anagram/
    https://neetcode.io/problems/is-anagram/question?list=neetcode150

    Problem:
    Given two strings s and t, return True if t is an anagram of s,
    and False otherwise.

    Approach:
    - If the lengths of the strings are not equal, they cannot be anagrams.
    - Use a dictionary to store character frequencies from string `s`.
    - Decrement the frequency while iterating through string `t`.
    - If a character is missing or its count becomes negative, return False.
    - If all characters are balanced, return True.

    Time Complexity: O(n)
        - One pass to count characters in `s`
        - One pass to decrement counts using `t`

    Space Complexity: O(n)
        - Dictionary stores up to `n` unique characters
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}

        # Count characters in s
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] = d[ch] + 1

        # Decrement counts using t
        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch] = d[ch] - 1
                if d[ch] < 0:
                    return False

        return True


# Example usage (for local testing)
if __name__ == "__main__":
    s = "racecar"
    t = "carrace"

    solution = Solution()
    print(solution.isAnagram(s, t))  # Expected output: True

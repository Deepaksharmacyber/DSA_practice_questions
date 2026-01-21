"""
LeetCode Problem: Maximum Number of Words Found in Sentences
Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

Problem Statement:
A sentence is a list of words separated by a single space.
Given an array of strings sentences, return the maximum number of words
that appear in a single sentence.

Example:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks"]
Output: 5

Time Complexity: O(n)
- Each sentence is scanned once using a built-in C-optimized method.

Space Complexity: O(1)
- No extra space used apart from variables.
"""

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        """
        Returns the maximum number of words in any sentence.

        :param sentences: List of sentences
        :return: Maximum word count
        """
        return max(sentence.count(' ') + 1 for sentence in sentences)

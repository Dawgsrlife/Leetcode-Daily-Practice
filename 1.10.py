##############################################################################
# Author: AlexanderTheMango
# Date: January 10th, 2025
# Description: Word Subsets
# Leetcode Problem Link: https://leetcode.com/problems/word-subsets/description/
##############################################################################

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count_frequency(word: str) -> dict:
            freq = {}

            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            return freq

        required = {}
        for b in words2:
            b_count = count_frequency(b)
            for char, count in b_count.items():
                if char in required:
                    required[char] = max(required[char], count)
                else:
                    required[char] = count

        universal = []
        for a in words1:
            a_count = count_frequency(a)
            is_universal = True
            for char, count in required.items():
                if a_count.get(char, 0) < count:
                    is_universal = False
                    break
            if is_universal:
                universal.append(a)

        return universal

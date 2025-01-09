##############################################################################
# Author: AlexanderTheMango
# Date: January 8th, 2025
# Description: Count Prefix and Suffix Pairs I
# Leetcode Problem Link: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/?envType=daily-question&envId=2025-01-08
##############################################################################

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(
                        words[i]):
                    count += 1

        return count

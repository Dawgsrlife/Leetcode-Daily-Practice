##############################################################################
# Author: AlexanderTheMango
# Date: January 9th, 2025
# Description: Counting Words With a Given Prefix
# Leetcode Problem Link: https://leetcode.com/problems/counting-words-with-a-given-prefix/description/?envType=daily-question&envId=2025-01-09
##############################################################################

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(words)

        for i in range(n):
            if words[i].startswith(pref):
                count += 1

        return count

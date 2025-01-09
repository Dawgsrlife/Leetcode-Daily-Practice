##############################################################################
# Author: AlexanderTheMango
# Date: January 7th, 2025
# Description: String Matching in an Array
# Leetcode Problem Link: https://leetcode.com/problems/string-matching-in-an-array/submissions/1502412512/?envType=daily-question&envId=2025-01-07
##############################################################################

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        result = set()

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    result.add(words[i])
                    break

        return list(result)

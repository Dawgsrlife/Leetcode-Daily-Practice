##############################################################################
# Author: AlexanderTheMango
# Date: January 1st, 2025
# Description: Maximum Score After Splitting a String
# Leetcode Problem Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-01
##############################################################################

class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        left_zeros = left_ones = 0
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                left_ones += 1

            curr_score = left_zeros + (total_ones - left_ones)
            max_score = max(max_score, curr_score)

        return max_score

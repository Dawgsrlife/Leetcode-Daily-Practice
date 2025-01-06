##############################################################################
# Author: AlexanderTheMango
# Date: January 1st, 2025
# Description: Maximum Score After Splitting a String
# Leetcode Problem Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-01
##############################################################################

class Solution:
    def maxScore(self, s: str) -> int:
        zeros_seen, ones_seen = (1, 0) if s[0] == '0' else (0, 1)

        max_left_score = -1
        for i in range(1, len(s)):
            max_left_score = max(max_left_score, zeros_seen - ones_seen)
            zeros_seen += s[i] == '0'
            ones_seen += s[i] == '1'

        return max_left_score + ones_seen

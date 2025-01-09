##############################################################################
# Author: AlexanderTheMango
# Date: January 6th, 2025
# Description: Minimum Number of Operations to Move All Balls to Each Box
# Leetcode Problem Link: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/?envType=daily-question&envId=2025-01-06
##############################################################################

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Left-to-right pass
        balls = operations = 0
        for i in range(n):
            answer[i] = operations
            balls += boxes[i] == '1'
            operations += balls

        # Right-to-left pass
        balls = operations = 0
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            balls += boxes[i] == '1'
            operations += balls

        return answer

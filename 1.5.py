##############################################################################
# Author: AlexanderTheMango
# Date: January 5th, 2025
# Description: Shifting Letters II
# Leetcode Problem Link: https://leetcode.com/problems/shifting-letters-ii/description/?envType=daily-question&envId=2025-01-05
##############################################################################

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        # Apply shifts using the difference array
        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            diff[start] += shift
            if end + 1 < n:
                diff[end + 1] -= shift

        # Apply shifts directly while computing prefix sums
        result = []
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            # Apply the net shift to the current character
            new_char = chr(
                (ord(s[i]) - ord('a') + current_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)

##############################################################################
# Author: AlexanderTheMango
# Date: January 4th, 2025
# Description: Unique Length-3 Palindromic Subsequences
# Leetcode Problem Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-01-04
##############################################################################

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_set = set()
        right_count = [0] * 26  # Tracks count of each character to the right
        result_set = set()

        # Populate right_count with character frequencies
        for char in s:
            right_count[ord(char) - ord('a')] += 1

        # Iterate over the string with s[i] as the middle character
        for i, char in enumerate(s):
            right_count[ord(char) - ord('a')] -= 1  # Remove current character from right count

            # Check all possible left and right characters for palindrome
            for left_char in left_set:
                if right_count[ord(left_char) - ord('a')] > 0:
                    result_set.add(
                        (left_char, char, left_char))  # Add unique palindrome

            # Add current character to left set
            left_set.add(char)

        return len(result_set)

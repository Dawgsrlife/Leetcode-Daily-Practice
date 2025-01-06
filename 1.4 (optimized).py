##############################################################################
# Author: AlexanderTheMango
# Date: January 4th, 2025
# Descrpition: Unique Length-3 Palindromic Subsequences
# Leetcode Problem Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-01-04
##############################################################################

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Arrays to store the first and last occurrence of each character
        first_occurrence = [-1] * 26
        last_occurrence = [-1] * 26

        # Record first and last occurrence for each character
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            if first_occurrence[index] == -1:
                first_occurrence[index] = i
            last_occurrence[index] = i

        # Set to store unique palindromes
        result_set = set()

        # Iterate over all characters
        for char_index in range(26):
            start = first_occurrence[char_index]
            end = last_occurrence[char_index]
            if start != -1 and start < end:  # Valid range for a palindrome
                # Collect all unique middle characters
                middle_chars = set(s[start + 1:end])
                for middle_char in middle_chars:
                    result_set.add((chr(char_index + ord('a')), middle_char,
                                    chr(char_index + ord('a'))))

        return len(result_set)

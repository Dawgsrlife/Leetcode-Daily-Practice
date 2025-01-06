##############################################################################
# Author: AlexanderTheMango
# Date: January 2nd, 2025
# Descrpition: Count Vowel Strings in Ranges
# Leetcode Problem Link: https://leetcode.com/problems/count-vowel-strings-in-ranges/description/?envType=daily-question&envId=2025-01-02
##############################################################################

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')  # O(1) lookup time.

        # Iterate through words:
        prefix_sums = [0]
        for word in words:
            # Determine if this word is a vowel string.
            is_vowel_string = word[0] in vowels and word[-1] in vowels
            # Compute the cumulative counts of matches up to each index.
            prefix_sums.append(prefix_sums[-1] + (1 if is_vowel_string else 0))

        # Use <prefix_sums> to produce results for the query.
        # Note that the right index is inclusive.
        return [prefix_sums[ri + 1] - prefix_sums[li] for li, ri in queries]

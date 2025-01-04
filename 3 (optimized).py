##############################################################################
# Author: AlexanderTheMango
# Date: January 3rd, 2025
# Descrpition: Number of Ways to Split Array
# Leetcode Problem Link: https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-02
##############################################################################

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        total_sum = sum(nums)
        valid_splits = 0
        right_sum = total_sum

        for num in nums[:-1]:  # Exclude last element, avoiding index checks
            prefix_sum += num
            right_sum -= num
            if prefix_sum >= right_sum:
                valid_splits += 1

        return valid_splits

##############################################################################
# Author: AlexanderTheMango
# Date: January 3rd, 2025
# Descrpition: Number of Ways to Split Array
# Leetcode Problem Link: https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-02
##############################################################################

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        cumulative_sum = 0
        valid_splits = 0

        for i in range(len(nums) - 1):  # Stop at n-1 to ensure the right part is non-empty
            cumulative_sum += nums[i]
            right_sum = total_sum - cumulative_sum
            if cumulative_sum >= right_sum:
                valid_splits += 1

        return valid_splits

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        diff_set = set()
        if len(nums) < 2:
            return 0
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)):
            diff = sorted_nums[i] - sorted_nums[i - 1]
            diff_set.add(diff)

        return max(diff_set)





from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        max_val = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i - 1] > nums[i]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1

            max_val = max(max_val, inc, dec)

        return max_val

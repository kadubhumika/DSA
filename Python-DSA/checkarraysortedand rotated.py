from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:

        n = len(nums)
        break_point = 0

        for i in range(n-1):

            if nums[i] > nums[i+1]:
                break_point += 1

        # circular check (last → first)
        if nums[n-1] > nums[0]:
            break_point += 1

        if break_point <= 1:
            return True

        return False
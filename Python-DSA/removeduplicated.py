from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for num in nums:

            if j < 2 or num != nums[j - 2]:
                nums[j] = num
                j += 1
        return j

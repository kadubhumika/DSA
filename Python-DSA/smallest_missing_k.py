from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        multiple = k
        while True:
            if multiple not in nums_set:
                return multiple
            multiple += k







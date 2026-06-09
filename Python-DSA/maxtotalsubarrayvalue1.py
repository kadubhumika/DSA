from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # One pass to find both min and max
        min_num = float('inf')
        max_num = float('-inf')

        for num in nums:
            if num < min_num: min_num = num
            if num > max_num: max_num = num

        return (max_num - min_num) * k

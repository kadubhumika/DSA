from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        i, j = min(min_idx, max_idx), max(max_idx, min_idx)
        del_both_left = j + 1

        del_both_right = n - i
        del_mixed = (i + 1) + (n - j)
        return min(del_both_left, del_both_right, del_mixed)

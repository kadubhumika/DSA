from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        n = len(nums)
        for num in nums:
            total_xor ^= num

        if total_xor != 0:
            return n

        output = []
        for i in range(len(nums)):
            if total_xor ^ nums[i] != 0:
                output.append(nums[i])

        if len(output) > 0:
            return n - 1
        else:
            return 0


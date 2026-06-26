from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')
        current_sum = 0
        left = 0

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                current_length = right - left + 1
                min_length = min(min_length, current_length)

                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0

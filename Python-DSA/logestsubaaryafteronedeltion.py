class Solution(object):
    def longestSubarray(self, nums):
        n = len(nums)
        zero_Count = 0
        left = 0
        max_length = 0

        for right in range(n):
            if nums[right] == 0:
                zero_Count += 1

            while zero_Count > 1:
                if nums[left] == 0:
                    zero_Count -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length

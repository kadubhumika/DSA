class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # oaky i understood the question here we will apply dp loggic computatation
        if not nums:
            return 0
        max_val = 1
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)





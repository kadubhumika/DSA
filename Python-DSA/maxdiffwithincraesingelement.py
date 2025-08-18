class Solution(object):
    def maximumDifference(self, nums):
        n = len(nums)
        maxDiff = -1

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    maxDiff = max(maxDiff, diff)

        return maxDiff

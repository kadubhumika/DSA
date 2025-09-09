class Solution(object):
    def findMaxAverage(self, nums, k):
        total_sum = sum(nums[:k])
        max_sum = total_sum

        for i in range(k, len(nums)):
            total_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, total_sum)

        return float(max_sum) / k




class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        if all(x < 0 for x in nums):
            return max(nums)

        if all(x >= 0 for x in nums):
            return sum(nums)

        total_sum = sum(nums)

        max_sum = nums[0]
        current_max = nums[0]

        min_sum = nums[0]
        current_min = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_sum = max(max_sum, current_max)

            current_min = min(nums[i], current_min + nums[i])
            min_sum = min(min_sum, current_min)

        wrapped_max_sum = total_sum - min_sum

        return max(max_sum, wrapped_max_sum)

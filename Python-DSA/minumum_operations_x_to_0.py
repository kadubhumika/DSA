class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        left = 0
        prefix_sum = 0
        max_len = -1
        for right in range(len(nums)):
            prefix_sum += nums[right]
            while prefix_sum > target and left <= right:
                prefix_sum -= nums[left]
                left += 1
            if prefix_sum == target:
                max_len = max(max_len, right - left + 1)
        return len(nums) - max_len if max_len != -1 else -1


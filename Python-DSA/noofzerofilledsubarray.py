class Solution(object):
    def zeroFilledSubarray(self, nums):
        total = 0
        streak = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                streak += 1
                total += streak
            else:
                streak = 0

        return total

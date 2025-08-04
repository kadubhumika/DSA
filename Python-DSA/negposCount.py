class Solution(object):
    def maximumCount(self, nums):
        negCount = 0
        posCount = 0

        for i in range(len(nums)):
            if nums[i] < 0:
                negCount += 1
            elif nums[i] > 0:
                posCount += 1

        return max(negCount, posCount)

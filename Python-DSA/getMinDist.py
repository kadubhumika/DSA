class Solution(object):
    def getMinDistance(self, nums, target, start):
        left = start
        right = start
        sum_min = float('inf')
        n = len(nums)

        while left >= 0 or right < n:
            if left >= 0:
                if nums[left] == target:
                    sum_min = min(sum_min, abs(left - start))
                left -= 1

            if right < n:
                if nums[right] == target:
                    sum_min = min(sum_min, abs(right - start))
                right += 1

        return sum_min
class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        max_Count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    mul = i * j
                    if mul % k == 0:
                        count += 1
        max_Count = max(max_Count, count)
        return max_Count






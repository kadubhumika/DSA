class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        divisible_by_3 = []
        for num in nums:
            if num % 3 != 0:
                divisible_by_3.append(nums)
        return len(divisible_by_3)



class Solution(object):
    def subsetXORSum(self, nums):
        n = len(nums)
        total_sum = 0

        for mask in range(1 << n):
            xor_val = 0
            for i in range(n):
                if mask & (1 << i):
                    xor_val ^= nums[i]
            total_sum += xor_val

        return total_sum
    

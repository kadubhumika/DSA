class Solution(object):
    def minimumOperations(self, nums):
        from collections import Counter

        operations = 0
        while len(nums) > 0:

            if len(nums) == len(set(nums)):
                return operations

            remove_count = min(3, len(nums))
            for _ in range(remove_count):
                nums.pop(0)

            operations += 1

        return operations

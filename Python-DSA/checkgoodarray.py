from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # okay i understood the problem basically

        # first find maximum number
        n = max(nums)

        # helper function to create base array
        def base_fun(n):

            arr = []

            for i in range(1, n):
                arr.append(i)

            arr.append(n)
            arr.append(n)

            return arr

        result = base_fun(n)

        if len(result) != len(nums):
            return False

        result.sort()
        nums.sort()

        if result == nums:
            return True

        return False
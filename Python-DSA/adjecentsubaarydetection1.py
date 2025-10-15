class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        length = len(nums)

        def check_increasing_order(array):
            n = len(array)
            for i in range(n - 1):
                if array[i + 1] <= array[i]:
                    return False
            return True

        for a in range(0, length - 2 * k + 1):
            subarry_first = nums[a:a + k]
            subarry_second = nums[a + k:a + 2 * k]

            if check_increasing_order(subarry_first) and check_increasing_order(subarry_second):
                return True

        return False

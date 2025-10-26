class Solution(object):
    def searchRange(self, nums, target):
        # main function: will call two helper functions
        # left_bound -> find first occurrence
        # right_bound -> find last occurrence

        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            left_most = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left_most = mid
                    right = mid - 1  # move left to find earlier occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left_most

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            right_most = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right_most = mid
                    left = mid + 1  # move right to find later occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right_most

        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)

        return [left_index, right_index]

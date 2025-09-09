class Solution(object):
    def maximumUniqueSubarray(self, nums):
        seen = set()  # Track unique elements in current window
        current_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            num = nums[right]

            # If duplicate found, remove elements from the left until duplicate removed
            while num in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Add current number
            seen.add(num)
            current_sum += num

            # Update max_sum
            max_sum = max(max_sum, current_sum)

        return max_sum

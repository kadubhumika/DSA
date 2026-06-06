from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # 1. Get the total sum of all numbers first
        total_sum = sum(nums)

        # 2. Start left_sum at 0 because there is nothing to the left of index 0
        left_sum = 0
        result = []

        for num in nums:
            # 3. Right sum is: (Total) - (Left Sum) - (Current Number)
            right_sum = total_sum - left_sum - num

            # 4. Calculate the absolute difference
            diff = abs(left_sum - right_sum)
            result.append(diff)

            # 5. Crucial Step: Add the current number to left_sum for the next turn
            left_sum += num

        return result

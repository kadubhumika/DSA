class Solution:
    def minElement(self, nums: list[int]) -> int:
        min_check = float('inf')

        for num in nums:
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10  # Gets the last digit
                num = num // 10  # Removes the last digit

            if digit_sum < min_check:
                min_check = digit_sum

        return min_check

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        total_sum = 0
        result_int = 0
        place_value = 1  # Tracks units, tens, hundreds place

        while n > 0:
            d = n % 10
            if d > 0:
                total_sum += d
                result_int += d * place_value
                place_value *= 10  # Move to the next column to the left
            n = n // 10

        return total_sum * result_int

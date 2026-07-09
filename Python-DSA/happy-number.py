class Solution:
    def isHappy(self, n: int) -> bool:

        seen_sums = set()

        while n != 1 and n not in seen_sums:
            seen_sums.add(n)

            sumUp = 0
            while n > 0:
                digit = n % 10  # Get the last digit
                sumUp += digit ** 2  # Add its square to your sumUp
                n = n // 10  # Move to the next digit

            n = sumUp

        return n == 1

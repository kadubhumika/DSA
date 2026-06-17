class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1. Convert the integer number into a binary string fast
        binary_string = bin(n)  # Example: 11 becomes '0b1011'

        # 2. Use the count() function to count all the '1' digits instantly
        return binary_string.count('1')

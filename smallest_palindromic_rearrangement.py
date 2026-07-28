class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        half_len = n // 2

        sorted_half = sorted(s[:half_len])

        mid_char = s[half_len] if n % 2 == 1 else ""

        result = "".join(sorted_half) + mid_char + "".join(sorted_half[::-1])

        return result

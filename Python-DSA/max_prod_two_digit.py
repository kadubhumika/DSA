class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]

        if len(digits) < 2:
            return 0

        sorted_n = sorted(digits, reverse=True)

        return sorted_n[0] * sorted_n[1]

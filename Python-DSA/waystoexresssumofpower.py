class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case

        for i in range(1, n + 1):
            val = i ** x
            if val > n:
                break

            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % MOD

        return dp[n]

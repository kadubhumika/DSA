class Solution:
    def tribonacci(self, n: int) -> int:

        hash_map = {}

        def solve(n):

            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1

            if n in hash_map:
                return hash_map[n]

            output = solve(n-1) + solve(n-2) + solve(n-3)

            hash_map[n] = output

            return output

        return solve(n)
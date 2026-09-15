class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # okay i understood the qesution nicley
        final_array = [1]
        flattened_grid = [0] * len(primes)
        while len(final_array) < n:
            candidates = []
            for i in range(len(primes)):
                mul_val = primes[i] * final_array[flattened_grid[i]]
                candidates.append(mul_val)
            min_val = min(candidates)
            final_array.append(min_val)
            for i in range(len(primes)):
                if candidates[i] == min_val:
                    flattened_grid[i] += 1
        return final_array[n - 1]








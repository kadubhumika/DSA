from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]):

        memo = {}

        def solve(i):

            # reached top
            if i >= len(cost):
                return 0

            # memoization
            if i in memo:
                return memo[i]

            # choice 1 -> jump one step
            one_jump = cost[i] + solve(i+1)

            # choice 2 -> jump two steps
            jump_two = cost[i] + solve(i+2)

            # choose minimum
            min_cost = min(one_jump, jump_two)

            memo[i] = min_cost

            return min_cost

        return min(solve(0), solve(1))
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        cost.sort()

        total_cost = 0

        for i in range(len(cost) - 1, -1, -1):

            if (len(cost) - i) % 3 == 0:
                continue  # "Remove" the element by skipping it (getting it for free)

            total_cost += cost[i]

        return total_cost

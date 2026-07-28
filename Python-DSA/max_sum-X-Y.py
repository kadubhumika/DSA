from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        hash_map = {}

        for key, val in zip(x, y):
            hash_map[key] = max(hash_map.get(key, float('-inf')), val)

        if len(hash_map) < 3:
            return -1

        distinct_max_values = sorted(hash_map.values(), reverse=True)

        return sum(distinct_max_values[:3])

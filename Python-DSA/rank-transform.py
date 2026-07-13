from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique_arr = sorted(list(set(arr)))

        rank_map = {}
        for rank, num in enumerate(sorted_unique_arr, 1):
            rank_map[num] = rank

        return [rank_map[num] for num in arr]



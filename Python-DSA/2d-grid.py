from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid:
            return []

        m, n = len(grid), len(grid[0])
        total_elements = m * n
        k = k % total_elements

        flat_list = [val for row in grid for val in row]

        shifted_flat = flat_list[total_elements - k:] + flat_list[:total_elements - k]

        res = []
        for i in range(0, total_elements, n):
            res.append(shifted_flat[i: i + n])

        return res

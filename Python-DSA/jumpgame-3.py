from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        visited = set()

        def dfs(index):
            if index < 0 or index >= len(arr):
                return False
            if index in visited:
                return False

            if arr[index] == 0:
                return True

            visited.add(index)

            return dfs(index + arr[index]) or dfs(index - arr[index])

        return dfs(start)
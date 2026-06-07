from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index: int, current_subset: List[int]):
            if index == len(nums):
                result.append(list(current_subset))
                return

            current_subset.append(nums[index])
            backtrack(index + 1, current_subset)

            current_subset.pop()

            backtrack(index + 1, current_subset)

        backtrack(0, [])
        return result

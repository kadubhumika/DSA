from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # okat i understood thequestion we wil use binary tree things to get and log n
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = (row * col) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // col
            mid_col = mid % col
            mid_val = matrix[mid_row][mid_col]

            if mid_val == target:
                return True

            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False






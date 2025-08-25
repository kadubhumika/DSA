from collections import defaultdict


class Solution(object):
    def findDiagonalOrder(self, mat):
        row = len(mat)
        column = len(mat[0])
        diagonal_matrix = defaultdict(list)
        result = []

        for i in range(row):
            for j in range(column):
                diagonal_matrix[i + j].append(mat[i][j])

        for k in range(row + column - 1):
            if k % 2 == 0:

                result.extend(diagonal_matrix[k][::-1])
            else:
                result.extend(diagonal_matrix[k])
        return result

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        max_area = 0
        max_diagonal = 0
        for length, width in dimensions:
            area = length * width
            diagonal_length = length * length + width * width

            if diagonal_length > max_diagonal:
                max_diagonal = diagonal_length
                max_area = area
            elif diagonal_length == max_diagonal:
                max_area = max(max_area, area)
        return max_area




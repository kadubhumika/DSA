class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        nums_count = {}

        for row in grid:
            for num in row:
                nums_count[num] = nums_count.get(num, 0) + 1

        repeated = -1
        missing = -1

        for i in range(1, n * n + 1):
            count = nums_count.get(i, 0)
            if count == 2:
                repeated = i
            elif count == 0:
                missing = i

        return [repeated, missing]

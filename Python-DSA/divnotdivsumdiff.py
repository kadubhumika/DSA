class Solution(object):
    def differenceOfSums(self, n, m):
        divisible_Sum = 0
        not_divisible_Sum = 0

        for i in range(1, n + 1):
            if i % m == 0:
                divisible_Sum += i
            else:
                not_divisible_Sum += i

        diff = not_divisible_Sum-divisible_Sum
        return diff

class Solution(object):
    def getNoZeroIntegers(self, n):
        res = []
        non_zero_box = []

        for i in range(1, n + 1):
            if '0' not in str(i):
                non_zero_box.append(i)

        for a in non_zero_box:
            for b in non_zero_box:
                if a + b == n:
                    res.append(a)
                    res.append(b)
                    return res

        return res


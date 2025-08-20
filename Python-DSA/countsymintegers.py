class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0

        for num in range(low, high + 1):
            s = str(num)
            n = len(s)

            if n % 2 == 0:
                left_sum = sum(int(d) for d in s[:n//2])
                right_sum = sum(int(d) for d in s[n//2:])
                if left_sum == right_sum:
                    count += 1

        return count

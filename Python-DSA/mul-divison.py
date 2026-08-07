class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            mul_ans = 1

            while temp > 0:
                digit = temp % 10
                mul_ans *= digit
                temp //= 10

            if mul_ans % t == 0:
                return n
            n += 1

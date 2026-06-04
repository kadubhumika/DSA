class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        output = 0
        num = num1

        while num <= num2:

            s = str(num)

            if len(s) >= 3:

                k = 1

                while k < len(s) - 1:

                    if ((s[k] > s[k-1] and s[k] > s[k+1]) or
                        (s[k] < s[k-1] and s[k] < s[k+1])):

                        output += 1

                    k += 1

            num += 1

        return output
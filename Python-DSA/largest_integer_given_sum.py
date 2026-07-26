class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n:
            return -1
        if s == 0:
            return 0

        single_arr = [0] * n
        running_sum = 0

        for i in range(n):
            digit = 9

            while digit >= 0:
                if running_sum + digit <= s:
                    single_arr[i] = digit
                    running_sum += digit
                    break
                digit -= 1

        formed_num = 0
        for num in single_arr:
            formed_num = formed_num * 10 + num

        return formed_num


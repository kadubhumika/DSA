class Solution(object):
    def hasSameDigits(self, s):
        n = len(s)

        while n > 2:
            new_s = ""
            for i in range(n - 1):
                two_digit_sum = int(s[i]) + int(s[i + 1])
                unit_digit_val = two_digit_sum % 10
                new_s += str(unit_digit_val)
            s = new_s
            n = len(s)

        if s[0] == s[1]:
            return True
        else:
            return False

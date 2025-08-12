class Solution(object):
    def minMaxDifference(self, num):
        s = str(num)

        for digit in s:
            if digit != '9':
                max_str = s.replace(digit, '9')
                break
        else:
            max_str = s

        first_digit = s[0]
        if first_digit != '0':
            min_str = s.replace(first_digit, '0')
        else:
            min_str = s

        return int(max_str) - int(min_str)

class Solution(object):
    def isPalindrome(self, x):
        original = x
        new_num = 0

        if x < 0:
            return False

        while x != 0:
            remainder = x % 10
            x = x // 10
            new_num = new_num * 10 + remainder

        return new_num == original

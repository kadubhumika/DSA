class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        # checking every base from 2 to n-2
        for base in range(2, n - 1):

            rem_box = []

            num = n

            # converting number into current base
            while num != 0:

                rem = num % base

                rem_box.append(rem)

                quotient = num // base

                num = quotient

            # palindrome check
            if rem_box != rem_box[::-1]:
                return False

        return True
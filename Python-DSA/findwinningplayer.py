class Solution:
    def winningPlayer(self, x: int, y: int) -> str:

        # same variables
        total_75 = x
        total_10 = y

        i = 1
        k = 4
        count = 0

        rem_75 = total_75
        rem_10 = total_10

        while rem_10 >= 4 and rem_75 > 0:

            rem_75 = total_75 - i
            rem_10 = total_10 - k

            total_75 = rem_75
            total_10 = rem_10

            count += 1

        if count % 2 == 0:
            return "Bob"
        else:
            return "Alice"
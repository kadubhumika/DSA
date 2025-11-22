class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):

            profit = prices[right] - prices[left]

            if profit > 0:
                max_profit = max(max_profit, profit)
            else:

                left = right

            # always move right forward
            right += 1

        return max_profit

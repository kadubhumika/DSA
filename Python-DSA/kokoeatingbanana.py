import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        result = right  # start with max as a safe answer

        while left <= right:
            mid = (left + right) // 2
            total_hours = 0

            # calculate total hours needed at speed = mid
            for pile in piles:
                total_hours += math.ceil(pile / float(mid))

            # if she can finish in time or sooner
            if total_hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

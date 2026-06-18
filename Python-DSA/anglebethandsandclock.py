class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Convert hour 12 to 0
        if hour == 12:
            hour = 0

        angle = abs(30 * hour - 5.5 * minutes)

        return min(angle, 360 - angle)

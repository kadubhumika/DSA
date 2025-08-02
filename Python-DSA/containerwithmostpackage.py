class Solution(object):
    def maxArea(self, height):
        max_Area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_Area = max(max_Area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_Area

class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)

        right = n - 1
        while colors[0] == colors[right]:
            right -= 1
        dist1 = right

        left = 0

        while colors[n - 1] == colors[left]:
            left += 1
        dist2 = (n - 1) - left

        return max(dist1, dist2)

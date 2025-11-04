class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        left = 0
        n = len(colors)
        right = 1
        total_sum = 0

        while right < n:
            if colors[left] == colors[right]:
                if neededTime[left] < neededTime[right]:
                    total_sum += neededTime[left]
                    left = right
                else:
                    total_sum += neededTime[right]
                right += 1
            else:
                left = right
                right += 1
        return total_sum

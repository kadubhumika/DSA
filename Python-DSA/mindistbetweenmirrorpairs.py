class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dictionary to store the last seen position of a reversed number
        # Key: reversed_number, Value: index
        last_seen = {}
        min_dist = float('inf')
        found = False

        for i, num in enumerate(nums):
            # Check if this number is the reverse of a previous number
            if num in last_seen:
                dist = abs(i - last_seen[num])
                if dist < min_dist:
                    min_dist = dist
                found = True

            # Create the reversed number
            reversed_num = self.reverseNum(num)

            # Update the last seen position of the reversed number
            last_seen[reversed_num] = i

        return min_dist if found else -1

    def reverseNum(self, n):
        # Efficient digit reversal (e.g., 120 -> 21)
        res = 0
        while n:
            res = res * 10 + n % 10
            n //= 10
        return res


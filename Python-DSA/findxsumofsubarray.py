class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res = []
        n = len(nums)

        for i in range(n - k + 1):
            subarr = nums[i:i + k]

            freq = {}
            for num in subarr:
                freq[num] = freq.get(num, 0) + 1

            freq_items = list(freq.items())

            freq_items.sort(key=lambda x: (x[1], x[0]), reverse=True)

            top_x = freq_items[:x]

            s = 0
            for num, count in top_x:
                s += num * count

            res.append(s)

        return res

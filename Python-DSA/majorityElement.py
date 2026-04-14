class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter

        n = len(nums)
        freq = Counter(nums)

        result = list(filter(lambda x: freq[x] > n // 3, freq))
        return result
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_hash_map = {}
        res = []

        for val in nums:
            count_hash_map[val] = count_hash_map.get(val, 0) + 1
            if count_hash_map[val] == 2:
                res.append(val)

        return res

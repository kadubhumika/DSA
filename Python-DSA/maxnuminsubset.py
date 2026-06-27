from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for key in count.keys():
            if key == 1:

                total = count[key] if count[key] % 2 else count[key] - 1
            else:
                total = 0

                while count[key] >= 2:
                    total += 2
                    key = key * key

                if count[key] >= 1:
                    total += 1
                else:

                    total -= 1

            res = max(res, total)

        return res

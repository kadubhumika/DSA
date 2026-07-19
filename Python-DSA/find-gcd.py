import math
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # oaky i gost the losgic pattern tso solev this uqstion acolaiiy
        min_num = min(nums)
        max_num = max(nums)
        result = math.gcd(min_num,max_num)
        return result
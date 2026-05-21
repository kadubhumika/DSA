from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        output = 0

        prefix_set = set()

        # create prefixes from arr1
        for i in range(len(arr1)):

            s = str(arr1[i])

            temp = ""

            for ch in s:
                temp += ch
                prefix_set.add(temp)

        # check arr2 prefixes
        for i in range(len(arr2)):

            s = str(arr2[i])

            temp = ""

            for ch in s:

                temp += ch

                if temp in prefix_set:
                    output = max(output, len(temp))

        return output
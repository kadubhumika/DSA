from itertools import zip_longest


class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        # Removed list() to use memory-efficient map iterators directly
        v1_iter = map(int, v1.split('.'))
        v2_iter = map(int, v2.split('.'))

        for rev1, rev2 in zip_longest(v1_iter, v2_iter, fillvalue=0):
            if rev1 == rev2:
                continue

            return -1 if rev1 < rev2 else 1

        return 0

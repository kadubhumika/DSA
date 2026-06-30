class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        last_seen = {'a': -1, 'b': -1, 'c': -1}
        total_count = 0

        for current_index, char in enumerate(s):

            last_seen[char] = current_index

            min_index = min(last_seen['a'], last_seen['b'], last_seen['c'])

            if min_index >= 0:
                total_count += (min_index + 1)

        return total_count

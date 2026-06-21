from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):

            current_start, current_end = merged_intervals[-1]

            next_start, next_end = intervals[i]

            if current_end >= next_start:

                merged_intervals[-1][1] = max(current_end, next_end)
            else:

                merged_intervals.append([next_start, next_end])

        return merged_intervals

class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        unique_timestamps = sorted(list(set([t for t, v in series1] + [t for t, v in series2])))

        variable = unique_timestamps
        map1 = dict(series1)
        map2 = dict(series2)

        next_val1 = 0
        next_val2 = 0

        for t in reversed(variable):

            if t in map1:
                next_val1 = map1[t]
            else:
                map1[t] = next_val1

            if t in map2:
                next_val2 = map2[t]
            else:
                map2[t] = next_val2

        result_arr = []
        for t in variable:
            summed_value = map1[t] + map2[t]
            result_arr.append([t, summed_value])
        return result_arr




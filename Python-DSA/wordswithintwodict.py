class Solution(object):
    def twoEditWords(self, queries, dictionary):
        result = []

        for q in queries:
            for d in dictionary:
                diff = 0

                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff += 1
                        if diff > 2:
                            break  # no need to continue

                if diff <= 2:
                    result.append(q)
                    break  # move to next query

        return result
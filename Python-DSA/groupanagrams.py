from collections import defaultdict


def groupAnagrams(self, strs):
    anagrams_map = defaultdict(list)
    result = []
    for s in strs:
        sorted_s = tuple(sorted(s))
        anagrams_map[sorted_s].append(s)
    for value in anagrams_map.values():
        result.append(value)
    return result


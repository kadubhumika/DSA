class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        char_in_s = {}
        char_in_t = {}
        for char in s:
            char_in_s[char] = char_in_s.get(char, 0) + 1
        for char in t:
            char_in_t[char] = char_in_t.get(char, 0) + 1
        return char_in_t == char_in_s


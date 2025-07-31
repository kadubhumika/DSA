class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        charSet = set()
        left = 0
        maxLen = 0

        for i in range(n):
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[i])
            maxLen = max(maxLen, i - left + 1)

        return maxLen

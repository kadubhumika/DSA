class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_length = 0
        string_hash_map = {}

        for right, char in enumerate(s):
            if char in string_hash_map and string_hash_map[char] >= left:
                # Move left pointer just after the last duplicate
                left = string_hash_map[char] + 1

            string_hash_map[char] = right

            max_length = max(max_length, right - left + 1)

        return max_length

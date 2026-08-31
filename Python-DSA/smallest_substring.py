class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # okay i understood the question actually
        if k <= 0:
            return ""
        left = 0
        count_1 = 0
        min_len = float('inf')
        sundar_substring = ""
        for right in range(len(s)):
            if s[right] == '1':
                count_1 += 1

            while count_1 == k:
                current_len = right - left + 1
                current_substring = s[left:right + 1]
                if current_len < min_len:
                    min_len = current_len
                    sundar_substring = current_substring
                elif current_len == min_len and current_substring < sundar_substring:
                    sundar_substring = current_substring

                if s[left] == "1":
                    count_1 -= 1
                left += 1
        return sundar_substring








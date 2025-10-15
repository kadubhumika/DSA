class Solution(object):
    def maxFreqSum(self, s):
        vowels = "aeiou"
        vowels_list = []
        consonants_list = []

        # separate vowels and consonants
        for ch in s:
            if ch in vowels:
                vowels_list.append(ch)
            else:
                consonants_list.append(ch)

        # count max frequency in vowels
        max_vowels_count = 0
        for v in vowels_list:
            count_v = vowels_list.count(v)
            max_vowels_count = max(max_vowels_count, count_v)

        # count max frequency in consonants
        max_consonants_count = 0
        for c in consonants_list:
            count_c = consonants_list.count(c)
            max_consonants_count = max(max_consonants_count, count_c)

        # total
        max_sum = max_vowels_count + max_consonants_count
        return max_sum

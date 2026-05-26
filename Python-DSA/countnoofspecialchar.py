class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        count = 0
        set_word = set(word)

        for ch in set_word:

            # only process lowercase letters
            if ch.islower():

                upper_case = ch.upper()
                lower_case = ch.lower()

                if upper_case in set_word and lower_case in set_word:
                    count += 1

        return count
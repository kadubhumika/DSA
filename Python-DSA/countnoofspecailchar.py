class Solution:
    def numberOfSpecialChars(self, word: str):

        count = 0

        for i in range(26):

            lower_case = chr(ord('a') + i)

            upper_case = chr(ord('A') + i)

            lower_index = word.rfind(lower_case)

            upper_index = word.find(upper_case)

            # both must exist
            if lower_index != -1 and upper_index != -1:

                if lower_index < upper_index:
                    count += 1

        return count
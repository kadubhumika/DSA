from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []

        for word in words:
            word_weight = 0

            for char in word:
                # Fixed: Removed the accidental [2] from the end
                char_index = ord(char) - ord('a')
                word_weight += weights[char_index]

            modulo_result = word_weight % 26

            mapped_char = chr(ord('z') - modulo_result)
            result.append(mapped_char)

        return "".join(result)

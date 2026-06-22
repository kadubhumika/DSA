class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        hashmap = {}
        for char in text:

            if char in 'balloon':
                hashmap[char] = hashmap.get(char, 0) + 1

        output = 0

        b_count = hashmap.get('b', 0)
        a_count = hashmap.get('a', 0)
        l_count = hashmap.get('l', 0) // 2  # We need 2 'l's per balloon
        o_count = hashmap.get('o', 0) // 2  # We need 2 'o's per balloon
        n_count = hashmap.get('n', 0)

        output = min(b_count, a_count, l_count, o_count, n_count)

        return output

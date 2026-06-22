class Solution:
    def countAndSay(self, n: int) -> str:

        current_string = "1"

        for _ in range(n - 1):
            next_string = ""

            active_char = current_string[0]
            char_count = 0

            for char in current_string:
                if char == active_char:

                    char_count += 1
                else:

                    next_string += str(char_count) + active_char

                    active_char = char
                    char_count = 1

            next_string += str(char_count) + active_char

            current_string = next_string

        return current_string

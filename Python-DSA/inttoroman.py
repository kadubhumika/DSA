class Solution(object):
    def intToRoman(self, num):
        String = ""
        symbol_list = ['M', 1000, 'CM', 900, 'D', 500, 'CD', 400,
                       'C', 100, 'XC', 90, 'L', 50, 'XL', 40,
                       'X', 10, 'IX', 9, 'V', 5, 'IV', 4, 'I', 1]

        for i in range(0, len(symbol_list), 2):
            symbol = symbol_list[i]
            value = symbol_list[i + 1]
            count = num // value
            String += symbol * count
            num -= value * count

        return String

import math
def encryption(s):
    s = s.replace(" ", "")
    length = len(s)
    root_val = math.sqrt(length)
    row = int(math.floor(root_val))
    column = int(math.ceil(root_val))
    if row * column < length:
        row += 1
    result = ""
    for i in range(column):
        j = i
        while j < length:
            result += s[j]
            j += column
        result += " "
    return result.strip()

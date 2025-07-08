class Solution {
    fun clearDigits(s: String): String {
        var result = ""

        for (i in 0 until s.length) {
            if (s[i].isDigit()) {
             
                if (result.isNotEmpty()) {
                    result = result.dropLast(1)
                }
            } else {
                result += s[i]
            }
        }

        return result
    }
}

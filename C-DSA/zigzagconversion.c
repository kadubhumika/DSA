#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    int len = strlen(s);
    if (numRows == 1 || numRows >= len) {
        return strdup(s);
    }

    char* result = (char*)malloc(sizeof(char) * (len + 1));
    int k = 0;

    for (int row = 0; row < numRows; row++) {
        for (int j = row; j < len; j += 2 * (numRows - 1)) {
            result[k++] = s[j];

            int secondCharIndex = j + 2 * (numRows - row - 1);
            if (row != 0 && row != numRows - 1 && secondCharIndex < len) {
                result[k++] = s[secondCharIndex];
            }
        }
    }

    result[k] = '\0';
    return result;
}

#include <stdio.h>
#include <limits.h>
#include <ctype.h>
#include <string.h>

int myAtoi(char* s) {
    int i = 0, sign = 1;
    long result = 0;

    // 1. Skip leading whitespaces
    while (s[i] == ' ') {
        i++;
    }

    // 2. Check for optional '+' or '-' sign
    if (s[i] == '+' || s[i] == '-') {
        if (s[i] == '-') sign = -1;
        i++;
    }

    // 3. Convert digits to integer
    while (isdigit(s[i])) {
        int digit = s[i] - '0';
        result = result * 10 + digit;

        // 4. Handle overflow
        if (sign == 1 && result > INT_MAX) return INT_MAX;
        if (sign == -1 && -result < INT_MIN) return INT_MIN;

        i++;
    }

    return (int)(sign * result);
}

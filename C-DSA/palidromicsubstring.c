#include <stdio.h>
#include <string.h>

int countSubstrings(char* s) {
    int n = strlen(s);
    int count = 0;

    // Odd-length palindromes
    for (int center = 0; center < n; center++) {
        int left = center, right = center;
        while (left >= 0 && right < n && s[left] == s[right]) {
            count++;
            left--;
            right++;
        }
    }

    // Even-length palindromes
    for (int center = 0; center < n - 1; center++) {
        int left = center, right = center + 1;
        while (left >= 0 && right < n && s[left] == s[right]) {
            count++;
            left--;
            right++;
        }
    }

    return count;
}


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* longestPalindrome(char* s) {
    int n = strlen(s);
    int maxlen = 0;
    int startIndex = 0;

    for (int i = 0; i < n; i++) {
        for (int j = n - 1; j >= i; j--) {

            int left = i;
            int right = j;
            int isPalindrome = 1;

            while (left < right) {
                if (s[left] != s[right]) {
                    isPalindrome = 0;
                    break;
                }
                left++;
                right--;
            }

            if (isPalindrome) {
                int currentlen = j - i + 1;
                if (currentlen > maxlen) {
                    maxlen = currentlen;
                    startIndex = i;
                }
            }
        }
    }

    char* result = (char*)malloc(sizeof(char) * (maxlen + 1));
    for (int i = 0; i < maxlen; i++) {
        result[i] = s[startIndex + i];
    }
    result[maxlen] = '\0';

    return result;
}
#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int maxLen = 0;
    int n = strlen(s);

    for (int i = 0; i < n; i++) {
        int visited[256] = {0};  // Array to mark visited characters
        int currentLen = 0;

        for (int j = i; j < n; j++) {
            char currentChar = s[j];

            // If character is already seen, break
            if (visited[currentChar]) {
                break;
            }

            // Mark the character as visited and increase length
            visited[currentChar] = 1;
            currentLen++;
        }

        // Update max length if current is longer
        if (currentLen > maxLen) {
            maxLen = currentLen;
        }
    }

    return maxLen;
}

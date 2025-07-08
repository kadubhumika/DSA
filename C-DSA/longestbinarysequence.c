#include <stdio.h>
#include <string.h>

int longestSubsequence(char* s, int k) {
    int totalresult = 0;  // number of digits in the valid subsequence
    int result = 0;       // total decimal value of chosen bits
    int power = 0;        // bit position from right (2^power)
    int n = strlen(s);

    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '0') {
            totalresult++;  // always safe to take 0
        } else {
            if (power < 31) { // only check if 2^power fits in int
                int val = 1 << power;
                if (result + val <= k) {
                    result += val;
                    totalresult++;
                }
            }
        }
        power++;
    }

    return totalresult;
}

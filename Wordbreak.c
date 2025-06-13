#include <stdbool.h>
bool wordBreak(char* s, char** wordDict, int wordDictSize) {
    int n = strlen(s);
    bool dp[n + 1];
    
    // Initialize all dp values to false
    for (int i = 0; i <= n; i++) {
        dp[i] = false;
    }
    
    dp[0] = true;  // empty string can always be segmented
    
    // Check substring s[0..i-1]
    for (int i = 1; i <= n; i++) {
        // Check all substrings ending at i-1
        for (int j = 0; j < i; j++) {
            if (dp[j]) {
                // substring from j to i-1
                int len = i - j;
                char sub[len + 1];
                
                // copy substring s[j..i-1] into sub
                for (int k = 0; k < len; k++) {
                    sub[k] = s[j + k];
                }
                sub[len] = '\0';
                
                // Now check if sub is in dictionary
                for (int w = 0; w < wordDictSize; w++) {
                    if (strcmp(sub, wordDict[w]) == 0) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            if (dp[i]) {
                break;  // no need to check more if already true
            }
        }
    }
    
    return dp[n];
}
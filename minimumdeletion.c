#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);  // Ascending order
}

int minimumDeletions(char* word, int k) {
    int freq[26] = {0};
    int n = strlen(word);

    
    for (int i = 0; i < n; i++) {
        freq[word[i] - 'a']++;
    }

    
    int countFreq[26], count = 0;
    for (int i = 0; i < 26; i++) {
        if (freq[i] > 0) {
            countFreq[count++] = freq[i];
        }
    }

    qsort(countFreq, count, sizeof(int), compare);

    int minDeletions = n;

    for (int i = 0; i < count; i++) {
        int deletions = 0;
        int base = countFreq[i];  

        for (int j = 0; j < count; j++) {
            if (countFreq[j] > base + k) {
                deletions += countFreq[j] - (base + k);
            } else if (countFreq[j] < base) {
                deletions += countFreq[j];  // Remove all
            }
        }

        if (deletions < minDeletions)
            minDeletions = deletions;
    }

    return minDeletions;
}

#include <stdio.h>
#include <string.h>

int possibleStringCount(char* word) {
    int len = strlen(word);
    int totalCount = 1; 

    for (int i = 0; i < len; ) {
        int count = 1;
        int j = i + 1;

        while (j < len && word[j] == word[i]) {
            count++;
            j++;
        }

        if (count > 1) {
            totalCount += (count - 1);
        }

        i = j;  
    }

    return totalCount;
}



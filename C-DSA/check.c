#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

bool check(int* nums, int numsSize) {
    int *sorted = (int*)malloc(numsSize * sizeof(int));
    int *reversesorting = (int*)malloc(numsSize * sizeof(int));
    
    // Copy original array to sort
    for (int i = 0; i < numsSize; i++) {
        sorted[i] = nums[i];
    }

    // Sort the array
    qsort(sorted, numsSize, sizeof(int), compare);

    // Try all rotations of the sorted array
    for (int key = 0; key < numsSize; key++) {
        int match = 1;
        for (int i = 0; i < numsSize; i++) {
            int rotatedIndex = (key + i) % numsSize;
            reversesorting[i] = sorted[rotatedIndex];
            if (reversesorting[i] != nums[i]) {
                match = 0;
                break;
            }
        }
        if (match) {
            free(sorted);
            free(reversesorting);
            return true;
        }
    }

    free(sorted);
    free(reversesorting);
    return false;
}

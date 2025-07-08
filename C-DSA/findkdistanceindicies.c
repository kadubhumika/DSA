#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

int* findKDistantIndices(int* nums, int numsSize, int key, int k, int* returnSize) {
    int* result = (int*)malloc(numsSize * sizeof(int));
    bool* added = (bool*)calloc(numsSize, sizeof(bool)); // To track duplicates
    int count = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == key) {
            int start = fmax(0, i - k);
            int end = fmin(numsSize - 1, i + k);
            for (int j = start; j <= end; j++) {
                if (!added[j]) {
                    result[count++] = j;
                    added[j] = true;
                }
            }
        }
    }

    free(added); // Clean up
    *returnSize = count;
    return result;
}

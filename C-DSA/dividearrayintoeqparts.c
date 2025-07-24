#include <stdbool.h>
#include <stdlib.h>

// Comparison function for qsort
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

bool divideArray(int* nums, int numsSize) {
    // Step 1: Sort the array
    qsort(nums, numsSize, sizeof(int), compare);

    // Step 2: Check if every pair is equal
    for (int i = 0; i < numsSize; i += 2) {
        if (nums[i] != nums[i + 1]) {
            return false;  // Found a non-matching pair
        }
    }

    return true; // All pairs matched
}

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int findLHS(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);  

    int left = 0;
    int maxLength = 0;

    for (int right = 0; right < numsSize; right++) {
    
        while (nums[right] - nums[left] > 1) {
            left++;
        }

        if (nums[right] - nums[left] == 1) {
            int length = right - left + 1;
            if (length > maxLength) {
                maxLength = length;
            }
        }
    }

    return maxLength;
}

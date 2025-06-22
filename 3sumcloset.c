#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int threeSumClosest(int* nums, int numsSize, int target) {
    int sum = 0;
    int minsum = 0;
    int mindiff = INT_MAX;

    qsort(nums, numsSize, sizeof(int), compare);  // Fix: used correct sizeof

    for(int i = 0; i < numsSize - 2; i++) {
        for(int j = i + 1; j < numsSize - 1; j++) {
            for(int k = j + 1; k < numsSize; k++) {
                sum = nums[i] + nums[j] + nums[k];
                int diff = abs(target - sum);

                if(diff < mindiff) {
                    mindiff = diff;
                    minsum = sum;
                }
            }
        }
    }

    return minsum;
}

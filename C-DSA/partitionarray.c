#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int partitionArray(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int), cmp);  

    int count = 0; 
    int i = 0;

    while (i < numsSize) {
        int minInBox = nums[i];
        count++;
        i++;

       
        while (i < numsSize && nums[i] - minInBox <= k) {
            i++;
        }
    }

    return count;
}

#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    qsort(nums, numsSize, sizeof(int), cmp);

    int capacity = 100000;
    int** result = malloc(capacity * sizeof(int*));
    *returnColumnSizes = malloc(capacity * sizeof(int));
    *returnSize = 0;

    for (int i = 0; i < numsSize - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        int j = i + 1, k = numsSize - 1;

        while (j < k) {
            int sum = nums[i] + nums[j] + nums[k];
            if (sum < 0) {
                j++;
            } else if (sum > 0) {
                k--;
            } else {
                int* triplet = malloc(3 * sizeof(int));
                triplet[0] = nums[i];
                triplet[1] = nums[j];
                triplet[2] = nums[k];
                result[*returnSize] = triplet;
                (*returnColumnSizes)[*returnSize] = 3;
                (*returnSize)++;

                j++;
                k--;
                while (j < k && nums[j] == nums[j - 1]) j++;
                while (j < k && nums[k] == nums[k + 1]) k--;
            }
        }
    }

    return result;
}

#include <stdlib.h>

#define MOD 1000000007

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int numSubseq(int* nums, int numsSize, int target) {
    int count = 0;

    
    int pow2[numsSize];
    pow2[0] = 1;
    for (int i = 1; i < numsSize; i++) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    qsort(nums, numsSize, sizeof(int), compare);

    int left = 0, right = numsSize - 1;

    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            count = (count + pow2[right - left]) % MOD;
            left++;
        } else {
            right--;
        }
    }

    return count;
}

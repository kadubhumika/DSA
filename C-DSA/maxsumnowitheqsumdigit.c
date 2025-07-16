#include <stdio.h>

int digitSum(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int maximumSum(int* nums, int numsSize) {
    int maxSum = -1;
    int digitMax[82];  // Max digit sum is 9*9 = 81 (since 10^9 max value)

    // Initialize to -1
    for (int i = 0; i < 82; i++) {
        digitMax[i] = -1;
    }

    for (int i = 0; i < numsSize; i++) {
        int sum = digitSum(nums[i]);

        if (digitMax[sum] != -1) {
            int total = nums[i] + digitMax[sum];
            if (total > maxSum) {
                maxSum = total;
            }
        }

        if (nums[i] > digitMax[sum]) {
            digitMax[sum] = nums[i];
        }
    }

    return maxSum;
}

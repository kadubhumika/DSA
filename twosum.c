int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));

    // Check every possible pair
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            // If a valid pair is found
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                *returnSize = 2; // Set return size to 2
                return result;   // Return the result array
            }
        }
    }

    // If no pair found, set return size to 0
    *returnSize = 0;
    return 0;
}
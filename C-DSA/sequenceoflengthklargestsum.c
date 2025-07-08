#include <stdlib.h>
#include <stdbool.h>

// Compare function for descending sort
int compare(const void *a, const void *b) {
    return (*(int *)b - *(int *)a);
}

int* maxSubsequence(int* nums, int numsSize, int k, int* returnSize) {
    // Step 1: Copy original nums to temp array
    int *temp = (int *)malloc(sizeof(int) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        temp[i] = nums[i];
    }

    // Step 2: Sort temp to get top k elements
    qsort(temp, numsSize, sizeof(int), compare);

    // Step 3: Store top k elements in topK[]
    int *topK = (int *)malloc(sizeof(int) * k);
    for (int i = 0; i < k; i++) {
        topK[i] = temp[i];
    }

    // Step 4: Build result array from nums, matching topK values in order
    int *result = (int *)malloc(sizeof(int) * k);
    int a = 0;

    // Use visited array to avoid duplicates if needed
    bool *visited = (bool *)calloc(k, sizeof(bool));

    for (int i = 0; i < numsSize && a < k; i++) {
        for (int j = 0; j < k; j++) {
            if (!visited[j] && nums[i] == topK[j]) {
                result[a++] = nums[i];
                visited[j] = true;
                break;
            }
        }
    }

    // Cleanup
    free(temp);
    free(topK);
    free(visited);

    *returnSize = k;
    return result;
}

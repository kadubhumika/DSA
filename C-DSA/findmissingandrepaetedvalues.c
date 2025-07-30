/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMissingAndRepeatedValues(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    int Double = gridSize * gridSize;

    int* count = (int*)calloc(Double + 1, sizeof(int));  // Track occurrences
    int* output = (int*)malloc(2 * sizeof(int));         // [repeated, missing]

    // Count occurrences of each number
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            count[grid[i][j]]++;
        }
    }

    int repeated = 0;
    int missing = 0;

    // Find repeated and missing
    for (int num = 1; num <= Double; num++) {
        if (count[num] == 2) {
            repeated = num;
        } else if (count[num] == 0) {
            missing = num;
        }
    }

    output[0] = repeated;
    output[1] = missing;

    free(count);
    *returnSize = 2;
    return output;
}

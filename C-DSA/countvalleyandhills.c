int countHillValley(int* nums, int numsSize) {
    int clean[1000];
    int n = 0;

    clean[n++] = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[i - 1]) {
            clean[n++] = nums[i];
        }
    }

    int countHill = 0, countValley = 0;
    for (int i = 1; i < n - 1; i++) {
        if (clean[i] > clean[i - 1] && clean[i] > clean[i + 1]) {
            countHill++;
        } else if (clean[i] < clean[i - 1] && clean[i] < clean[i + 1]) {
            countValley++;
        }
    }

    return countHill + countValley;
}

int maximumCount(int* nums, int numsSize) {
    int negCount = 0;
    int posCount = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < 0) {
            negCount++;
        } else if (nums[i] > 0) {
            posCount++;
        } else if (nums[i] == 0) {
            continue;
        }
    }

    if (negCount > posCount) {
        return negCount;
    }
    if (posCount > negCount) {
        return posCount;
    }

    // If both are equal
    return posCount;  // or return negCount; both are same here
}

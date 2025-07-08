int missingNumber(int* nums, int numsSize) {
    int actualSum = 0;
    int arraySum = 0;
    
    for (int i = 0; i <= numsSize; i++) {
        actualSum += i; 
    }

    for (int j = 0; j < numsSize; j++) {
        arraySum += nums[j];  
    }

    return actualSum - arraySum;  // the missing number
}

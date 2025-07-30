int maximumLength(int* nums, int numsSize) {
    int evenCount = 0;
    int oddCount = 0;
    int alternateCount = 1;   // At least one element exists.

    // Count evens and odds
    for(int i = 0; i < numsSize; i++) {
        if(nums[i] % 2 == 0){
            evenCount++;
        }
        else{
            oddCount++;
        }
    }

    // Count maximum alternating subsequence length
    int partition = nums[0] % 2;
    for(int i = 1; i < numsSize; i++){
        int current = nums[i] % 2;
        if(current != partition){
            alternateCount++;
            partition = current;   // Update partition for next comparison
        }
    }

    // Find maximum of evenCount, oddCount, and alternateCount manually
    int result = evenCount;
    if(oddCount > result) result = oddCount;
    if(alternateCount > result) result = alternateCount;

    return result;
}

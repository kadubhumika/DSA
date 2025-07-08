int search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;
    int result = -1;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (nums[mid] == target) {
            result = mid;
            break;
        }

        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        else {
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return result;
}

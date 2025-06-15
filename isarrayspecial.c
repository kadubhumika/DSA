#include <stdbool.h>
#include <stdlib.h>
bool isArraySpecial(int* nums, int numsSize) {
    if (numsSize == 1) {
        return true;  // Single element is trivially "special"
    }

    for (int i = 1; i < numsSize; i++) {
        if ((nums[i] % 2) == (nums[i - 1] % 2)) {
            return false;  // Two same parity elements in a row → not special
        }
    }
    return true;  // All adjacent pairs alternate in parity
}
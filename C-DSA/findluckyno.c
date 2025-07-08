int findLucky(int* arr, int arrSize) {
    int maxLucky = -1;

    for (int i = 0; i < arrSize; i++) {
        int count = 0;

        // Count frequency of arr[i]
        for (int j = 0; j < arrSize; j++) {
            if (arr[i] == arr[j]) {
                count++;
            }
        }

        // Check if it's lucky
        if (count == arr[i]) {
            if (arr[i] > maxLucky) {
                maxLucky = arr[i];
            }
        }
    }

    return maxLucky;
}

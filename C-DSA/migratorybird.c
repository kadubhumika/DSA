int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int migratoryBirds(int arr_count, int* arr) {
    qsort(arr, arr_count, sizeof(int), compare);  // Sort the array

    int maxcount = 1;
    int count = 1;
    int result = arr[0];

    for (int i = 1; i < arr_count; i++) {
        if (arr[i] == arr[i - 1]) {
            count++;
        } else {
            count = 1; // Reset count for new bird type
        }

        // Update result if count is greater
        if (count > maxcount) {
            maxcount = count;
            result = arr[i];
        }
        // If same frequency, pick smaller type
        else if (count == maxcount && arr[i] < result) {
            result = arr[i];
        }
    }

    return result;
}
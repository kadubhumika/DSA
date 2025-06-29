int divisibleSumPairs(int n, int k, int ar_count, int* ar) {
    int count = 0;

    for (int left = 0; left < ar_count; left++) {
        for (int right = left + 1; right < ar_count; right++) {
            if ((ar[left] + ar[right]) % k == 0) {
                count++;
            }
        }
    }

    return count;
}

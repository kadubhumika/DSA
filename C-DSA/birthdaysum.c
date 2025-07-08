
int birthday(int s_count, int* s, int d, int m) {
    int count = 0;

    for (int i = 0; i <= s_count - m; i++) {  // stop when m elements can't fit
        int sum = 0;
        for (int j = 0; j < m; j++) {
            sum = sum + s[i + j];  // sum m consecutive elements
        }
        if (sum == d) {
            count++;
        }
    }

    return count;
}
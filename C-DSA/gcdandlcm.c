#include <stdio.h>

int findGCD(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int findLCM(int a, int b) {
    return (a * b) / findGCD(a, b);
}

// Find LCM of all elements in array a[]
int getLCMArray(int* a, int n) {
    int result = a[0];
    for (int i = 1; i < n; i++) {
        result = findLCM(result, a[i]);
    }
    return result;
}

// Find GCD of all elements in array b[]
int getGCDArray(int* b, int n) {
    int result = b[0];
    for (int i = 1; i < n; i++) {
        result = findGCD(result, b[i]);
    }
    return result;
}

int getTotalX(int a_count, int* a, int b_count, int* b) {
    int lcm = getLCMArray(a, a_count);
    int gcd = getGCDArray(b, b_count);
    int count = 0;

    for (int i = lcm; i <= gcd; i += lcm) {
        if (gcd % i == 0) {
            count++;
        }
    }

    return count;
}
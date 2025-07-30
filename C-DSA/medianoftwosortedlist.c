#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    // Compare function for qsort
    double diff = (*(double *)a) - (*(double *)b);
    if (diff < 0) return -1;
    else if (diff > 0) return 1;
    else return 0;
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int k = 0;
    int totalLen = nums1Size + nums2Size;
    
    double* result = (double*)malloc(sizeof(double) * totalLen);
    if (result == NULL) return 0; // handle malloc failure

    for (int i = 0; i < nums1Size; i++) {
        result[k++] = nums1[i];
    }
    for (int i = 0; i < nums2Size; i++) {
        result[k++] = nums2[i];
    }

    qsort(result, totalLen, sizeof(double), compare);

    double median;
    if (totalLen % 2 == 0) {
        median = (result[totalLen/2 - 1] + result[totalLen/2]) / 2.0;
    } else {
        median = result[totalLen/2];
    }

    free(result);
    return median;
}

#include <stdio.h>

int main() {
    int a[5] = {5, 3, 8, 1, 2};
    int i, j, temp;

    // BEFORE SORTING
    printf("Before sorting: ");
    for(i = 0; i < 5; i++) {
        printf("%d ", a[i]);
    }

    // BUBBLE SORT LOGIC
    for(i = 0; i < 5-1; i++) {
        for(j = 0; j < 5-1-i; j++) {
            if(a[j] > a[j+1]) {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }

    // AFTER SORTING
    printf("\nAfter sorting: ");
    for(i = 0; i < 5; i++) {
        printf("%d ", a[i]);
    }

    return 0;
}
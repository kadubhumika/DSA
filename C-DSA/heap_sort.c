#include <stdio.h>

int main() {
    int a[5] = {5, 3, 8, 1, 2};
    int i, j, min, temp;

    printf("Before sorting: ");
    for(i = 0; i < 5; i++)
        printf("%d ", a[i]);

    for(i = 0; i < 5-1; i++) {
        min = i;
        for(j = i+1; j < 5; j++) {
            if(a[j] < a[min])
                min = j;
        }
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
    }

    printf("\nAfter sorting: ");
    for(i = 0; i < 5; i++)
        printf("%d ", a[i]);

    return 0;
}
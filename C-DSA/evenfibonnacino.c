#include<stdbool.h>
#include<stdlib.h>
#include <stdio.h>
int main() {
    int t;
    scanf("%d", &t);

    for (int a0 = 0; a0 < t; a0++) {
        long n;
        scanf("%ld", &n);

        int i = 0;
        
        int index = 0;
        long long *fibarray = (long long *)malloc(100 * sizeof(long long));
        if (fibarray == NULL) return 0;
        long long a = 0, b = 1, fib = 0;
        long long even_sum = 0;

        while (fib<=n) {
            if(fib%2==0){
                even_sum = even_sum+fib;
            }
            fib = a + b;
            a = b;
            b = fib;
            
        }

        

        printf("%lld\n", even_sum);
        free(fibarray);  // Always free heap memory
    }

    return 0;
}

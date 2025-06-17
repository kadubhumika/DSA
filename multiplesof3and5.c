long long sum_of_multiples(int x, int n) {
    long long p = (n - 1) / x;
    return (long long)x * p * (p + 1) / 2;
}
int main() {
    int t, n;
    scanf("%d", &t);
    
    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        
        long long sum = sum_of_multiples(3, n)
              + sum_of_multiples(5, n)
              - sum_of_multiples(15, n);
printf("%lld\n", sum);
    }
    
    return 0;
}

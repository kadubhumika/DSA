void bonAppetit(int bill_count, int* bill, int k, int b) {
    int sum = 0;
    int actualsum = 0;
    int bactual, result;

    for(int i = 0; i < bill_count; i++) {
        sum = sum + bill[i];
    }

    actualsum = sum - bill[k];  
    bactual = actualsum / 2;   
    result = b - bactual;

    if (b == bactual) {
        printf("Bon Appetit\n");
    } else {
        printf("%d\n", result);
    }
}
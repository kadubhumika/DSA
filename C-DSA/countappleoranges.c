void countApplesAndOranges(int s, int t, int a, int b, int apples_count, int* apples, int oranges_count, int* oranges) {
    int count1 = 0;
    int count2 = 0;

    int *applebox = (int*)malloc(sizeof(int) * apples_count);
    int *orangebox = (int*)malloc(sizeof(int) * oranges_count);

    // Fill applebox with positions where apples fall
    for (int i = 0; i < apples_count; i++) {
        applebox[i] = a + apples[i];  // apple falls from tree a
    }

    // Fill orangebox with positions where oranges fall
    for (int i = 0; i < oranges_count; i++) {
        orangebox[i] = b + oranges[i];  // orange falls from tree b
    }

    // Count apples on the house
    for (int i = 0; i < apples_count; i++) {
        if (applebox[i] >= s && applebox[i] <= t) {
            count1++;
        }
    }

    // Count oranges on the house
    for (int i = 0; i < oranges_count; i++) {
        if (orangebox[i] >= s && orangebox[i] <= t) {
            count2++;
        }
    }

    // Print result
    printf("%d\n%d", count1, count2);

    // Free memory
    free(applebox);
    free(orangebox);
}

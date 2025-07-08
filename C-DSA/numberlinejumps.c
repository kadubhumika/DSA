char* kangaroo(int x1, int v1, int x2, int v2) {
    if (v1 == v2) {
        if (x1 == x2)
            return "YES";
        else
            return "NO";
    }

    int step1 = x1;
    int step2 = x2;

    // Keep simulating their positions for a reasonable number of steps
    for (int i = 0; i < 10000; i++) {
        step1 += v1;
        step2 += v2;

        if (step1 == step2) {
            return "YES";
        }
    }

    return "NO";
}
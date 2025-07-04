char* dayOfProgrammer(int year) {
    char* date = (char*)malloc(20); 
    if (year == 1918) {
     
        sprintf(date, "26.09.%d", year);
    } else if (
        (year < 1918 && year % 4 == 0) ||                      // Julian leap year
        (year > 1918 && (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))) // 
    ) {
        sprintf(date, "12.09.%d", year);
    } else {
        sprintf(date, "13.09.%d", year);
    }

    return date;
}
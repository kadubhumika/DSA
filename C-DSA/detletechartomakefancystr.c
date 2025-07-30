char* makeFancyString(char* s) {
    int count = 1;  
    int writeIndex = 1; 

    for(int i = 1; s[i] != '\0'; i++) {
        if(s[i] == s[i - 1]) {
            count++;
        } else {
            count = 1; 
        }

        if(count <= 2) {  
            s[writeIndex] = s[i];
            writeIndex++;
        }
    }

    s[writeIndex] = '\0';  

    return s;
}

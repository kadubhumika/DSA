char** divideString(char* s, int k, char fill, int* returnSize) {
   int n = strlen(s);
int a = 0;
  *returnSize = (n + k - 1) / k;

 char** Box = (char**)malloc((*returnSize) * sizeof(char*));

for(int i=0; i<n; i+=k){
    
char *triplet = (char *)malloc((k + 1) * sizeof(char));
    for(int j=0; j<k; j++){
        if(i+j<n){
            triplet[j]= s[j+i];
        }
        else {
            triplet[j] = fill;
        }

    }
    triplet[k]='\0';
    Box[a++]=triplet;

}
return Box;




    
}
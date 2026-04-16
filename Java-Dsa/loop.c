#include<stdio.h>
int sum(int n);
int main() {
	
	
	printf("sum is = %d\n",sum(5));
	
	return 0;
}
int sum(int n){
	if(n==1){
		return 1;
	}
	int summ1=sum(n-1);
	int sumN=summ1+n;
	return sumN;
}
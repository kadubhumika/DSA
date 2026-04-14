#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100
char stack[MAX];
int top = -1;
void push(char c) {
    stack[++top] = c;
}
char pop() {
    return stack[top--];
}
char peek() {
    return stack[top];
}
int precedence(char op) {
    if(op == '+' || op == '-') return 1;
    if(op == '*' || op == '/') return 2;
    return 0;
}
void reverse(char exp[]) {
    int i, j;
    char temp;
    for(i = 0, j = strlen(exp)-1; i < j; i++, j--) {
        temp = exp[i];
        exp[i] = exp[j];
        exp[j] = temp;
    }
}
void infixToPrefix(char infix[]) {
    char prefix[MAX];
    int i, k = 0;
    reverse(infix);
    for(i = 0; i < strlen(infix); i++) {

        if(isalnum(infix[i])) {
            prefix[k++] = infix[i];
        }
        else {
            while(top != -1 && precedence(peek()) >= precedence(infix[i])) {
                prefix[k++] = pop();
            }
            push(infix[i]);
        }
    }

    while(top != -1) {
        prefix[k++] = pop();
    }
    prefix[k] = '\0';
    reverse(prefix);
    printf("Prefix Expression: %s\n", prefix);
}
int main() {
    char infix[] = "a+b-c*d";
    infixToPrefix(infix);
    return 0;
}
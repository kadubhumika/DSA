// Implementation of single linked list using array
#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* head = NULL;
void create(int value) {
    struct Node* newnode = (struct Node*)malloc(sizeof(struct Node));
    newnode->data = value;
    newnode->next = NULL;
    if(head == NULL) {
        head = newnode;
    }
    else {
        struct Node* temp = head;
        while(temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newnode;
    }
}
void insert(int value, int pos) {
    struct Node* newnode = (struct Node*)malloc(sizeof(struct Node));
    newnode->data = value;
    struct Node* temp = head;
    for(int i = 1; i < pos-1; i++) {
        temp = temp->next;
    }
    newnode->next = temp->next;
    temp->next = newnode;
}
void deleteNode(int pos) {
    struct Node* temp = head;
    for(int i = 1; i < pos-1; i++) {
        temp = temp->next;
    }
    struct Node* del = temp->next;
    temp->next = del->next;
    free(del);
}
void display() {
    struct Node* temp = head;
    while(temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
int main() {
    create(10);
    create(20);
    create(30);
    printf("Original List:\n");
    display();
    insert(25,3);
    printf("After Insert:\n");
    display();
    deleteNode(2);
    printf("After Delete:\n");
    display();
    return 0;
}
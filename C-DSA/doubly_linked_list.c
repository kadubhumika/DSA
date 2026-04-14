// Program to craete doubley linked list and return searched key
#include <stdio.h>
#include <stdlib.h>
typedef struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
} Node;
Node *head = NULL;
Node *tail = NULL;
Node* createNode(int data) {
    Node *newNode = (Node*) malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;

    return newNode;
}
void insert(int data) {
    Node *newNode = createNode(data);
    if (head == NULL) {
        head = tail = newNode;
    } else {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
}
Node* search(int key) {
    Node *temp = head;
    while (temp != NULL) {
        if (temp->data == key) {
            return temp;
        }
        temp = temp->next;
    }
    return NULL;
}
void display() {
    Node *temp = head;
    while (temp != NULL) {
        printf("Address: %p | Data: %d\n", temp, temp->data);
        temp = temp->next;
    }
}
int main() {
    insert(10);
    insert(20);
    insert(30);
    display();
    int key = 20;
    Node *result = search(key);
    if (result != NULL) {
        printf("Key %d found at address: %p\n", key, result);
    } else {
        printf("Key not found\n");
    }

    return 0;
}
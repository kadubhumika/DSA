#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}
void preorder(struct Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}
struct Node* queue[100];
int front = 0, rear = 0;
void enqueue(struct Node* node) {
    queue[rear++] = node;
}
struct Node* dequeue() {
    return queue[front++];
}
int isEmpty() {
    return front == rear;
}
void BFS(struct Node* root) {
    if (root == NULL) return;
    enqueue(root);
    while (!isEmpty()) {
        struct Node* curr = dequeue();
        printf("%d ", curr->data);
        if (curr->left)
            enqueue(curr->left);
        if (curr->right)
            enqueue(curr->right);
    }
}
int main() {
    struct Node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    printf("Before (Preorder): ");
    preorder(root);
    printf("\nAfter (BFS): ");
    BFS(root);
    return 0;
}
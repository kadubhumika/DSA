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
int check(struct Node* root) {
    if (root == NULL)
        return 0;
    int left = check(root->left);
    if (left == -1) return -1;
    int right = check(root->right);
    if (right == -1) return -1;
    if (abs(left - right) > 1)
        return -1;
    return 1 + (left > right ? left : right);
}
int isAVL(struct Node* root) {
    return check(root) != -1;
}
int main() {
    struct Node* root1 = newNode(10);
    root1->left = newNode(5);
    root1->right = newNode(15);
    printf("Balanced Tree: %d\n", isAVL(root1));  // Output: 1
    struct Node* root2 = newNode(10);
    root2->left = newNode(5);
    root2->left->left = newNode(2);
    printf("Unbalanced Tree: %d\n", isAVL(root2)); // Output: 0
    return 0;
}
#include <stdio.h>
#define N 5
int queue[N];
int front = -1, rear = -1;
void enqueue(int x) {
    if ((rear + 1) % N == front) {
        printf("Queue is Full\n");
        return;
    }
    if (front == -1) {
        front = rear = 0;
    } else {
        rear = (rear + 1) % N;
    }
    queue[rear] = x;
}
void dequeue() {
    if (front == -1) {
        printf("Queue is Empty\n");
        return;
    }
    printf("Deleted: %d\n", queue[front]);
    if (front == rear) {
        front = rear = -1;
    } else {
        front = (front + 1) % N;
    }
}
void display() {
    if (front == -1) {
        printf("Queue is Empty\n");
        return;
    }
    int i = front;
    while (1) {
        printf("%d ", queue[i]);
        if (i == rear) break;
        i = (i + 1) % N;
    }
    printf("\n");
}
int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    display();
    dequeue();
    display();
    enqueue(50);
    enqueue(60); // shows circular effect
    display();
    return 0;
}
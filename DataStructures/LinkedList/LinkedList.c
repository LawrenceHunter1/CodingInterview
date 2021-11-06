#include "LinkedList.h"
#include <stdlib.h>
#include <stdio.h>

Node* push(Node* head, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = head;
    return newNode;
}

Node* constructList(int keys[], int n) {
    Node* head = NULL;
    for (int i = n - 1; i >= 0; i--) {
        head = push(head, keys[i]);
    }
    return head;
}

int get(Node* head, int index) {
    Node* ptr = head;
    int counter = 0;
    while (ptr) {
        if (index == counter) {
            return ptr->data;
        }
        counter++;
        ptr = ptr->next;
    }
    printf("Index out of bounds error.\n");
    exit(0);
}

Node* pop(Node* head) {
    int data = head->data;
    head->next = NULL;
    return data;
}

void printList(struct Node* head) {
    Node* ptr = head;
    while (ptr)
    {
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}

#include <stdio.h>
#include <stdlib.h>
#include "List.h"

void initalise(List *l) {
    l->list = (int*)malloc(1 * sizeof(int));
    l->used = 0;
    l->size = 1;
}

void append(List *l, int element) {
    if (l->used == l->size) {
        l->size *= 2;
        l->list = (int*)realloc(l->list, l->size * sizeof(int));
    }
    l->list[l->used++] = element;
}

void freeList(List *l) {
    free(l->list);
    l->list = NULL;
    l->used = l->size = 0;
}

int resize(List *l) {
    l->size *= 2;
    void *temp = realloc(l->list, l->size * sizeof(int));
    if (!temp) {
        return 1;
    }
    l->list = (int*)temp;
    return 0;
}

int getLength(List *l) {
    return l->size;
}

void print(List *l) {
    printf("[");
    for (int i = 0; i < l->used - 1; i++) {
        printf("%d, ", l->list[i]);
    }
    printf("%d]\n", l->list[l->used-1]);
}
#include <stdio.h>
#include <stdlib.h>
#include "Tree.h"

int insert(Tree** tree, int data) {
    Tree *temp = NULL;
    if (!(*tree)) {
        temp = (Tree*)malloc(sizeof(Tree));
        temp->left = temp->right = NULL;
        temp->data = data;
        *tree = temp;
        return 1;
    }

    if (data < (*tree)->data) {
        insert(&(*tree) -> left, data);
    }
    else if (data > (*tree)->data) {
        insert(&(*tree) -> right, data);
    }
    return NULL;
}

void deltree(Tree* tree) {
    if (tree)
    {
        deltree(tree->left);
        deltree(tree->right);
        free(tree);
    }
}

Tree* search(Tree** tree, int data) {
    if(!(*tree)) {
        return NULL;
    }
    if(data < (*tree)->data) {
        search(&((*tree)->left), data);
    }
    else if(data > (*tree)->data) {
        search(&((*tree)->right), data);
    }
    else if(data == (*tree)->data) {
        return *tree;
    }
    return NULL;
}
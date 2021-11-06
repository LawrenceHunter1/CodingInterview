#include "HashTable.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

unsigned long hashFunction(HashTable* table, char* str) {
    unsigned long result = 0;
    for (int i = 0; str[i]; i++) {
        result += str[i];
    }
    return result % table->size;
}

HT_Item* createItem(char* key, char* value) {
    HT_Item* item = (HT_Item*)malloc(sizeof(HT_Item));
    item->key = (char*)malloc(strlen(key) + 1);
    item->value = (char*)malloc(strlen(value) + 1);

    strcpy(item->key, key);
    strcpy(item->value, value);

    return item;
}

HashTable* createTable(unsigned size) {
    HashTable* table = (HashTable*) malloc(sizeof(HashTable));
    table->size = size;
    table->count = 0;
    table->items = (HT_Item**)malloc(table->size * sizeof(HT_Item*));

    for (int i = 0; i < table->size; i++) {
        table->items[i] = NULL;
    }

    return table;
} 

void freeItem(HT_Item* item) {
    free(item->key);
    free(item->value);
    free(item);
}

void freeTable(HashTable* table) {
    for (int i=0; i < table->size; i++) {
        HT_Item* item = table->items[i];
        if (item != NULL) {
            freeItem(item);
        }
    }
    free(table->items);
    free(table);
}


int insert(HashTable* table, char* key, char* value) {
    HT_Item* item = createItem(key, value);
    unsigned long index = hashFunction(table, key);
    HT_Item* current_item = table->items[index];
     
    if (current_item == NULL) {
        if (table->count == table->size) {
            return 0;
        }
        table->items[index] = item; 
        table->count++;
    }
 
    else {
        if (strcmp(current_item->key, key) == 0) {
            strcpy(table->items[index]->value, value);
            return 1;
        }
        
        else {
            // ***HANDLE COLLISION***
            return 0;
        }
    }
}

char* search(HashTable* table, char* key) {
    int index = hashFunction(table, key);
    HT_Item* item = table->items[index];
 
    if (item != NULL) {
        if (strcmp(item->key, key) == 0)
            return item->value;
    }
    return NULL;
}
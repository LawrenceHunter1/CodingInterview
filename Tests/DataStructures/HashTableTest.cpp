#include <gtest/gtest.h>
#include "../../DataStructures/HashTable/HashTable.h"

unsigned long hashFunction(char* str);
HT_Item* createItem(char* key, char* value);
HashTable* createTable(unsigned size);
void freeItem(HT_Item* item);
void freeTable(HashTable* table);
int insert(HashTable* table, char* key, char* value);
char* search(HashTable* table, char* key);


TEST(IntegerInputsSuite, initSize) {
    HashTable* ht = createTable(5000);
    EXPECT_EQ(ht->size, 5000) << "HashTable size incorrect";
}

TEST(IntegerInputsSuite, initCount) {
    HashTable* ht = createTable(5000);
    EXPECT_EQ(ht->count, 0) << "HashTable count incorrect";
}

TEST(IntegerInputsSuite, countIncrease) {
    HashTable* ht = createTable(5000);
    char *key = "1";
    char *value = "First";
    insert(ht, key, value);
    EXPECT_EQ(ht->count, 1) << "HashTable items count didn't increase";
}

TEST(IntegerInputsSuite, correctStore) {
    HashTable* ht = createTable(5000);
    char *key = "1";
    char *value = "First";
    insert(ht, key, value);
    char *expected = "First";
    int compare = strcmp(search(ht, key), expected);
    EXPECT_EQ(compare, 0) << "HashTable value stored incorrect";
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
#include <gtest/gtest.h>
#include "../../DataStructures/List/List.h"

void initalise(List *l);
void append(List *l, int element);
int resize(List *l);
int getLength(List *l);
void printList(List *l);

TEST(IntegerInputsSuite, initSize) {
    List l;
    initalise(&l);
    EXPECT_EQ(getLength(&l), 1) << "List length incorrect";
}

TEST(IntegerInputsSuite, firstGrowSize) {
    List l;
    initalise(&l);
    append(&l, 1);
    append(&l, 1);
    EXPECT_EQ(getLength(&l), 2) << "List length incorrect";
}

TEST(IntegerInputsSuite, secondGrowSize) {
    List l;
    initalise(&l);
    append(&l, 1);
    append(&l, 1);
    append(&l, 1);
    EXPECT_EQ(getLength(&l), 4) << "List length incorrect";
}

TEST(IntegerInputsSuite, insertCorrect) {
    List l;
    initalise(&l);
    append(&l, 1);
    append(&l, 1);
    int expected[2] = {1, 1};
    EXPECT_TRUE( 0 == std::memcmp( l.list, expected, sizeof(expected) ) ) << "List items incorrect";
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
#include <stdlib.h>
#include <gtest/gtest.h>
#include "../../DataStructures/Tree/Tree.h"

int insert(Tree** tree, int data);
void deltree(Tree* tree);
Tree* search(Tree** tree, int data);

TEST(IntegerInputsSuite, rootUpdates) {
    Tree* t;
    t = NULL;
    insert(&t, 10);
    EXPECT_EQ(t->data, 10) << "Tree root incorrect";
}

TEST(IntegerInputsSuite, leftUpdates) {
    Tree* t;
    t = NULL;
    insert(&t, 10);
    insert(&t, 5);
    EXPECT_EQ(t->left->data, 5) << "Tree left incorrect";
}

TEST(IntegerInputsSuite, rightUpdates) {
    Tree* t;
    t = NULL;
    insert(&t, 10);
    insert(&t, 15);
    EXPECT_EQ(t->right->data, 15) << "Tree right incorrect";
}

TEST(IntegerInputsSuite, leftSubTreeProducedOne) {
    Tree* t;
    t = NULL;
    insert(&t, 10);
    insert(&t, 5);
    insert(&t, 3);
    EXPECT_EQ(t->left->left->data, 3) << "Tree right incorrect";
}

TEST(IntegerInputsSuite, leftSubTreeProducedTwo) {
    Tree* t;
    t = NULL;
    insert(&t, 10);
    insert(&t, 5);
    insert(&t, 7);
    EXPECT_EQ(t->left->right->data, 7) << "Tree right incorrect";
}


TEST(IntegerInputsSuite, rightSubTreeProducedOne) {
    Tree* t;
    t = NULL;
    insert(&t, 10);
    insert(&t, 15);
    insert(&t, 30);
    EXPECT_EQ(t->right->right->data, 30) << "Tree right incorrect";
}

TEST(IntegerInputsSuite, rightSubTreeProducedTwo) {
    Tree* t;
    t = NULL;
    insert(&t, 10);
    insert(&t, 15);
    insert(&t, 12);
    EXPECT_EQ(t->right->left->data, 12) << "Tree right incorrect";
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
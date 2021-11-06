#include <gtest/gtest.h>
#include "../../DataStructures/LinkedList/LinkedList.h"

Node* constructList(int keys[], int n);
Node* push(Node* head, int data);
int get(Node* head, int index);
void printList(struct Node* head);

TEST(IntegerInputsSuite, checkData) {
    int keys[] = {1, 2, 3, 4};
    int n = sizeof(keys)/sizeof(keys[0]);

    struct Node* head = constructList(keys, n);

    EXPECT_EQ(get(head, 2), 3) << "List length incorrect";
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
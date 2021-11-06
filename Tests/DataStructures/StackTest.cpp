#include <gtest/gtest.h>
#include "../../DataStructures/Stack/Stack.h"

Stack* createStack(unsigned capacity);
int isFull(Stack* stack);
int isEmpty(Stack* stack);
int push(Stack* stack, int item);
int pop(Stack* stack);
int peek(Stack* stack);

TEST(IntegerInputsSuite, initCapacity) {
    Stack *s = createStack(10);
    EXPECT_EQ(s->capacity, 10) << "Init stack capacity incorrect";
}

TEST(IntegerInputsSuite, initTop) {
    Stack *s = createStack(10);
    EXPECT_EQ(s->top, -1) << "Init stack top incorrect";
}

TEST(IntegerInputsSuite, initEmpty) {
    Stack *s = createStack(10);
    EXPECT_EQ(isEmpty(s), 1) << "Init stack not empty";
}

TEST(IntegerInputsSuite, initNotFull) {
    Stack *s = createStack(10);
    EXPECT_EQ(isFull(s), 0) << "Init stack is full";
}

TEST(IntegerInputsSuite, popCorrectVal) {
    Stack *s = createStack(10);
    push(s, 10);
    EXPECT_EQ(pop(s), 10) << "Pop fail";
}

TEST(IntegerInputsSuite, peekCorrectVal) {
    Stack *s = createStack(10);
    push(s, 10);
    EXPECT_EQ(peek(s), 10) << "Peek fail";
}

TEST(IntegerInputsSuite, popTopChanges) {
    Stack *s = createStack(10);
    push(s, 10);
    int top = s->top;
    pop(s);
    EXPECT_EQ(s->top, top-1) << "Pop top fail";
}

TEST(IntegerInputsSuite, peekTopNoChange) {
    Stack *s = createStack(10);
    push(s, 10);
    int top = s->top;
    peek(s);
    EXPECT_EQ(s->top, top) << "Peek top fail";
}

TEST(IntegerInputsSuite, isFullCorrect) {
    Stack *s = createStack(2);
    push(s, 10);
    push(s, 10);
    EXPECT_EQ(isFull(s), 1) << "Full fail";
}

TEST(IntegerInputsSuite, insertCorrect) {
    Stack *s = createStack(2);
    push(s, 10);
    push(s, 10);
    int expected[2] = {10, 10};
    EXPECT_TRUE( 0 == std::memcmp( s->array, expected, sizeof(expected) ) ) << "Stack items incorrect";
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
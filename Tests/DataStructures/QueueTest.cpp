#include <gtest/gtest.h>
#include "../../DataStructures/Queue/Queue.h"

Queue* createQueue(unsigned capacity);
int isFull(Queue* queue);
int isEmpty(Queue* queue);
int enqueue(Queue* queue, int item);
int dequeue(Queue* queue);
int front(Queue* queue);
int rear(Queue* queue);

TEST(IntegerInputsSuite, initCapacity) {
    Queue *q = createQueue(10);
    EXPECT_EQ(q->capacity, 10) << "Init queue capacity incorrect";
}

TEST(IntegerInputsSuite, initRear) {
    Queue *q = createQueue(10);
    EXPECT_EQ(q->rear, 9) << "Init queue rear incorrect";
}

TEST(IntegerInputsSuite, initFront) {
    Queue *q = createQueue(10);
    EXPECT_EQ(q->front, 0) << "Init queue front incorrect";
}

TEST(IntegerInputsSuite, initEmpty) {
    Queue *q = createQueue(10);
    EXPECT_EQ(isEmpty(q), 1) << "Init queue not empty";
}

TEST(IntegerInputsSuite, initNotFull) {
    Queue *q = createQueue(10);
    EXPECT_EQ(isFull(q), 0) << "Init queue is full";
}

TEST(IntegerInputsSuite, enqueCorrectFront) {
    Queue *q = createQueue(10);
    enqueue(q, 10);
    EXPECT_EQ(q->front, 0) << "Enque front fail";
}

TEST(IntegerInputsSuite, enqueCorrectRear) {
    Queue *q = createQueue(10);
    enqueue(q, 10);
    EXPECT_EQ(q->rear, 0) << "Enque rear fail";
}

TEST(IntegerInputsSuite, enqueCorrectSize) {
    Queue *q = createQueue(10);
    enqueue(q, 10);
    EXPECT_EQ(q->size, 1) << "Enque size fail";
}

TEST(IntegerInputsSuite, dequeCorrectValue) {
    Queue *q = createQueue(10);
    enqueue(q, 10);
    EXPECT_EQ(dequeue(q), 10) << "Dequeue value fail";
}

TEST(IntegerInputsSuite, dequeCorrectFront) {
    Queue *q = createQueue(10);
    enqueue(q, 10);
    dequeue(q);
    EXPECT_EQ(q->front, 1) << "Enque front fail";
}

TEST(IntegerInputsSuite, dequeCorrectRear) {
    Queue *q = createQueue(10);
    enqueue(q, 10);
    dequeue(q);
    EXPECT_EQ(q->rear, 0) << "Enque rear fail";
}

TEST(IntegerInputsSuite, dequeCorrectSize) {
    Queue *q = createQueue(10);
    enqueue(q, 10);
    dequeue(q);
    EXPECT_EQ(q->size, 0) << "Enque size fail";
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
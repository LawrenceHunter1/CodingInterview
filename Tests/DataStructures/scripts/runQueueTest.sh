clear
if [ $? -eq 0 ]; then
    g++ -std=c++0x ../QueueTest.cpp  ../../../DataStructures/Queue/Queue.c -lgtest -lgtest_main -pthread -o ../out/queueTest
    if [ $? -eq 0 ]; then
        ../out/queueTest
    fi
fi
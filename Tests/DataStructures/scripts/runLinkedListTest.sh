clear
if [ $? -eq 0 ]; then
    g++ -std=c++0x ../LinkedListTest.cpp  ../../../DataStructures/LinkedList/LinkedList.c -lgtest -lgtest_main -pthread -o ../out/linkedListTest
    if [ $? -eq 0 ]; then
        ../out/linkedListTest
    fi
fi
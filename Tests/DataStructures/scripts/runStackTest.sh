clear
if [ $? -eq 0 ]; then
    g++ -std=c++0x ../StackTest.cpp  ../../../DataStructures/Stack/Stack.c -lgtest -lgtest_main -pthread -o ../out/stackTest
    if [ $? -eq 0 ]; then
        ../out/stackTest
    fi
fi
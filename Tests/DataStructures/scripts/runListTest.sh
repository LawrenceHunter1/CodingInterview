clear
if [ $? -eq 0 ]; then
    g++ -std=c++0x ../ListTest.cpp  ../../../DataStructures/List/List.c -lgtest -lgtest_main -pthread -o ../out/listTest
    if [ $? -eq 0 ]; then
        ../out/listTest
    fi
fi
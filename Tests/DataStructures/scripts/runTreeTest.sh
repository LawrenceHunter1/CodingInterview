clear
if [ $? -eq 0 ]; then
    g++ -std=c++0x ../TreeTest.cpp  ../../../DataStructures/Tree/Tree.c -lgtest -lgtest_main -pthread -o ../out/treeTest
    if [ $? -eq 0 ]; then
        ../out/treeTest
    fi
fi
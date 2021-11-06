clear
if [ $? -eq 0 ]; then
    g++ -std=c++0x ../HashTableTest.cpp  ../../../DataStructures/HashTable/HashTable.c -lgtest -lgtest_main -pthread -o ../out/hashTable
    if [ $? -eq 0 ]; then
        ../out/hashTable
    fi
fi
typedef struct HT_Item {
    char* key;
    char* value;
} HT_Item;

typedef struct HashTable
{
    HT_Item** items;
    unsigned size;
    int count;
} HashTable;

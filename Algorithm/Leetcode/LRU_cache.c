//https://leetcode.com/problems/lru-cache/
// ���� �� ��� ���ʿ� �߰�

// =========================
// Result
// Accepted 396 ms 109.5 MB
// =========================

// hash table
// 10**4 �ؽ� �ʿ� ����
#include <stdio.h>
#include <malloc.h>

struct _cache {
    int key;
    int value;
    int enable;
    //struct _cache* c_prev;
    //struct _cache* c_next;
    struct _cache* prev;
    struct _cache* next;
}cache_node[100010]; //cache_node[500000], 

//int node;

typedef struct {
    int capacity;
    int cur;
    struct _cache head;
    struct _cache tail;
} LRUCache;

// linked list�� �޾Ƴ���
// capa ������ �� ���ʿ��� ����
// prev next

LRUCache* lRUCacheCreate(int capacity) {
	int i;
    for (i = 0; i<100010; i++) cache_node[i].enable = 0;
 //   node = 0;

    //LRUCache* myLRUCache = new LRUCache;
    LRUCache* myLRUCache = malloc(sizeof(LRUCache));
    myLRUCache->capacity = capacity;
    myLRUCache->cur = 0;

    myLRUCache->head.next = &myLRUCache->tail;
    myLRUCache->tail.prev = &myLRUCache->head;
    
    //printf("### head %x (%x) tail %x (%x)\n", &myLRUCache->head,
	//myLRUCache->tail.prev, &myLRUCache->tail, myLRUCache->head.next);

    // head�� tail�� ���� ���ֺ���
    return myLRUCache;
}

void lRUCacheDelete(LRUCache* obj, int key) {
    cache_node[key].enable = 0;
    cache_node[key].next->prev = cache_node[key].prev;
    cache_node[key].prev->next = cache_node[key].next;
}

// �Ǽ�: ���� �߰��Ǵ� �͸� �Ű� ����
// ���� �� �ڸ��� �ִ� head, tail �� ���⼺�� �Ű� �� �� 
void lRUCacheAdd(LRUCache* obj, int key, int value) {
    cache_node[key].enable = 1;
    cache_node[key].key = key;
    cache_node[key].value = value;
    cache_node[key].prev = &(obj->head);
    cache_node[key].next = obj->head.next;
    obj->head.next->prev = &cache_node[key];
    obj->head.next = &cache_node[key];
}

// 
int lRUCacheGet(LRUCache* obj, int key) {
  // hash table ���� ã�ƿ���
    //for (struct _cache*p = hash[key].next; p; p = p->next) {
    if (cache_node[key].enable){
        // �����ϰ� ������Ʈ
        lRUCacheDelete(obj, key);
        lRUCacheAdd(obj, key, cache_node[key].value);
        return cache_node[key].value;
    }
    else
        return -1;
}

void lRUCachePut(LRUCache* obj, int key, int value) {
  // capacity�� ������ tail ����Ű�� �� ���� (hash table ������ ����? �ƴϸ� disable ǥ��?)
    // head �� �߰�
    // �̹� ������ ������Ʈ

    // �̹� ������ ������Ʈ
    // �����ϰ� �ٽ� �� �տ� �߰� 

    if (cache_node[key].enable) {
        cache_node[key].value = value;
        lRUCacheDelete(obj, key);
        lRUCacheAdd(obj, key, value);
        return;
    }
    //printf("### not enable %d [cur %d] key %d\n", key, obj->cur, key);
/*	if (key == 3)
	    printf("head (%x) %d %x -> %d %x tail (%x)\n", &obj->head,
	obj->head.next->key, obj->head.next->next,
	obj->head.next->next->key, obj->head.next->next->next,
	&obj->tail);
*/
    // ���� �Ѿ�� tail ����Ű�� �� ���� // ���� ���� �ʿ� (key�� key �� ������!!!)
    if (obj->cur == obj->capacity) {
    	//printf("### delete key %d\n", obj->tail.prev->key);
        lRUCacheDelete(obj, obj->tail.prev->key);
        obj->cur--;
    }
    //printf("### delete\n");
    // ������ ���� �߰�
    lRUCacheAdd(obj, key, value);
    obj->cur++;
    //myLRUCache->cur++;

    return;
}

void lRUCacheFree(LRUCache* obj) {
    free(obj); //delete obj;
}

int main()
{
    LRUCache* lRUCache = lRUCacheCreate(2);
    lRUCachePut(lRUCache, 1, 1); // cache is {1=1}
    lRUCachePut(lRUCache, 2, 2); // cache is {1=1, 2=2}
    //printf("###1\n");
    printf("%d\n", lRUCacheGet(lRUCache, 1));    // return 1
    //printf("###2\n");
    lRUCachePut(lRUCache, 3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    //printf("###3\n");
    printf("%d\n", lRUCacheGet(lRUCache, 2));    // returns -1 (not found)
    //printf("###4\n");
    lRUCachePut(lRUCache, 4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    //printf("###5\n");
    printf("%d\n", lRUCacheGet(lRUCache, 1));    // return -1 (not found)
    //printf("###6\n");
    printf("%d\n", lRUCacheGet(lRUCache, 3));    // return 3
    printf("%d\n", lRUCacheGet(lRUCache, 4));    // return 4

    return 0;
}

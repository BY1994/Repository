#include <malloc.h>
#define NULL 0

// 고려해야할 사항: 새로운 걸 추가할 때 Head랑 Tail 이 같이 업데이트 되어야함 
// 주제가 Single Linked List 이므로 prev, next 로 하는 게 아니면 Tail 을 찾아가라는 듯 

typedef struct _MyList{
    int val;
    struct _MyList *next; 
} MyList;

typedef struct {
    MyList * Head;
    //MyList * Tail;
    int buf_ind;
    MyList buf[2021];
} MyLinkedList;

/** Initialize your data structure here. */

MyLinkedList* myLinkedListCreate() {
    MyLinkedList * LinkedList = (MyLinkedList *)malloc(sizeof(MyLinkedList));
    
    LinkedList->Head = &(LinkedList->buf[0]);
    //LinkedList->Tail = &(LinkedList->buf[0]);
    LinkedList->Head->next = NULL;
    //LinkedList->Tail->next = NULL;
    LinkedList->buf_ind = 1;
    return LinkedList;
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
int myLinkedListGet(MyLinkedList* obj, int index) {
    int current = 0;
    for (MyList *p = obj->Head->next; p; p=p->next) {
        if (current == index) return p->val;
        current++;
    }
    return -1;
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
	// Head랑 Tail 이랑 같으면 Head 추가할 때 Tail 에도 추가해야함 
    obj->buf[obj->buf_ind].val = val;
    obj->buf[obj->buf_ind].next = obj->Head->next;
    obj->Head->next = &(obj->buf[obj->buf_ind]);
    obj->buf_ind++;
}

/** Append a node of value val to the last element of the linked list. */
void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
	MyList *p = obj->Head;
    for (; p->next; p=p->next);

    obj->buf[obj->buf_ind].val = val;
    obj->buf[obj->buf_ind].next = p->next;
    p->next = &(obj->buf[obj->buf_ind]);
    obj->buf_ind++;
    
	// Head랑 Tail 이랑 같으면 Tail 추가할 때 Head에도 추가해야함 
    //obj->buf[obj->buf_ind].val = val;
    //obj->buf[obj->buf_ind].next = obj->Tail;
    //obj->Tail = &(obj->buf[obj->buf_ind]);
    //obj->buf_ind++;
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    int current = 0;
    MyList *prev = obj->Head;
    for (MyList *p = obj->Head->next; p; p=p->next) {
        if (current == index) {
            obj->buf[obj->buf_ind].val = val;
            obj->buf[obj->buf_ind].next = prev->next;
            prev->next = &(obj->buf[obj->buf_ind]);
            obj->buf_ind++;
            return;
        }
        prev = p;
        current++;
    }
}

/** Delete the index-th node in the linked list, if the index is valid. */
void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    int current = 0;
    MyList *prev = obj->Head;
    for (MyList *p = obj->Head->next; p; p=p->next) {
        if (current == index) {
            prev->next = p->next;
            return;
        }
        prev = p;
        current++;
    }
}

void myLinkedListFree(MyLinkedList* obj) {
    free(obj);
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 
 * myLinkedListAddAtHead(obj, val);
 
 * myLinkedListAddAtTail(obj, val);
 
 * myLinkedListAddAtIndex(obj, index, val);
 
 * myLinkedListDeleteAtIndex(obj, index);
 
 * myLinkedListFree(obj);
*/

#include <stdio.h>

int main(void)
{
	MyLinkedList* obj = myLinkedListCreate();
	
	myLinkedListAddAtHead(obj, 1);
	myLinkedListAddAtTail(obj, 3);
	myLinkedListAddAtIndex(obj, 1, 2);

	printf("%d\n", myLinkedListGet(obj, 1));
	myLinkedListDeleteAtIndex(obj, 1);
	printf("%d\n", myLinkedListGet(obj, 1));
	return 0;
}

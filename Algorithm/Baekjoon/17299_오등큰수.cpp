/*
17299 ����ū�� 

stack

NGF ���� �߸� �����ؼ� �� �� Ʋ�� 

2022.07.31 ��� 
*/

// stack �� ���� �ƴ϶� i �� ���� �Ѵ�. 
// NGF �� ���� �ƴ϶� i �� ���� �Ѵ�. 
#include <stdio.h>
#define MAX (1000010)
int N;
int A[MAX];
int count[MAX]; // = F()
int NGF[MAX];
int stack[MAX];
int sp;

int main(void)
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &A[i]);
		count[A[i]]++;
		NGF[i] = -1; 
	}

	for (int i = 0; i < N; ++i) {
		while (sp > 0 && count[A[stack[sp-1]]] < count[A[i]]) {
			NGF[stack[sp-1]] = A[i];
			sp--;
		}
		stack[sp++] = i;
	}
	
	for (int i = 0; i < N; ++i)
		printf("%d ", NGF[i]);
	printf("\n");

	return 0;
}

// Ʋ�Ƚ��ϴ� 
/*
������ Ʋ���� ���ͼ� �Ʒ��� ���� �ۼ��ؾ��Ѵٰ� �����ߴ�. 
NGF �� N ������ �ƴ϶� ������ ���� ������ �� �����ؾ��ϴ� ��
������ print �� ���� NGF �ȿ��� �ε����� �ƴ϶� �� ��ü�� �����ϴ� ��  
*/
#if 0
#include <stdio.h>
#define MAX (1000010)
int N;
int A[MAX];
int count[MAX]; // = F()
int NGF[MAX];
int stack[MAX];
int sp;

int main(void)
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &A[i]);
		count[A[i]]++;
	}

	for (int i = 0; i < MAX; ++i)
		NGF[i] = -1;
	
	for (int i = 0; i < N; ++i) {
		while (sp > 0 && count[stack[sp-1]] < count[A[i]]) {
			NGF[stack[sp-1]] = A[i];
			sp--;
		}
		stack[sp++] = A[i];
	}
	
	for (int i = 0; i < N; ++i)
		printf("%d ", NGF[A[i]]);
	printf("\n");
	
	return 0;
}
#endif

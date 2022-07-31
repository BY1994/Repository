/*
17299 오등큰수 

stack

NGF 설명 잘못 이해해서 한 번 틀림 

2022.07.31 통과 
*/

// stack 에 값이 아니라 i 가 들어가야 한다. 
// NGF 도 수가 아니라 i 가 들어가야 한다. 
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

// 틀렸습니다 
/*
예제가 틀리게 나와서 아래와 같이 작성해야한다고 생각했다. 
NGF 는 N 까지가 아니라 나오는 수의 범위를 다 포함해야하는 것
정답을 print 할 때도 NGF 안에는 인덱스가 아니라 수 자체가 들어가야하는 것  
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

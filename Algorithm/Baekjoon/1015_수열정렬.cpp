/*
1015 수열 정렬 

정렬
count sort 
(혹은 개수가 적기 때문에 완전 탐색도 가능할 것) 
*/

#include <stdio.h>

int A[51];
int count[1001];
int psum[1002];

int main(void)
{
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &A[i]);
		count[A[i]]++;
	}
	for (int i = 0; i <= 1000; i++) {
		psum[i+1] = psum[i] + count[i];
	}
	for (int i = 0; i < N; i++) {
		printf("%d ", psum[A[i]]++);
	}
	printf("\n");
	return 0;
}

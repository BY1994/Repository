/*
14697 방 배정하기

brute force

단순히 배정 가능 / 불가만 판단하면 됨
A, B, C 가 무조건 인풋으로 들어오고
적당히 300 x 300 x 300 이 1초 안에 탐색 가능해서 for 문으로 작성 
*/
#include <stdio.h>

int A, B, C, N;
int flag;

int main(void)
{
	scanf("%d %d %d %d", &A, &B, &C, &N);
	for (int i = 0; i <= N; i += A){
		for (int j = 0; j <= (N-i); j += B) {
			for (int k = 0; k <= (N-i-j); k += C) {
				if (i + j + k == N) {
					flag = 1;
					break;
				}
			}
			if (flag) break;
		}
		if (flag) break;
	}
	
	printf("%d\n", flag);
	return 0;
}

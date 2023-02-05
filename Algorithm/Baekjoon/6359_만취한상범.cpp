/*
6359 만취한 상범 

시뮬레이션
*/

#include <stdio.h>

int rooms[101]; // 0 = 닫힘 1 = 열림 
int count[101];
int main(void) {
	int T, n;
	scanf("%d", &T);
	for (int i = 1; i <= 100; ++i) {
		for (int j = i; j <= 100; j += i) {
			rooms[j] ^= 1;
		}
	}
	for (int i = 1; i <= 100; ++i) {
		count[i+1] += count[i] + rooms[i];
	}
	while (T--) {
		scanf("%d", &n);
		printf("%d\n", count[n+1]);
	}
	
	return 0;
} 

/*
3035 스캐너
 
문자열 확대시키기 
ZR 씩 확대시켰으므로, ZR 로 나누면 원래 인덱스 접근 가능
2 개씩 건너뛰는 거라면 2로 나눴을 때 이렇게 됨 
0 1 2 3
0 0 1 1 
*/
#include <stdio.h>

char scanner[52][52];

int main(void) {
	int R, C, ZR, ZC;
	scanf("%d %d %d %d", &R, &C, &ZR, &ZC);
	for (int i = 0; i < R; ++i) {
		scanf("%s", scanner[i]);
	}
	for (int i = 0; i < R*ZR; ++i) {
		for (int j = 0; j < C*ZC; ++j) {
			printf("%c", scanner[i/ZR][j/ZC]);
		}
		printf("\n");
	}
	return 0;
}

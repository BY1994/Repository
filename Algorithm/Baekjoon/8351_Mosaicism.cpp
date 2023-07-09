/*
8351 Mosaicism

비트마스킹 
인덱스가 너무 커져서 배열을 필요한 만큼 잡는다면 메모리 초과가 발생하게 됨 
풀이 방식 다시 고민해야함 

2023-06-04 런타임 에러 (Out of bounds) 
*/

// 틀린 코드 => total 및 count 에 나타나는 최대 인덱스는 300 이 아니라 
// 300 * 300 인 90000 이다.
#if 0 
#include <stdio.h>

int n, max;
int an[310];
int ai[310][310];
int tbl[100010];
int total[310];
int count[310][310];

int main(void) {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &an[i]);
		for (int j = 0; j < an[i]; ++j) {
			scanf("%d", &ai[i][j]);
			tbl[ai[i][j]] = 1;
			if (max < ai[i][j]) max = ai[i][j];
		}
	}
	for (int i = 0; i <= max; ++i) {
		tbl[i+1] += tbl[i];
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < an[i]; ++j) {
			total[tbl[ai[i][j]]]++;
			for (int k = j+1; k < an[i]; ++k) {
				count[tbl[ai[i][j]]][tbl[ai[i][k]]]++;
				count[tbl[ai[i][k]]][tbl[ai[i][j]]]++;
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		int ans = 0;
		for (int j = 0; j < an[i]; ++j) {
			for (int k = j+1; k < an[i]; ++k) {
				ans += (total[tbl[ai[i][j]]] - count[tbl[ai[i][j]]][tbl[ai[i][k]]]) *\
				(total[tbl[ai[i][k]]] - count[tbl[ai[i][j]]][tbl[ai[i][k]]]);
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
#endif

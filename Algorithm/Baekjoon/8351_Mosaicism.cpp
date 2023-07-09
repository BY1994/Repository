/*
8351 Mosaicism

��Ʈ����ŷ 
�ε����� �ʹ� Ŀ���� �迭�� �ʿ��� ��ŭ ��´ٸ� �޸� �ʰ��� �߻��ϰ� �� 
Ǯ�� ��� �ٽ� ����ؾ��� 

2023-06-04 ��Ÿ�� ���� (Out of bounds) 
*/

// Ʋ�� �ڵ� => total �� count �� ��Ÿ���� �ִ� �ε����� 300 �� �ƴ϶� 
// 300 * 300 �� 90000 �̴�.
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

/*
1392 �뷡 �Ǻ� 

�Ʒ� �� ���� �� �� Ǯ�� ����� ������ �� 
1. ������ + ���̳ʸ� ��ġ 
2. ��� ���̺�
*/

#include <stdio.h>

int time_table[10100];
int score[101];

int main(void) {
	int N, Q, time, cur = 0;
	scanf("%d %d", &N, &Q);
	for (int i = 1; i <= N; ++i) {
		scanf("%d", &score[i]);
		for (int j = 0; j < score[i]; ++j)
			time_table[cur++] = i;
	}
	for (int i = 0; i < Q; ++i) {
		scanf("%d", &time);
		printf("%d\n", time_table[time]);
	}
	return 0;
}

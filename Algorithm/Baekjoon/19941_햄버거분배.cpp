/*
19941 �ܹ��� �й�

greedy ����
���ʿ��� ���� �ִ��� �� �ܹ��Ÿ� �ϳ� ����, 
������ ��Ȳ�� ������� �ʾƵ� �װ� �׻� �������� ����Ǵ� �� �ϴ�. 
������ �� ���Ƽ� �ڵ带 ¥�� ����� ������ 
��Ȯ�� ������ ��� �ϴ��� �𸣰ڴ� 

�ڵ带 ¥�ٰ� �Ǽ��� �� �ϳ� �־��µ�,
�ܹ��Ÿ� �ϳ� ã���� �ٷ� break �� �ؾ��ϴµ� �װ� ���� �ʾƼ�
�� ����� ���� �ܹ��Ÿ� �Ե��� ���۽��׾���. 

�����Խ��ǿ� ���� �� �� �־��µ� �ݷʸ� ã�� ���ߴ�.
�Ʒ��� �亯�� ����̴�. 
��Ÿ�� ���� �ذ�
https://www.acmicpc.net/board/view/85375 
Try Catch ����
https://www.acmicpc.net/board/view/71099 
Python �� ���� ���ǹ����� ó�� �� ���� (��Ÿ�� ������ �� ���� �� ã���� ��) 
https://www.acmicpc.net/board/view/66505 
*/

#include <stdio.h>
int N, K, ans;
char table[20010];

int main(void) {
	scanf("%d %d", &N, &K);
	scanf("%s", table);
	for (int i = 0; i < N; i++) {
		if (table[i] == 'P') {
			for (int j = -K; j <= K; j++) {
				int next_i = i + j; 
				if (next_i < 0 || next_i >= N) continue;
				if (table[next_i] == 'H') {
					table[next_i] = 0;
					ans++;
					break;
				}
			}
		} 
	}
	printf("%d\n", ans);
	return 0;
}


/*
1384 �޽���

���� 

Ʋ�� ��
Group 1 ��� �� ��
N ����ϴµ� +5 �� �ϵ��ڵ��ع���;; 

�ݷ� 
https://www.acmicpc.net/board/view/94983
3
ANN N N
BOB N N
CLIVE P P
0
*/

#include <stdio.h>
char name[21][61];
char msg[21][21];

int main(void)
{
	int N, flag, tc = 0;
	while (1) {
		scanf("%d", &N);
		if (N == 0) break;
		getchar();
		printf("Group %d\n", ++tc); 
		for (int i = 0; i < N; ++i) {
			scanf("%s", name[i]);
			for (int j = 0; j < N-1; ++j) {
				scanf(" %c", &msg[i][j]);
			}
			getchar();
		}
		flag = 1;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N-1; ++j) {
				if (msg[i][j] == 'P') continue;
				printf("%s was nasty about %s\n", name[(i+N-(j+1))%N], name[i]);
				flag = 0;
			}
		}
		if (flag) printf("Nobody was nasty\n");
		printf("\n");
	}
	return 0;
}

/*
1474 �� �� 

greedy
�ִ� 1�� �ۿ� ���̰� ���� �����Ƿ�
�ҹ��� �տ� �ִ� ��, ���� ������ �� ������ ������ �ִ� ��
���� �ص� �ȴ�. (greedy) 
*/

#include <stdio.h>
#include <string.h>
char words[10][11];

int main(void)
{
	int N, M, div, rem, total = 0;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		scanf("%s", words[i]);
		total += strlen(words[i]);
	}
	total = M - total;
	div = total / (N-1);
	rem = total - (div*(N-1));
	printf("%s", words[0]);
	for (int i = 1; i < N; ++i) {
		for (int j = 0; j < div; ++j) printf("_");
		if (rem >= (N-i) || (rem > 0 && words[i][0] >= 'a')) {
			printf("_");
			rem--;
		}
		printf("%s", words[i]);
	}
	printf("\n");
	return 0;
}

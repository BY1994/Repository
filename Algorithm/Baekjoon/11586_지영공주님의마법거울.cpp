/*
11586 ���� ���ִ��� ���� �ſ� 

���� 
*/

#include <stdio.h>
char mirror[101][101];

int main(void) {
	int N, mood;
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%s", &mirror[i]);
	}
	scanf("%d", &mood);
	if (mood == 1) { // �ִ� �״�� 
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				printf("%c", mirror[i][j]);
			}
			printf("\n");
		}
	} else if (mood == 2) { // ��/��� ������ ��� 
		for (int i = 0; i < N; ++i) {
			for (int j = N-1; j >= 0; --j) {
				printf("%c", mirror[i][j]);
			}
			printf("\n");
		}
	} else {
		for (int i = N-1; i >= 0; --i) {
			for (int j = 0; j < N; ++j) {
				printf("%c", mirror[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}

/*
3023 마술사 이민혁

구현, 문자열 
*/

#include <stdio.h>
char design[101][101];
int main(void) {
	int R, C, A, B;
	scanf("%d %d", &R, &C);
	for (int i = 0; i < R; ++i) {
		scanf("%s", design[i]);
	}
	scanf("%d %d", &A, &B);
	
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			design[i][2*C-1-j] = design[i][j];
		}
	}
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < 2*C; ++j) {
			design[2*R-1-i][j] = design[i][j];
		}
	}
	if (design[A-1][B-1] == '.') design[A-1][B-1] = '#';
	else design[A-1][B-1] = '.';

	for (int i = 0; i < 2*R; ++i) {
		for (int j = 0; j < 2*C; ++j) {
			printf("%c", design[i][j]);
		}
		printf("\n");
	}
	return 0;
}


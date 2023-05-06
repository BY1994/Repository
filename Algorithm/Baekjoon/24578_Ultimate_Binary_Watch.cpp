/*
24578 Ultimate Binary Watch

비트를 . 과 * 로 표현해서 출력하기 
*/

#include <stdio.h>
char clock[4][4];
int time[4];
int main(void) {
	scanf("%1d%1d%1d%1d",&time[0],&time[1],&time[2],&time[3]);
	for (int i = 0; i < 4; ++i) {
		for (int j = 3; j >= 0; --j) {
			if (time[i] & 1) clock[i][j] = '*';
			else clock[i][j] = '.';
			time[i] >>= 1;
		}
	}
	printf("%c %c   %c %c\n", clock[0][0],clock[1][0],clock[2][0],clock[3][0]);
	printf("%c %c   %c %c\n", clock[0][1],clock[1][1],clock[2][1],clock[3][1]);
	printf("%c %c   %c %c\n", clock[0][2],clock[1][2],clock[2][2],clock[3][2]);
	printf("%c %c   %c %c\n", clock[0][3],clock[1][3],clock[2][3],clock[3][3]);
}

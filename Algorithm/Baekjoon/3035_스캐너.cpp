/*
3035 ��ĳ��
 
���ڿ� Ȯ���Ű�� 
ZR �� Ȯ��������Ƿ�, ZR �� ������ ���� �ε��� ���� ����
2 ���� �ǳʶٴ� �Ŷ�� 2�� ������ �� �̷��� �� 
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

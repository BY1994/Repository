/*
3034 �ޱ׸� â��

������ ����
���� ���� �밢�� ���̺��� ������ �Ǵ�

sqrt ����
https://blockdmask.tistory.com/307
*/
#include <stdio.h>
#include <math.h>

int N, W, H, D, match;

int check(int match) {
	if (match <= W) return 1;
	if (match <= H) return 1;
	if (match <= D) return 1;
	return 0;
}

int main(void)
{
	scanf("%d %d %d", &N, &W, &H);
	D = sqrt(W*W + H*H);
	while (N--) {
		scanf("%d", &match);
		if (check(match)) printf("DA\n");
		else printf("NE\n");
	}
	return 0;
}

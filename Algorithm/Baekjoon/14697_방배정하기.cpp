/*
14697 �� �����ϱ�

brute force

�ܼ��� ���� ���� / �Ұ��� �Ǵ��ϸ� ��
A, B, C �� ������ ��ǲ���� ������
������ 300 x 300 x 300 �� 1�� �ȿ� Ž�� �����ؼ� for ������ �ۼ� 
*/
#include <stdio.h>

int A, B, C, N;
int flag;

int main(void)
{
	scanf("%d %d %d %d", &A, &B, &C, &N);
	for (int i = 0; i <= N; i += A){
		for (int j = 0; j <= (N-i); j += B) {
			for (int k = 0; k <= (N-i-j); k += C) {
				if (i + j + k == N) {
					flag = 1;
					break;
				}
			}
			if (flag) break;
		}
		if (flag) break;
	}
	
	printf("%d\n", flag);
	return 0;
}

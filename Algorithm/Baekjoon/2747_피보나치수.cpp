/*
2747 �Ǻ���ġ ��

DP
������ n >= 2 ��� �Ǿ�������,
�����δ� 0, 1 �� ���´�. 
�Է¿��� 45���� �۰ų� ���� �ڿ������ ������ �־
0, 1 �� �������� �����ϴ� �� �ϴ�. 
*/

#include <stdio.h>

int fibo[46];

int main(void)
{
	int n;
	scanf("%d", &n);
	fibo[1] = 1;
	for (int i = 2; i <= n; i++) {
		fibo[i] = fibo[i-1] + fibo[i-2];
	}
	printf("%d\n", fibo[n]);
	return 0;	
} 

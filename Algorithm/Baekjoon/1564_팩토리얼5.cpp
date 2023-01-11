/*
1564 ���丮��5 

���� 

�ݷ�
https://www.acmicpc.net/board/view/94908
390625
���� 50016

Ʋ�ȴ� ����: N! �� ���� �� 0 �� ��û ���� ���� �� �ִµ�,
�װ� ��� ���ϰ� ������ % �� N �� �ִ� ũ�� + 1 ���θ� ��Ҵ�.
N �� �ִ�ũ�� * 2 �� ��ƾ��Ѵ�. 
*/
#include <stdio.h>

int main(void) {
	unsigned long long N;
	unsigned long long ans = 1;
	scanf("%llu", &N);
	for (unsigned long long i = 1; i <= N; ++i) {
		ans *= i;
		while (ans % 10ULL == 0) ans /= 10ULL;
		ans %= 1000000000000ULL;
	}
	printf("%05llu\n", ans % 100000ULL);
	return 0;
}

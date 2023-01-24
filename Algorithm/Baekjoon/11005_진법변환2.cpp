/*
11005 ���� ��ȯ 2

���� ���� ��ȯ
10 ���� to N ���� 

N �������� ��ȯ���� �� ���� �� ���̰� �������� �־����� ����
0.5 ���� �� ���� �׷��� ���� �ʰ� ������ �� ����.
�־��� ����ؼ� 10 �� 2�� 4���� �Ǿ���ϴϱ� 4��� �����Ͽ���.
=> ������ �� ��;; 10������ ���� 
=> �����ߴ��� �޸� �ʰ� ���� 1������ ���� => Ʋ�Ƚ��ϴ� 
=> int2str[0] = 0 �̶�� �����ߴ�. '0' �̾���ϴµ� 
35 35 �̷� �ݷ� �Է��غ��� Ʋ�� �� �� �� �ִ�! 
*/

#include <stdio.h>

char int2str[129];
char ans[1000000000LL];
void init(void)
{
	for (int i = 0; i <= 9; ++i) int2str[i] = '0' + i;
	for (int i = 10; i <= 35; ++i) int2str[i] = 'A' + i - 10;
}

int main(void)
{
	int N, B;
	long long ind = 0LL;

	init();
	scanf("%d %d", &N, &B);
	while (N) {
		ans[ind] = int2str[N % B];
		ind += 1LL;
		N /= B;
	}
	for (long long i = 0LL; i < ind; i += 1LL) {
		printf("%c", ans[ind - 1LL - i]);
	}
	printf("\n");
	return 0;
} 

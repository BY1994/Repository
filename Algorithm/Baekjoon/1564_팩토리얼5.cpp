/*
1564 팩토리얼5 

수학 

반례
https://www.acmicpc.net/board/view/94908
390625
정답 50016

틀렸던 이유: N! 을 곱할 때 0 이 엄청 많이 붙을 수 있는데,
그걸 고려 못하고 나누는 % 를 N 의 최대 크기 + 1 으로만 잡았다.
N 의 최대크기 * 2 로 잡아야한다. 
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

/*
2747 피보나치 수

DP
문제에 n >= 2 라고 되어있지만,
실제로는 0, 1 도 나온다. 
입력에는 45보다 작거나 같은 자연수라는 조건이 있어서
0, 1 도 포함으로 봐야하는 듯 하다. 
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

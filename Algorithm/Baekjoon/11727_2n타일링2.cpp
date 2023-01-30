/*
11727 2xn ≈∏¿œ∏µ 2 

DP
*/

#include <stdio.h>

int dp[1100];

int main(void) {
	int n;
	scanf("%d", &n);
	dp[0] = dp[1] = 1;
	for (int i = 2; i <= n; i++) {
		dp[i] += dp[i - 1];
		dp[i] += dp[i - 2] * 2;
		dp[i] %= 10007;
	}
	printf("%d\n", dp[n]);
	return 0;
}

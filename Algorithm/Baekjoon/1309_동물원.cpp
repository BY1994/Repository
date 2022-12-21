/*
1309 동물원 

DP
*/
#include <stdio.h>

int N;
int dp[100001][3];

int main(void)
{
	scanf("%d", &N);
	// 왼쪽, 오른쪽, 아무데도 두지 않는 경우 
	dp[0][0] = dp[0][1] = dp[0][2] = 1;
	for (int i = 1; i < N; ++i) {
		dp[i][0] += (dp[i-1][1] + dp[i-1][2]) % 9901;
		dp[i][1] += (dp[i-1][0] + dp[i-1][2]) % 9901;
		dp[i][2] += (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901;
	}
	printf("%d\n", (dp[N-1][0]+dp[N-1][1]+dp[N-1][2]) % 9901);
	return 0;
}

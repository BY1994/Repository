/*
2961

brute force
알고리즘 분류에 비트마스킹이 있길래
visited 배열 따로 안 두고 비트마스킹으로 풀어보았다. 
 
*/
#include <stdio.h>
#include <stdlib.h> 
#define INF (1000000010LL)

int N;
int taste[11][2];
long long ans = INF;

void dfs(int visited, long long S, long long B){
	if (ans > abs(S-B)) {
		ans = abs(S-B);
	}
	for (int i = 0; i < N; ++i) {
		if (visited >> i) continue;
		dfs(visited | (1<<i), S*taste[i][0], B+taste[i][1]);
	}
}

int main(void)
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d %d", &taste[i][0], &taste[i][1]);
	}
	for (int i = 0; i < N; ++i) {
		dfs(1 << i, taste[i][0], taste[i][1]);
	}
	printf("%lld\n", ans);
	return 0;
}

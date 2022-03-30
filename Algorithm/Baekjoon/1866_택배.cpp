/*
택배

헬리콥터는 여러 개 사용할 수 있고,
헬리콥터가 사용되면 좋을 구간을 찾는 문제
특정 구간의 중앙값에 헬리콥터가 들어가야하고,
그 구간 외 나머지는 트럭이 유리

for 문 돌면서 현재 위치의 제일 최소 cost 를 구하는데,
이전 위치들을 잡아서 구간으로 잡으면서,
헬리콥터가 그 중앙에 갔을 때 최소 cost 나오는 때를 구함
그 이전까지는 이전에 구해둔 트럭이든 헬리콥터든 최소값으로 유지하고 dp[j]
j 부터 i 까지의 구간에 대해 다시 최소값을 구하는 것
=> 이중 for 문 부분 이유

중앙값을 생각해보면
30 40 50 일 때
40 지점에 헬리콥터가 와야 최적의 위치
10 0 10 이렇게 비용이 소요됨
그러면 비용 계산은 미리 누적합을 구해두면 거리의 절대값의 합을 빠르게 계산할 수 있음
0 30 70 120
중앙값에서 위쪽 절반은 120 - 30 = 90 인데, 여기서 중앙값 40*2(40,50 2개 합해서) 를 빼주면,
90 - 80 = 10 이 나옴
중앙값에서 아래 절반은 30 - 0 = 30 인데, 중앙값에서 이 값을 빼면
40 * 1 - 30 = 10 이 나옴
=> prefix sum 을 사용하는 이유

// 10 억 이하 자연수가 출력이라는 조건 있어서
// long long 필요 없음

// 중앙값을 잘 이해하면 이런 로직도 가능
https://www.acmicpc.net/source/4574205
*/
#include <stdio.h>

int arr[3010];
int temp[3010];
long long dp[3010];
long long prefix[3010];

// merge sort
void sort(int s, int e)
{
	// 1. base condition
	if (s >= e) return;
	// 2. divide & conquer
	int m = (s + e) / 2, i = s, j = m + 1, k = s;
	sort(s, m);
	sort(m + 1, e);
	// 3. merge
	while (i <= m && j <= e) {
		if (arr[i] < arr[j]) temp[k++] = arr[i++];
		else temp[k++] = arr[j++];
	}
	while (i <= m) temp[k++] = arr[i++];
	while (j <= e) temp[k++] = arr[j++];
	// 4. copy
	for (i = s; i <= e; i++) arr[i] = temp[i];
}

long long min(long long a, long long b) {
	return a < b ? a : b;
}

int main(void)
{
	int N, tcost, hcost;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) scanf("%d", &arr[i]);
	scanf("%d %d", &tcost, &hcost);

	// sort
	sort(0, N-1);
	//for (int i = 0; i < N; i++) printf("%d", arr[i]);
	//printf("\n");

	// prefix
	for (int i = 0; i < N; i++) prefix[i + 1] += prefix[i] + arr[i]*tcost;
	//for (int i = 0; i <= N; i++) printf("%lld", prefix[i]);
	//printf("\n");

	// dp
	for (int i = 0; i < N; i++) {
		dp[i + 1] += dp[i] + arr[i]*tcost;
		//printf("## truck %lld\n", dp[i + 1]);
		for (int j = i; j >= 0; j--) {
			int mid = (i + j) / 2;
			long long rcost = (prefix[i+1]-prefix[mid]) - (arr[mid]*tcost*(i-mid+1));
			long long lcost = (arr[mid] * tcost*(mid-j)) - (prefix[mid] - prefix[j]);
			//printf("### i %d j %d rcost %lld lcost %lld\n", i, j, rcost, lcost);
			dp[i + 1] = min(dp[i + 1], dp[j]+ rcost + lcost + hcost);
		}
		//printf("# dp %lld\n", dp[i + 1]);
	}
	printf("%lld\n", dp[N]);
	return 0;
}
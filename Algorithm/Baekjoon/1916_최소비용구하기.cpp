/*
1916 
다익스트라 연습

최대 버스 수 * 비용 10^10 버스 비용이 가능하기 때문에 결과값이 int 안에 안 담김
https://www.acmicpc.net/board/view/64011

특정 도시에서 다른 도시로 가는 버스 편 여러 개 가능
https://www.acmicpc.net/board/view/68108

반례
https://www.acmicpc.net/board/view/9761
*/
#include <stdio.h>

long long arr[1001][1001];
struct data {
	int node;
	long long cost;
}heap[1000100];

int hn = 1;

void push(int node, long long cost)
{
	// 부모와 비교
	int i;
	for (i = hn; i > 1; i /= 2) {
		if (cost >= heap[i / 2].cost) break;
		heap[i] = heap[i / 2];
	}
	heap[i] = { node, cost };
	hn++;
}

struct data pop(void)
{
	struct data ret = heap[1];
	struct data cur = heap[hn-1];

	int i;
	for (i = 1; i * 2 + 1 < hn; ) {
		int c = i * 2;
		if (c + 1 < hn && heap[c].cost > heap[c + 1].cost) c += 1;
		if (heap[c].cost > cur.cost) break;
		heap[i] = heap[c];
		i = c;
	}
	heap[i] = heap[--hn];
	return ret;
}

int main(void)
{
	long long ans[1001];
	int N, M;

	scanf("%d", &N);
	scanf("%d", &M);

	int s, e;
	long long cost;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			arr[i][j] = -1;

	for (int i = 0; i < M; i++) {
		scanf("%d %d %lld", &s, &e, &cost);
		if (arr[s-1][e-1] < 0 || arr[s-1][e-1] > cost) // 질문답변 게시판 보면 많이 틀린 부분
			arr[s - 1][e - 1] = cost;
	}

	int S, E;
	scanf("%d %d", &S, &E);

	// ans 초기화
	for (int i = 0; i < N; i++) ans[i] = 10000000000ULL; // 1 << 62 이런 식으로 하면 int 처럼 들어가는 듯

	// 시작점 heap 에 push
	ans[S-1] = 0;
	push(S-1, 0); // num, cost

	// 다익스트라 돌면서
	while (hn > 1) {
		struct data x = pop();
		for (int i = 0; i < N; i++) {
			if (i == x.node) continue;
			if (arr[x.node][i] < 0) continue;
			long long next_cost = x.cost + arr[x.node][i];
			if (ans[i] > next_cost) {
				ans[i] = next_cost;
				push(i, next_cost);
			}
		}
	}

	printf("%ld\n", ans[E - 1]);
	return 0;
}
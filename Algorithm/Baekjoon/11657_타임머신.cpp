/*
11657 타임머신
 
벨만포드
https://velog.io/@kimdukbae/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Bellman-Ford-Algorithm
 
SPFA
https://gina65.tistory.com/26
https://levenshtein.tistory.com/119
https://hongjun7.tistory.com/134

벨만포드와 SPFA 의 최악의 시간 복잡도
https://www.acmicpc.net/board/view/21965 

틀렸습니다 기록
1. long long 으로 변경해도 틀렸습니다
https://www.acmicpc.net/board/view/84267#comment-137025
https://www.acmicpc.net/board/view/91430
(6천만을 N 번 반복) 
2. check 를 target 이 아닌 i 로 하는 것 잘못된 부분 찾아서 수정
3. 똑같은 A, B 를 가진 간선이 여러 개 들어오지 않는다고 생각한 코드라서 틀림 
https://www.acmicpc.net/board/view/39180
반례
3 3
1 2 3
2 1 -1000
2 1 5
답 -1 
*/

// 잘못된 로직 수정 후 AC 받은 코드 
#include <stdio.h>
// INF = 1 << 60
#define INF (0x1000000000000000LL)

int N, M;
struct _edge{
	int city;
	long long cost;
}edge[501][501];
int eid[501];

int visit[501];
int check[501];
long long dist[501];
int Q[3000000];
int fr, re;

int SPFA(void)
{
	for (int i = 1; i <= N; i++) {
		dist[i] = INF;
	}
	
	dist[1] = 0;
	Q[re++] = 1;
	check[1] = 1;
	visit[1]++;
	
	while (fr < re) {
		int current = Q[fr++];
		check[current] = 0;
		
		for (int i = 1; i <= eid[current]; i++) {
			int target = edge[current][i].city;
			int cost = edge[current][i].cost;
			if (dist[target] > dist[current] + cost) {
				dist[target] = dist[current] + cost;
				if (check[target]) continue;
				Q[re++] = target;
				check[target] = 1;
				if (++visit[target] > N) return 1;
			}
		}
	}
	return 0;
}

int main(void)
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; i++) {
		int A, B;
		long long C;
		scanf("%d %d %lld", &A, &B, &C);
		eid[A]++;
		edge[A][eid[A]] = {B, C};
	}
	
	if (SPFA()) {
		printf("-1\n");
	} else {
		for (int i = 2; i <= N; i++) {
			if (dist[i] == INF) printf("-1\n");
			else printf("%lld\n", dist[i]);
		}
	}
	
	return 0;
}

// 틀린 점 발견 
#if 0 
#include <stdio.h>
// INF = 1 << 60
#define INF (0x1000000000000000LL)

int N, M;
int edge[501][501];
long long cost[501][501];
int eid[501];

int visit[501];
int check[501];
long long dist[501];
int Q[3000000];
int fr, re;

int SPFA(void)
{
	for (int i = 1; i <= N; i++) {
		dist[i] = INF;
	}
	
	dist[1] = 0;
	Q[re++] = 1;
	check[1] = 1;
	visit[1]++;
	
	while (fr < re) {
		int current = Q[fr++];
		check[current] = 0;
		
		for (int i = 1; i <= eid[current]; i++) {
			int target = edge[current][i];
			if (dist[target] > dist[current] + cost[current][target]) {
				dist[target] = dist[current] + cost[current][target];
				if (check[target]) continue;
				Q[re++] = target;
				check[target] = 1;
				if (++visit[target] > N) return 1;
			}
		}
	}
	return 0;
}

int main(void)
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; i++) {
		int A, B;
		long long C;
		scanf("%d %d %lld", &A, &B, &C);
		eid[A]++;
		edge[A][eid[A]] = B;
		cost[A][B] = C;
	}
	
	if (SPFA()) {
		printf("-1\n");
	} else {
		for (int i = 2; i <= N; i++) {
			if (dist[i] == INF) printf("-1\n");
			else printf("%lld\n", dist[i]);
		}
	}
	
	return 0;
}
#endif

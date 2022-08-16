/*
10282 해킹

다익스트라 

input 받을 때 a와 b 의존성 반대로 받음
초기화할 때 i 를 1부터 n 까지로 해야하는데, 0부터 n-1 함 

struct 를 vector 안에 사용하는 방법 찾아봤는데
그럴 필요 없었다.
https://rim0621.tistory.com/68

pair<int, int> 로 충분했다.
https://ongveloper.tistory.com/182

질문 답변 반례 찾기
https://www.acmicpc.net/board/view/67702
입력 
1
3 3 2
2 1 5
3 2 5
2 3 3
정답 2 5 
https://www.acmicpc.net/board/view/71219
https://www.acmicpc.net/board/view/95684
*/

#include <stdio.h>
#include <queue>
using namespace std;

#define INF (100000000)

struct computer{
	int id;
	int cost;
	computer(int _id, int _cost): id(_id), cost(_cost) {}
};
vector<vector<computer > > computers;

int dist[10001]; 

void dijkstra(int start, int n, vector<pair<int, int > > computers[]) {
	for (int i = 1; i <= n; i++) {
		dist[i] = INF;
	}
	dist[start] = 0;
	
	priority_queue<pair<int, int> > PQ;
	PQ.push({0, start});
	
	while (!PQ.empty()) {
		int cost = -PQ.top().first;
		int cur = PQ.top().second;
		PQ.pop();
		for (int i = 0; i < computers[cur].size(); i++) { //com_id[cur]; i++) {
			int next = computers[cur][i].first;
			int next_cost = computers[cur][i].second + cost;
			if (dist[next] > next_cost) {
				dist[next] = next_cost;
				PQ.push({-next_cost, next});
			}
		}
	}
}

int main(void)
{
	int tc;
	scanf("%d", &tc);
	while (tc--) {
		vector<pair<int, int > > computers[10001];
		int total = 0;
		int time = 0;
		int n, d, c;
		scanf("%d %d %d", &n, &d, &c);
		for (int i = 1; i <= n; i++) com_id[i] = 0;
		for (int i = 0; i <d; i++) {
			int a, b, s;
			scanf("%d %d %d", &a, &b, &s);
			computers[b].push_back({a, s});
		}
		dijkstra(c, n, computers);
		for (int i = 1; i <= n; i++) {
			if (dist[i] == INF) continue;
			if (time < dist[i]) time = dist[i];
			total++;
		}
		printf("%d %d\n", total, time);
	}
	return 0;
}

// 메모리 초과
#if 0 
#include <stdio.h>
#include <queue>
using namespace std;

#define INF (100000000)

struct com{
	int id;
	int cost;
}computers[10001][10001];

int com_id[10001];

int dist[10001]; 

void dijkstra(int start, int n) {
	for (int i = 1; i <= n; i++) {
		dist[i] = INF;
	}
	dist[start] = 0;
	
	priority_queue<pair<int, int> > PQ;
	PQ.push({0, start});
	
	while (!PQ.empty()) {
		int cost = -PQ.top().first;
		int cur = PQ.top().second;
		PQ.pop();
		for (int i = 0; i < com_id[cur]; i++) {
			int next = computers[cur][i].id;
			int next_cost = computers[cur][i].cost + cost;
			if (dist[next] > next_cost) {
				dist[next] = next_cost;
				PQ.push({-next_cost, next});
			}
		}
	}
}

int main(void)
{
	int tc;
	scanf("%d", &tc);
	while (tc--) {
		int total = 0;
		int time = 0;
		int n, d, c;
		scanf("%d %d %d", &n, &d, &c);
		for (int i = 1; i <= n; i++) com_id[i] = 0;
		for (int i = 0; i <d; i++) {
			int a, b, s;
			scanf("%d %d %d", &a, &b, &s);
			computers[b][com_id[b]++] = {a, s};
		}
		dijkstra(c, n);
		for (int i = 1; i <= n; i++) {
			if (dist[i] == INF) continue;
			if (time < dist[i]) time = dist[i];
			total++;
		}
		printf("%d %d\n", total, time);
	}
	return 0;
}
#endif

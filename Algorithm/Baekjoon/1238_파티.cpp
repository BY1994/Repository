/*
1238 파티

다익스트라 
C++ stl 코드 참고: https://yabmoons.tistory.com/364 
문제 풀이 코드 참고: https://hyeo-noo.tistory.com/138 
정점마다 우선순위 큐를 어떻게 돌리지, 우선순위큐 배열을 만들 수 있나 하다가 찾았는데,
매번 초기화를 하면 되는 거였다... 

시간이 빠른 풀이들을 보면, 처음에 정보 입력 받을 때 역방향으로도 저장하고,
다익스트라를 같은 방향으로 2번 돌렸다.
이렇게 하면 훨씬 빠르다고 하는데 아직 정확히 이해는 못 했다. 
*/

#include <cstdio>
#include <vector>
#include <queue>

using namespace std;
const int INF = 1000000000;

int N, M, X;
vector<pair<int, int> > v[100001];
vector<int> dist;
int min_dist[1001];
int ans;

void dijkstra(int start){
	dist.clear();
	dist.resize(N+1, INF);
	
	dist[start] = 0;
	
	priority_queue<pair<int, int> > PQ;
	PQ.push(make_pair(0, start));
	
	while (!PQ.empty()) {		
		int cost = -PQ.top().first;
		int cur = PQ.top().second;
		PQ.pop();
		
		for (int i = 0; i< v[cur].size(); ++i) {
			int next = v[cur][i].first;
			int ncost = cost + v[cur][i].second;
			
			if (dist[next] > ncost) {
				dist[next] = ncost;
				PQ.push(make_pair(-ncost, next));
			}
		}
	}
}

int main(void) {
    scanf("%d %d %d", &N, &M, &X);

    for (int i = 0; i < M; ++i) {
        int a, b, c; scanf("%d %d %d", &a, &b, &c);
        v[a].push_back(make_pair(b, c));
    }
    
    for (int i = 1; i <= N; ++i) {
    	dijkstra(i);
		min_dist[i] = dist[X]; 	
	}

    dijkstra(X);

    for (int i = 1; i <= N; ++i) {
    	min_dist[i] += dist[i];
    	ans = max(ans, min_dist[i]);
    }

    printf("%d\n", ans);
    return 0;
}

